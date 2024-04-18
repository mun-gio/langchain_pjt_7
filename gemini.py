import os
from langchain_google_genai import ChatGoogleGenerativeAI



class Gemini():
    def __init__(self):
        pass
        
    def call_gemini(self):
        #gemini model key
        if "GOOGLE_API_KEY" not in os.environ:
            os.environ["GOOGLE_API_KEY"] = "AIzaSyDUJuLlRr0t7Tr0AojrJ3TdioImcJ8TReQ"

        #Gemini model중 최신버전인 gemini 1.5를 사용함 불러옴. temperature는 기본값으로 설정
        chat = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', temperature=0.7) 
        return chat
