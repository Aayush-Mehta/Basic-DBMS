from manager import Manager
from owner import Owner
from cust import Cust
from creator import Creator


class Final:
    @staticmethod
    def main_final():
        print("Welcome to AM's Turf Management System\nPress 1 if you are an existing User\nPress any other key to "
              "create an acoount")
        n = int(input())
        if n == 1:
            print("Welcome back User\nIf you are an owner press 1\nIf you are an employee/manager press 2\n if you "
                  "are an customer press 3")
            ch = int(input())
            if ch == 1:
                Owner.owner_main()
            elif ch == 2:
                Manager.manager_main()
            elif ch == 3:
                Cust.cust_main()
            else:
                print("Damn! we think you didn't get that, invalid syntax")
        else:
            print("Press 1 if you want to sign up as a owner\nPress 2 if you want to sign up as a manager\nPress 3 "
                  "you want to sign up as a Customer")
            ch = int(input())
            if ch == 1:
                user = input("Enter a username of your choice")
                passwd = input("enter a pass of your choice")
                Creator.creator_ow(user, passwd, 1)
            elif ch == 2:
                user = input("Enter a username of your choice")
                passwd = input("enter a pass of your choice")
                Creator.creator_ow(user, passwd, 2)


obj = Final()
Final.main_final()
