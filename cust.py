import booking
from authenticator import Authenticator as a
import mysql.connector as myc
from booking import *


class Cust():
    mydb = myc.connect(host="", user="", passwd="", database="")
    mycur = mydb.cursor()
    @staticmethod
    def cust_main():
        print("Welcome to the Customer module")
        user = input("Enter your username")
        passw = input("Enter your password")
        if a.auth_main(user, passw):
            print("Welcome back Customer\nPress 1 to make a booking\nPress 2 to check an existing booking\nPress any "
                  "other key to exit")
            n = int(input("Enter your choice now"))
            if n == 1:
                Booking.booking_main(user)
            elif n == 2:
                print("Enter the name of the turf with which you made the booking")
                check = input("Here")
                Booking.checker(user, check)
            else:
                print("Thanks for Using AM's DBMS")
                exit(1)
        else:
            print("Authentication Failed")

# cust_main()
