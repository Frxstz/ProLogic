"""
Assignment 9
Intro to Pro Logic
Github:https://github.com/Frxstz/ProLogic
Author @Frxstz
"""
class Student(object):
    def extra_cost(self):       #This works i guess, can be optimised
        food_payment = (int(0))
        dorms_payment = (int(0))
        DORMS = str(input("Do you plan to get an dormitory on campus? [Yes/No] ")).lower()
        if DORMS == ("yes"):
            dorms_payment = (int(1500))
            FOOD  = str(input("Do you plan to get food delivery on campus? [Yes/No] ")).lower()
            if FOOD == ("yes"):
                food_payment = (int(800))
            else :food_payment = (int(0))
        else :dorms_payment = (int(0))
        addon = dorms_payment + food_payment
        return addon   #Taking extra_cost and turning it into an Int(final_Cost)

    def bus_pass(self):
        BUS = str(input("Would you like to buy a bus pass? ")).lower()
        if BUS == ("yes"):
            Bus_payment = (int(330))
        else :Bus_payment = (int(0))
        addon = Bus_payment
        return addon

s = Student()
X = 0
w = 0           
while True:
    USER = str(input("Do you want to pay for a student? [Yes/No] ")).lower()
    if USER == "yes":
        X = X + 1   #Counter of how many students you registered
        print ("Hello, welcome to the Red River College Student services")
        FULL_NAME = str(input("What is your full name? "))
        number_credits = int(input("How many credits are you taking this term? "))
        Dorms_extra = s.extra_cost()
        Bus_extra = s.bus_pass()
        payment = number_credits*300
        final_payment = payment + Dorms_extra + Bus_extra    #Final Value
        print (f"{FULL_NAME}, For this term you owe us {final_payment}$")
        w = w + final_payment                   #Total Value after all students
    else:
        check1 = (int(0))
        while True:
            def terms(check1):
                Check  = str(input("Do you agree to the terms and conditions? [Yes/No] ")).lower()
                if Check == ("yes"):
                    check1 = (int(1))
                else :check1 = (int(0))
                return check1
            check2 = terms(check1)
            if check2 == 1:
                print("Red River College Thanks you for your Cooperation.")
                print(f"You paid for {X} Student's with a total of {w}$")
                break
            else :print("To Continue you must accept the terms and condtions.")
        break                                   #Break While loop
