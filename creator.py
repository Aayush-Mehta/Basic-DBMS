import mysql.connector as myc


class Creator:

    @staticmethod
    def creator_ow(user, passwd, ch):
        mydb = myc.connect(host="", user="", passwd="", database="")
        mycur = mydb.cursor()
        count = 0
        mycur.execute("SELECT username FROM test_turf.auth_details")
        result = list(mycur.fetchall())
        # print(result)
        for i in range(len(result)):
            x = str(result[i])
            # print(type(x))
            a, b = x.find("'"), x.rfind("'")
            x1 = x[a + 1:b]  # print(len(x1),x1)
            if len(user) == len(x1) and user == x1:
                print("User name aldready taken sorry")
                count += 1
                break
        if count != 1:

            mycur.execute(
                "INSERT INTO  `test_turf`. `auth_details`(`username`, `paswd`) VALUES(\'" + user + "\', \'" + passwd + "\');")
            mydb.commit()
            print("Sucessfully added")
            if ch == 1:
                mycur.execute(
                    "CREATE TABLE `test_turf`.`" + user + "` (`Sr.No.` INT NOT NULL AUTO_INCREMENT,`Turf_name` "
                                                          "VARCHAR(45) NOT NULL,`Turf_adress` VARCHAR(45) NOT NULL,`turf_pincode` INT NOT "
                                                          "NULL, PRIMARY KEY (`Sr.No.`));")
                mydb.commit()
                print("Created sucess fully")
            else:
                print("Creaated sucessfully")
        else:
            print("Sorry")


#if __name__ == 'main':
#obj = Creator()
#obj.creator_ow("kartik", "12341234", 1)
