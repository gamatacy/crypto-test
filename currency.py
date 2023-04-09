class Currency:

    def __init__(self, name, bot_value, high_value):
        self.name = name
        self.bot_value = bot_value
        self.top_value = high_value

    def get_info(self):
        return [self.name, self.bot_value, self.top_value]

