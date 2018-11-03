class myiter:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.no=0
        return self
    def __next__(self):
        if self.max>self.no:
            self.no+=1
            return self.no
