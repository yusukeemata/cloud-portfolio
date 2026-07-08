import json
import urllib.request
import xml.etree.ElementTree as ET

def lambda_handler(event, context):
    """
    Phase 1: テックニュース（RSSフィード）を自動収集するMVP用Lambda関数
    """
    # テスト用のRSSフィードURL（例としてAWSの最新情報フィードを設定）
    rss_url = "https://aws.amazon.com/about-aws/whats-new/recent/feed/"
    
    articles = []
    
    try:
        # 1. RSSフィード（XML）をダウンロード
        req = urllib.request.Request(
            rss_url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()
            
        # 2. XMLデータを解析して記事のタイトルやリンクを抽出
        root = ET.fromstring(xml_data)
        
        # RSS 2.0形式の解析（<item> タグを探す）
        for item in root.findall('.//item')[:5]:  # 最初はテスト用に最新5件だけ
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

    # 3. 取得したニュース一覧を返却（のちにPhase 2でこれをClaudeに渡します）
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Successfully fetched tech news',
            'news_count': len(articles),
            'articles': articles
        }, ensure_ascii=False)
    }
