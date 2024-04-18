from crawler import Crawler
from gemini import Gemini
from rag import Rag
from logger import Logger

def main():
    question=input("User : ")
    data=Crawler().crawler()
    ai=Gemini().call_gemini()
    system_active=Rag()
    logger = Logger()

    db=system_active.vectorlization(data)
    context=system_active.retriever(db,question)
    generate_answer=system_active.generate(context,question,ai)
    logger.logging(question,generate_answer)
    logger.save_txt()


if __name__ =="__main__":
    main()