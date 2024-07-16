class Task:
    def __init__(self, id, title,desc,status=False) -> None:
        self.id = id
        self.desc = desc
        self.status = status
        self.title = title
    
    def todict(self):
        return{
            "desc":self.desc,
            "ID":self.id,
            "title":self.title,
            "status":self.status,
        }
