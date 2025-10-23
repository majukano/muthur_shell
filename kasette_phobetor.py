from datetime import datetime


class KassettePhobetor:
    def __init__(self):
        self.keywords = []
        self.ph_time_str = 'ph_time'
        self.keywords.append(self.ph_time_str)
        self.ph_time_clock_str = ['ph_time', 'clock']
        self.keywords.append(self.ph_time_clock)
        self.hallo_str = 'hallo'
        self.keywords.append(self.hallo_str)
 
    def ph_time(self):
        now = datetime.now()
        time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return time
    
    def ph_time_clock(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        return time 

    def hallo(self):
        return 'Hallo, wie geht es dir?'

    def get_keywords(self):
        return self.keywords
    
    def get_answer(self, input_txt):
        action = {self.ph_time_str: self.ph_time,
                  self.ph_time_clock_str: self.ph_time_clock,
                  self.hallo_str: self.hallo}
        action = action.get(input_txt)
        if action:
            answer = action()
        return answer
        
        
        

