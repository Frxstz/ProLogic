"""intro2ProgramingLogic_assigment7"""
#Frxstz
#oct_2022

X = 0
while True:
    USER = str(input("Do you want to pay for a student? [Yes/No] ")).lower()
    if USER == "yes":
        X = X + 1
        #general_data_collection
        print ("Hello, welcome to the Collge Student services")
        FULL_NAME = str(input("What is your full name? "))
        number_credits = int(input("How many credits are you taking this term? "))
        DORMS = str(input("Do you plan to get an dormitory on campus? [Yes/No] ")).lower()

        #dorms_payment
        if DORMS == ("yes"):
            DORMS_PAYMENT = (int(1500))
        else :DORMS_PAYMENT = (int(0))

        #food_payment
        FOOD = ""
        if DORMS == ("yes"):
            FOOD  = str(input("Do you plan to get food delivery on campus? [Yes/No] ")).lower()
        if FOOD == ("yes"):
            FOOD_PAYMENT = (int(800))
        else :FOOD_PAYMENT = (int(0))

        #calculating_final_payment
        payment = number_credits*300
        final_payment = payment + DORMS_PAYMENT + FOOD_PAYMENT
        print (f"{FULL_NAME}, For this term you owe us {final_payment}$")
    else:     
        print(f"{X}")
        break
