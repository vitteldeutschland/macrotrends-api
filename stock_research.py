import requests
from bs4 import BeautifulSoup
import json

def research_stock(ticker):
    """macrotrends.net에서 주식 정보 리서치"""
    url = f"https://www.macrotrends.net/stocks/charts/{ticker.lower()}/stock-price-history"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        return json.dumps({
            'ticker': ticker.upper(),
            'url': url,
            'status': 'found'
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({'error': str(e)}, ensure_ascii=False)

def research_multiple_stocks(tickers):
    """여러 주식 동시 리서치"""
    results = []
    for ticker in tickers:
        result = research_stock(ticker)
        results.append(json.loads(result))
    return json.dumps(results, ensure_ascii=False, indent=2)
