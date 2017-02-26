class Girl:
    	#common attributes for all girls

    	def __init__(self, name, attract, intelligence ,budget):
        	self.name = name
        	self.attract = attract
        	self.intelligence = intelligence
        	self.budget = budget
        	self.status = 'Single'
        	self.bname = ''

    	def is_elligible(self, gfbudget):
        	if (self.budget <= gfbudget):
            		return True
        	else:
            		return False
