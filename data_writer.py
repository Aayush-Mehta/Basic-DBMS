import mysql.connector as myc


class DataWriter:

    @staticmethod
    def owner_writer(name, user):
        mydb = myc.connect(host="", user="", passwd="", database="")
        mycur = mydb.cursor()
        name.lower()
        user.lower()
        try:
            sql="CREATE TABLE `test_turf`.`"+ name +"` (`Name Of Customer` VARCHAR(45) NOT NULL,`Date of Booking` DATE NOT NULL,` Time Of Start` INT NULL DEFAULT NULL,`Time Of End` INT NULL DEFAULT NULL);"
            mycur.execute(sql)
            try:
                sql = "Insert Into `all_turfs` (`Turf Name`, `Owner Name`)Values(\'" + name + "\', \'" + user + "\');"

                mycur.execute(sql)
                mydb.commit()
                pincode = (input("Enter The pincode of the new turf"))
                turf_adress = input()
                try:
                    sql1 = "Insert Into `" + user + "`(`Turf_name`, `Turf_adress`, `turf_pincode`)Values(\'" + name + "\', \'" + turf_adress + "\', \'" + pincode + "\');"
                    mycur.execute(sql1)
                    mydb.commit()
                except Exception as e:
                    print("Something Went wrong", e)
            except Exception as e:
                print("Something Went wrong", e)
        except Exception as e:
            print("Something Went wrong", e)