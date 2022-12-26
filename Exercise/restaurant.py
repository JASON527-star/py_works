
class Restaurant:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.number_served=0
    def describe_restaurant(self):
        print(f'{self.name}餐厅正常营业中！')


    def read_number(self):
        print(f"此餐厅有{self.number_served}人就餐过")

    def set_number_served(self,number2):
        self.number_served=number2

    def increment_number_served(self,number3):
        self.number_served+=number3
        print(f"此餐厅可容纳{self.number_served}人")

restaurant1=Restaurant('清真',99)
print(f"餐厅为{restaurant1.name}餐厅")
print(f"此餐厅已经营{restaurant1.age}年")
restaurant1.describe_restaurant()

restaurant1.set_number_served(100)

restaurant1.read_number()

restaurant1.increment_number_served(20)



'''
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def get_descriptive_name(self):
        long_name=f"{self.make} {self.model} {self.year}"
        return long_name
car1=Car('Audi','r7s',9)
print(car1.get_descriptive_name())
'''

