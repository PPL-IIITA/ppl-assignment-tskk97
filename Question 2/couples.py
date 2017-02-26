class Couple:
    #common attributes for couples
    def __init__(self,boy,girl):
        self.boy = boy
        self.girl = girl
        self.happiness = 0
        self.compatibility = 0
        self.GFT = []

    def set_happiness(self):
        self.happiness = self.girl.happiness + self.boy.happiness

    def set_compatibility(self):
        m = self.boy.budget - self.girl.budget
        n = abs(self.boy.intelligence - self.girl.intelligence)
        o = abs(self.boy.attract - self.girl.attract)
        self.compatibility = m+n+o
