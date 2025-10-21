from datetime import datetime


class KassettePhobetor:
    def __init__(self):
        self.keywords = []
        self.keywords.append('ph_time')
 
    def ph_time(self):
        now = datetime.now()
        time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return time

    def get_keywords(self):
        return self.keywords
    
    def get_answer(self, input_txt):
        action = {'ph_time': self.ph_time}
        action = action.get(input_txt)
        if action:
            answer = action()
        return answer
        
        
        

