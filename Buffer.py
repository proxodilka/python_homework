class Buffer:
    def __init__(self):
        self.part = []
    def add(self, *a):
        for i in a:
            self.part.append(i)
            if len(self.part) == 5:
                print(sum(self.part))
                self.part=[]
    def get_current_part(self):
        return self.part