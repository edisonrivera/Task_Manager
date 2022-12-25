import datetime



class ToDo:
    def __init__(self, task :str, category: str
                , date_added=datetime.datetime.now().strftime("%d/%m/%Y"), 
                date_completed=None, status=None, position=None) -> None:
        self.task = task
        self.category = category
        self.date_added = date_added
        self.date_completed = date_completed
        self.status = status
        self.position = position

    def __repr__(self) -> str:
        return f"""({self.task}, {self.category}, {self.date_added}
                , {self.date_completed}, {self.status}, {self.position}"""