import json

class Logger:
    def __init__(self) -> None:
        self.dic_li = dict()

    def save_txt(self):
        # dic_li = [ {'question':input(), 'answer':'2222'}, {'question':'3333', 'answer':'4444'}]

        with open('log_data.txt', 'w') as f:
            for item in self.dic_li:
                f.write(json.dumps(item) + '\n')

    def logging(self,question, answer):
        self.dic_li["question"] = question
        self.dic_li["answer"] = answer
        
      