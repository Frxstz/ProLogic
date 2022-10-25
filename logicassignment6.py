"""intro2ProgramingLogic_assigment6"""
#daniel_Gauthier
#oct_2022

#general_data_collection
print ("Hello, welcome to the Red River Collge Student services")
FULL_NAME = str(input("What is your full name? "))
number_credits = int(input("How many credits \
 are you taking this term? "))
DORMS = str(input("Do you plan to get an dormitory \
on campus? [Yes/No] ")).lower()

#dorms_payment
if DORMS == ("yes"):
    DORMS_PAYMENT = (int(1500))
else :DORMS_PAYMENT = (int(0))

#calculating_final_payment
payment = number_credits*300
final_payment = payment + DORMS_PAYMENT
print (f"{FULL_NAME}, For this term you owe us {final_payment}$, \
Please proceed with payment.")
