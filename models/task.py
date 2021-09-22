class Task:

    def __init__(self, description, user, duration, completed = False,  id = None, ):
        self.description = description
        self.user = user
        self.duration = duration
        self.completed = completed
        self.id = id

    def mark_complete(self):
        self.completed = True
