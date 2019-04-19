class Message:
    def __init__(self, index, user_name, text, time):
        self.user_name = user_name
        self.message = text
        self.time = time
        self.index = index