import json
import urllib.request
import xml.etree.ElementTree as ET
import os

def lambda_handler(event, context):
    """
    Phase 2 (第1歩): RSSニュースを取得し、隔離されたプロンプトファイル(JSON)を読み込む
    """
    # 1. 先ほど作ったPMBOK第8版のルールブック(JSON)を読み込む
    # ※GitHub上の prompts/ フォルダと同じ階層からファイルを読み込みます
    rules_path = os.path.join(os.path.dirname(__file__), 'prompts', 'pmbok_8th_rules.json')
    
    try:
        with open(rules_path, 'r', encoding='utf-8') as f:
            pmbok_rules = json.load(f)
        print("Successfully loaded PMBOK 8th rules.")
    except Exception as e:
        print(f"Failed to load PMBOK rules from {rules_path}: {str(e)}")
        pmbok_rules = {"error": "Rules file not found or invalid"}

    # 2. テックニュース（RSSフィード）の収集
    rss_url = "https://aws.amazon.com/about-aws/whats-new/recent/feed/"
    articles = []
    
    try:
        req = urllib.request.Request(rss_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        for item in root.findall('.//item')[:3]:  # テスト用に最新3件に絞ります
            title = item.find('title').text if item.find('title') is not None else "No Title"
            link = item.find('link').text if item.find('link') is not None else ""
            description = item.find('description').text if item.find('description') is not None else ""
            
            articles.append({
                "title": title,
                "link": link,
                "description": description
            })
            
    except Exception as e:
        print(f"Error fetching RSS: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to fetch news data'})
        }

    # 3. 取得したニュースと、読み込んだPMBOKのルールを両方返却する
    # ※次のステップで、この2つのデータをClaudeのプロンプトに結合します
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Successfully fetched tech news and loaded rules',
            'pmbok_framework': pmbok_rules.get('framework', 'Unknown'),
            'news_count': len(articles),
            'articles': articles
        }, ensure_ascii=False)
    }
