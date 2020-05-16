from data_writer import DataWriter as dw

from datashower import DataShower as ds
import mysql.connector as myc
from authenticator import Authenticator as a


class Owner():
    mydb = myc.connect(host="", user="", passwd="", database="")
    mycur = mydb.cursor()

    @staticmethod
    def owner_main():

        mydb = myc.connect(host="", user="", passwd="", database="")
        mycur = mydb.cursor()
        print("Welcome to the owner module")
        user = input("Enter your username")
        passw = input("Enter your password")
        if a.auth_main(user, passw):
            print("Welcome back Dear owner \nPress one to check the logs of your current turfs\nPress 2 to add a new "
                  "turf on your account\nPress three to exit ")
            ch = int(input())
            if ch == 1:
                x = ds.data_main(user)
                print(x)
                print("press the Name of thr turf to which you want to fetch the data")
                name = input().lower()
                result = ds.data_main(name)
                for i in result:
                    print(i)
            elif ch == 2:
                name = input("Enter the name with which you want to make the entry")
                dw.owner_writer(name, user)
            elif ch == 3:
                print("Thanks for using AM's Database Manager")
                exit(1)
        else:
            print("Authentication Failed")
