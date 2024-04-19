# langchain_pjt_7

## Langchain_
#### 잦은 야근에 지친 이어드림스쿨 수강생들의 비타민이 되어줄 **Langchain 영양박사 챗봇 'Dr.알려드림'입니다.🧐**

1. **Data Crawl**을 통해 User의 질문에 **맞춤형 영양소 정보를 제공**하는 챗봇입니다. 

2. 저희가 Crawling한 해외사이트는 **공신력있는 전문 데이터를 제공**합니다.

3. **영양학 박사 학위가 있는 한국인 약사**라는 Persona를 주어 공신력 있는 정보를 한국어로 간편하게 얻을 수 있습니다.

---

## Persona_

1. 영문사이트( https://examine.com )를 Crawling한 데이터에 기반하기 때문에 **영어로 질문할 시 답변 정확도가 더 높습니다.**

2. 사용자 편의를 위해 **모든 답변은 한국어**로 하며, 사이트에 없는 내용은 가급적 답변하지 않습니다.

3. 증상을 입력하면 여기에 대한 **영양소를 추천해주고 효능, 효과와 주의사항**을 안내해줍니다.

4. 추가 답변을 원하면 한번 더 질문을 입력하고, 답변에 만족하면 **'종료'를 입력해주세요.**

---

## File Description_


### 1. Main.py
 - main.py에서 input(증상)을 입력하면, **While Flag 함수**를 통해 '종료'를 입력하기 전까지 question을 반복합니다.

### 2. Crawler.py
 - examine.com에서 영양소 정보를(nutrients) **Crawl해서 docs변수에 저장**합니다.

### 3. Gemini.py
 - Gemini model중 최신버전인 **gemini 1.5를 호출**합니다.

### 4. RAG.py
 - Crawl해서 가져온 **데이터를 Split해 Retriever변수에 저장**합니다.
 - **Gemini의 Persona를 정의**해 원하는 형태로 답변을 이끌어냅니다. 

### 5. Logger.py
 - 사용자의 질문과 챗봇의 답변을 **txt형태**로 저장합니다.
