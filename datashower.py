import mysql.connector as myc


class DataShower:
    @staticmethod
    def data_main(user):
        mydb = myc.connect(host="", user="", passwd="", database="")
        mycur = mydb.cursor()
        user.lower()
        try:
            sql = "SELECT * FROM "
            mycur.execute(sql + user)
            result = list(mycur.fetchall())
        # for i in result:
        #   print(i)
            return result
    # data_main("Aayush")
        except Exception as e:
            print("Something Went wrong", e)