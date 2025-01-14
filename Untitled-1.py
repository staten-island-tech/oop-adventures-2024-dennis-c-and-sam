class vendingmachine:
    def __init__(self,drinks):
        self.drinks = drinks
drinks = vendingmachine(["Cola",'Sprite','Dr.pepper'])
print(drinks.drinks)