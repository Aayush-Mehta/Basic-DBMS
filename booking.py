import mysql.connector as myc


class Booking:
    @staticmethod
    def booking_main(user):
        mydb = myc.connect(host="", user="", passwd="", database="")
        mycur = mydb.cursor()
        print("This is th list of all the turfs available on AM's turf manager")
        try:
            mycur.execute("Select `Turf Name` From all_turfs")
        except Exception as e:
            print("Something went wrong", e)
        result = mycur.fetchall()
        y = 0
        for i in range(len(result)):
            x = str(result[i])
            # print(type(x))
            a, b = x.find("'"), x.rfind("'")
            x1 = x[a + 1:b]
            print(y, "- " + x1)
            y += 1
        print("Enter your choice of Turf")
        name = input().lower()
        print("Enter the date of your bookin in the format yyyy-mm-dd")
        date = input()
        print("The Availability of " + name + "in 24 hour format is as follows")
        try:
            mycur.execute("Select ` Time Of Start` from " + name + " Where `Date Of Booking` = \'" + date + "\';")
            result = mycur.fetchall()
            for i in range(0, 25, 1):
                if i in result:
                    continue
                else:
                    print(i)
            print("Enter Your Prefered Time of booking and if you wish to exit press 1 else any key")
            n = int(input())
            if n == 1:
                exit(12)
            else:
                times = int(input("Enter the time os start for your booking in 24 hour format"))
                timee = times + 1
                sql = "INSERT INTO `test_turf`.`d7` (`Name Of Customer`, `Date of Booking`, ` Time Of Start`, `Time Of " "End`)VALUES(\'" + user + "\', \'" + date + "\', \'" + str(
                    times) + "\', \'" + str(timee) + "\');"
                print(sql)
                try:
                    mycur.execute(sql)
                    mydb.commit()
                    print("Booking made for the slot ", times, "-", timee)
                except Exception as e:
                    print ("something went wrong",e)
        except Exception as e:
            print("Something Went wrong",e)

    # INSERT INTO `test_turf`.`d7` (`Name Of Customer`, `Date of Booking`, ` Time Of Start`, `Time Of End`) VALUES (
    # 'cxcx', '2019-11-11', '12', '11');

    # booking_main("Aayush")
    @staticmethod
    def checker(user, check):
        mydb = myc.connect(host="", user="", passwd="", database="")
        mycur = mydb.cursor()
        print("fetching results for your request")
        mycur.execute("SELECT * FROM `" + check + "` WHERE `Name Of Customer`=\'" + user + "\';")
        x = mycur.fetchall()
        for i in x:
            print(" Sr.no: " + str(i[0]) + "\n Name Of customer " + str(i[1]) + "\n Date of booking " + str(
                i[2]) + "\n Starting Time " + str(i[3]) +
                  "\n Ending Time " + str(i[4]))
