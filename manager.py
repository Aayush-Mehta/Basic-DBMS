from datashower import DataShower as ds
from authenticator import Authenticator as a


class Manager:
    @staticmethod
    def manager_main():
        print("Welcome to the Manager module")
        user = input("Enter your username")
        passw = input("Enter your password")
        if a.auth_main(user, passw):
            print("Welcome back Manager")
            print("Enter The Turf under your Jurisdiction")
            name = input().lower()
            x = ds.data_main(name)
            for i in x:
                print(i)
        else:
            print("Authentication Failed")

# manager_main()
