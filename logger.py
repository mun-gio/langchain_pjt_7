import json

class Logger:
    def save_txt(self, data):
        # self.data = data
        # dic_li = [ {'question':'1111', 'answer':'2222'}, {'question':'3333', 'answer':'4444'}]

        with open('log_data.txt', 'w') as f:
            for item in data:
                f.write(json.dumps(item) + '\n')