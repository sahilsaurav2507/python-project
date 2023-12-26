class recipe():
    def __init__(self,dish,items,time) -> None:
      self.dish = dish
      self.items = items
      self .time = time

    def content(self):
       print("The "+ self.dish + "has " + str(self.items) + \
             "and takes" + str(self.time) + "min to prepare")
       
pizza = recipe("pizza" , ["cheeze", "bread","tomato"],45)
pasta = recipe("pasta",["sauce","penne"],55)

print(pizza.items)
print(pasta.items)

print(pizza.content)
