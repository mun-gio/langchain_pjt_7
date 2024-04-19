from crawler import Crawler
from gemini import Gemini
from rag import Rag
from logger import Logger

def main():
    
    data=Crawler().crawler()
    ai=Gemini().call_gemini()
    system_active=Rag()
    logger = Logger()

    flag = 1
    while flag:
        question=input("안녕하세요 당신을 위한 영양박사 챗봇 'Dr.알려드림'입니다. \n어디가 불편하신가요? 증상을 입력해주세요. : ")
        if question != '종료':
            db=system_active.vectorlization(data)
            context=system_active.retriever(db,question)
            generate_answer=system_active.generate(context,question,ai)
            logger.logging(question,generate_answer)
            logger.save_txt()
            print("다른 답변을 원하시면 한번 더 질문해주세요😁 \n답변에 만족하시면 '종료'를 입력해주세요🥺")
        else:
            flag = 0

if __name__ =="__main__":
    main()