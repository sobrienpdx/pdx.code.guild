


#dunder or magic methos == _thing_


# class BankAccount:
#     def __init__(self, name): #(other than "self", any arguments in the init need to be passed in when called)
#         self.name = name
#         self.balance = 0
#
#     def deposit(self, amt):  #not a dunder method.. I'm making it.. does not exist in our parent
#         self.balance += amt
#         return "Thank you {}. Your balance is now {}.".format(self.name, self.balance)
#
#     def withdraw(self, amt):
#         if self.balance - amt >= 0:
#             self.balance -= amt
#             return "Thank you {}. Your balance is now {}.".format(self.name, self.balance)
#         return "You do not have enough funds in your account. Your balance is {}.".format(self.balance)
#
#     def __str__(self):
#         return "{}'s' Bank Account".format(self.name)
#
# class BankAccountPlus(BankAccount):
#     def __init__(self, n):
#         super().__init__(n) #calls all the stuff from the parent
#
# chris = BankAccount('Chris')
# print(chris.balance)
# print(chris)

#vehicle, color, wheel number

cars = {prius: [blue, 4]}
class Cars:
    def __init__(self, color, name):
        self.wheels = 4
        self.color = color
        self.name = name

prius = Cars("blue", "Prius")

def print_car(car):
    print("The {} is {} and has {} wheels.".format(car.name, car.color, car.wheels))


for i in cars:
    print_car(car)
# bike = Vehicle(2, "red", "Bike")
# print(bike.color)
# print(bike.wheels)

# from .cars_example import Car  (this can use a class from a different file)

if __name__ == '__main__': #put this everywhere to import only the class not the stuff you did with the class
