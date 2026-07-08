import json
import urllib.request
import xml.etree.ElementTree as ET
import os
import boto3

def lambda_handler(event, context):
    """
    Phase 2: RSSニュースを取得し、隔離されたJSONルールブックを読み込み、
    Amazon Bedrock (Claude) でPMBOK 8th視点の分析インサイトを生成する
    """
    # 1. プロンプトファイル(JSONルールブック)の読み込み
    rules_path = os.path.join(os.path.dirname(__file__), 'prompts', 'pmbok_8th_rules.json')
    try:
        with open(rules_path, 'r', encoding='utf-8') as f:
            pmbok_rules = json.load(f)
    except Exception as e:
        print(f"Failed to load PMBOK rules: {str(e)}")
        pmbok_rules = {}

    # 2. テックニュース（RSSフィード）の収集
    rss_url = "https://aws.amazon.com/about-aws/whats-new/recent/feed/"
    articles = []
    try:
        req = urllib.request.Request(rss_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        for item in root.findall('.//item')[:1]:  # テスト時は最も最新の1件に絞って処理
            title = item.find('title').text if item.find('title') is not None else "No Title"
            link = item.find('link').text if item.find('link') is not None else ""
            description = item.find('description').text if item.find('description') is not None else ""
            articles.append({"title": title, "link": link, "description": description})
    except Exception as e:
        print(f"Error fetching RSS: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'error': 'Failed to fetch news'})}

    if not articles:
        return {'statusCode': 200, 'body': json.dumps({'message': 'No articles found'})}

    target_article = articles[0]

    # 3. Amazon Bedrock (Claude) の呼び出し準備
    # ※定義書のコスト最適化戦略に基づき、開発・検証時は最安の Haiku を使用
    bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')
    model_id = "anthropic.claude-3-haiku-20240307-v1:0" 

    # 外部化したルールブックとニュースを結合してプロンプト（指示文）を組み立てる
    prompt_content = f"""
You are an expert Technical Project Manager. Analyze the following technology news item using the PMBOK 8th Edition framework provided below.

[PMBOK 8th Framework Rules]
{json.dumps(pmbok_rules, ensure_ascii=False, indent=2)}

[Target News Item]
Title: {target_article['title']}
Description: {target_article['description']}

[Instructions]
1. Identify which PMBOK 8th Principle or Governance Process this news impacts most.
2. Provide a brief professional insight outlining the strategic management impact.
3. Output the response strictly in Japanese.
"""

    # Bedrock (Anthropic API) の要求フォーマットに整形
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": prompt_content
            }
        ]
    })

    try:
        # Claudeモデルの呼び出し実行
        response = bedrock.invoke_model(body=body, modelId=model_id)
        response_body = json.loads(response.get('body').read())
        ai_insight = response_body['content'][0]['text']
    except Exception as e:
        print(f"Bedrock invocation failed: {str(e)}")
        ai_insight = f"Failed to generate AI insight due to an error: {str(e)}"

    # 4. 最終成果（ニュース情報 + PMBOK分析インサイト）を返却
    return {
        'statusCode': 200,
        'body': json.dumps({
            'status': 'Success',
            'target_news': {
                'title': target_article['title'],
                'link': target_article['link']
            },
            'pmbok_analysis': ai_insight
        }, ensure_ascii=False)
    }
