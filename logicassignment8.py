"""
Logic assigment 8
Author @Frxstz
https://github.com/Frxstz/ProLogic/blob/main/logicassignment8.py
Oct_2022
Funtions Assignment
"""
class Student:
    X = 0
    w = 0
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
            Dorms_extra = extra_cost()   #Taking extra_cost and turning it into an Int(final_Cost)
            
            def bus_pass():
                BUS = str(input("Would you like to buy a bus pass? ")).lower()
                if BUS == ("yes"):
                    Bus_payment = (int(330))
                else :Bus_payment = (int(0))
                addon = Bus_payment
                return addon
            Bus_extra = bus_pass()
            
            #Taking the Final_cost and turning it into Final_payment
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
                    print("--- --- College Thanks you for your Cooperation.")
                    print(f"You paid for {X} Student's with a total of {w}$")    #How many students you paid for 
                    break
                else :print("To Continue you must accept the terms and condtions.")
            break                                   #Break While loop
