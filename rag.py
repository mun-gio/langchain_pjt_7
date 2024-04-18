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
    
    def generate(self,context,question):
        template = """Answer the question based only on the following context:

        {context}

        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)
        model = ChatGoogleGenerativeAI(model='gemini-pro')


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
