# crawling 한 데이터를 받아서 vecotr DB에 저장을 하고 유저 input을 받아서 Retriever해서 chat 에 generate까지 함. 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


class Rag:
    def _init__(self):
        pass

    def vectorlization(self,data):
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
        docs=text_splitter.split_documents(data)
        vectordb=Chroma.from_documents(docs,
                                       embedding=GoogleGenerativeAIEmbeddings(model='models/embedding-001'))
        return vectordb

    def retriever(self,KB,User_input):
        retriever=KB.as_retriever()
        #docs=retriever.get_relevant_documents(User_input)

        return retriever
    
    def generate(self,context,question,model):
        template = """너는 영양소 정보에 대해서 잘 아는 한국인 약사야. 이제부터 모든 대답은 한국말로 해줘. 물어보는 질문에 대해서 아래 내용을 토대로 입력된 내용에 대해 답변해줘. 아래 context에 원하는 답변이 없으면 모르겠다고 해줘.:

        {context}

        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)

        def format_docs(docs):
            return "\n\n".join([d.page_content for d in docs])


        chain = (
            {"context": context | format_docs, "question": RunnablePassthrough()}
                | prompt
                | model
                | StrOutputParser()
                )
        print(chain.invoke(question))
        return chain.invoke(question)
