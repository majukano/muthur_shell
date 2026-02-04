from datetime import datetime


class KassettePhobetor:
    def __init__(self):
        self.action_keys = {}
        self.the_keywords()

    def ph_time(self):
        now = datetime.now()
        time = now.strftime("%d/%m/%Y, %H:%M:%S")
        return time

    def ph_time_clock(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        return time

    def hallo(self):
        return "Hallo, wie geht es dir?"

    def get_keywords(self):
        keywords = []
        for key in self.action_keys:
            keywords.append(key)
        return keywords

    def get_answer(self, input_txt):
        answer = ""
        action = self.action_keys.get(input_txt)
        if action:
            answer = action()
        return answer

    def the_keywords(self):
        self.action_keys[("ph_time",)] = self.ph_time
        self.action_keys[("ph_time", "clock")] = self.ph_time_clock
        self.action_keys[("hallo",)] = self.hallo
