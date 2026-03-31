"""
Gemini AI와의 통합을 위한 모듈
"""

from stock_research import research_stock, research_multiple_stocks
import json

class GeminiStockTool:
    """Gemini를 위한 주식 리서치 도구"""
    
    @staticmethod
    def get_tool_definition():
        """Gemini에 등록할 Tool 정의"""
        return {
            "name": "research_macrotrends_stock",
            "description": "macrotrends.net에서 주식 데이터를 리서치합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "주식 종목코드 (예: AAPL, MSFT, GOOGL, TSLA 등)"
                    }
                },
                "required": ["ticker"]
            }
        }
    
    @staticmethod
    def execute_tool(ticker: str) -> str:
        """Tool 실행"""
        return research_stock(ticker)
    
    @staticmethod
    def get_tool_definition_multiple():
        """여러 주식을 리서치할 Tool 정의"""
        return {
            "name": "research_multiple_stocks_macrotrends",
            "description": "macrotrends.net에서 여러 주식의 데이터를 동시에 리서치합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "tickers": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "주식 종목코드 리스트 (예: [AAPL, MSFT, GOOGL])"
                    }
                },
                "required": ["tickers"]
            }
        }
    
    @staticmethod
    def execute_tool_multiple(tickers: list) -> str:
        """여러 주식 Tool 실행"""
        return research_multiple_stocks(tickers)
