"""intro2ProgramingLogic_assigment7"""
#daniel_Gauthier
#oct_2022
class Student:
    X = 0
    while True:
        USER = str(input("Do you want to pay for a student? [Yes/No] ")).lower()
        if USER == "yes":
            X = X + 1
            #general_data_collection
            print ("Hello, welcome to the Red River Collge Student services")
            FULL_NAME = str(input("What is your full name? "))
            number_credits = int(input("How many credits are you taking this term? "))

            def extra_cost(DORMS_PAYMENT, FOOD_PAYMENT):
                DORMS = str(input("Do you plan to get an dormitory on campus? [Yes/No] ")).lower()
                if DORMS == ("yes"):
                    DORMS_PAYMENT = (int(1500))
                    FOOD  = str(input("Do you plan to get food delivery on campus? [Yes/No] ")).lower()
                    if FOOD == ("yes"):
                        FOOD_PAYMENT = (int(800))
                    else :FOOD_PAYMENT = (int(0))
                else :DORMS_PAYMENT = (int(0))
                print(f"{DORMS_PAYMENT}")

            DORMS_PAYMENT = (int(0))
            FOOD_PAYMENT = (int(0))
            extra_cost(DORMS_PAYMENT, FOOD_PAYMENT)
            payment = number_credits*300
            final_payment = payment + DORMS_PAYMENT + FOOD_PAYMENT
            print (f"{FULL_NAME}, For this term you owe us {final_payment}$")
        else:     
            print(f"You paid for {X} Student's")
            break
