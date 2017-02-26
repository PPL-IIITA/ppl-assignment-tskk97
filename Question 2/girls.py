class Girl:
    #common attribute for all girls
    def __init__(self, name, attract, intelligence, budget, typ):
        self.name = name
        self.attract = attract
        self.intelligence = intelligence
        self.budget = budget
        self.status = 'Single'
        self.bname = ''
        self.happiness = 0
        self.type = typ

    def is_elligible(self, gfbudget):
        if (self.budget <= gfbudget):
            return True
        else:
            return False
