class Currency:

    def __init__(self, name, bot_value, high_value):
        self.name = name
        self.bot_value = bot_value
        self.top_value = high_value

    def get_info(self):
        return [self.name, self.bot_value, self.top_value, self.get_diff()]

    def get_diff(self):
        try:
            return str(abs((float(self.top_value) - float(self.bot_value)) / (
                    (float(self.top_value) + float(self.bot_value)) / 2)) * 100)[:5] + "%"
        except:
            return ""
