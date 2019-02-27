class cell:
    ingredient = ''
    belongsToSlice = False
    
    def __init__(self, ingredient, belongsToSlice):
        self.ingredient = ingredient
        self.belongsToSlice = belongsToSlice
		
	def setBelongsToSlice(self):
		if (!self.belongsToSlice):
			self.belongsToSlice = true
			return true
		else 
			return false
		
	
			
	
		