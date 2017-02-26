class Boy:
    #common attributes for all boys.

    def __init__(self, name, attract, intelligence, budget, min_atr_req, typ):
        self.name = name
        self.attract = attract
        self.intelligence = intelligence
        self.budget = budget
        self.min_atr_req = min_atr_req
        self.status = 'Single'
        self.gname = ''
        self.happiness = 0
        self.type = typ

    def is_elligible(self,mbudget,attract):
        if (self.budget >= mbudget) and (attract >= self.min_atr_req):
            return True
        else:
            return False
