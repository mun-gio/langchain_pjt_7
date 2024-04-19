import json

class Logger:
    def __init__(self) -> None:
        self.dic_li = []

    def logging(self,question, answer):
        self.dic_li.append({})
        self.dic_li[-1]["question"] = question
        self.dic_li[-1]["answer"] = answer
        # print(self.dic_li)

    def save_txt(self):
        # dic_li = [ {'question':input(), 'answer':'2222'}, {'question':'3333', 'answer':'4444'}]

        with open('log_data.txt', 'w') as f:
            for item in self.dic_li:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        # print(self.dic_li)
      