class Task:
    def __init__(self, id, title,desc,status=False) -> None:
        self.id = id
        self.desc = desc
        self.status = status
        self.title = title
    
    def todict(self):
        return{
            "Description":self.desc,
            "ID":self.id,
            "Title":self.title,
            "Status":self.status,
        }
