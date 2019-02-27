class cell:
    ingredient = ''
    belongsToSlice = False
    
    def __init__(self, ingredient, belongsToSlice):
        self.ingredient = ingredient
        self.belongsToSlice = belongsToSlice