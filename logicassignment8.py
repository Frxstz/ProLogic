"""
Logic assigment 8
Author @Frxstz
https://github.com/Frxstz/ProLogic/blob/main/logicassignment8.py
Oct_2022
Funtions Assignment
"""
class Student:
    X = 0
    while True:
        USER = str(input("Do you want to pay for a student? [Yes/No] ")).lower()
        if USER == "yes":
            X = X + 1   #Counter of how many students you registered
            print ("Hello, welcome to the College Student services")
            FULL_NAME = str(input("What is your full name? "))
            number_credits = int(input("How many credits are you taking this term? "))

            def extra_cost():       #This works i guess, can be optimised
                FOOD_PAYMENT = (int(0))
                DORMS_PAYMENT = (int(0))
                DORMS = str(input("Do you plan to get an dormitory on campus? [Yes/No] ")).lower()
                if DORMS == ("yes"):
                    DORMS_PAYMENT = (int(1500))
                    FOOD  = str(input("Do you plan to get food delivery on campus? [Yes/No] ")).lower()
                    if FOOD == ("yes"):
                        FOOD_PAYMENT = (int(800))
                    else :FOOD_PAYMENT = (int(0))
                else :DORMS_PAYMENT = (int(0))
                addon = DORMS_PAYMENT + FOOD_PAYMENT
                return addon
            Final_cost = extra_cost()   #Taking extra_cost and turning it into an Int(final_Cost)
            print(f"{Final_cost}")
            #Taking the Final_cost and turning it into Final_payment
            payment = number_credits*300
            final_payment = payment + Final_cost    #Final Value
            print (f"{FULL_NAME}, For this term you owe us {final_payment}$")
        else:
            print(f"You paid for {X} Student's")    #How many students you paid for 
            break                                   #Break While loop
