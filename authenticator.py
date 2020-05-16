import mysql.connector as myc


class Authenticator:
    mydb = myc.connect(host="", user="", passwd="", database="")
    mycur = mydb.cursor()

    @staticmethod
    def auth_main(user, passwd):

        mydb = myc.connect(host="", user="", passwd="", database="")
        mycur = mydb.cursor()
        try:
            mycur.execute("SELECT username FROM test_turf.auth_details Where username=\'" + user + "\';")
            result = list(mycur.fetchall())
            mycur.execute("SELECT paswd FROM test_turf.auth_details Where username=\'" + user + "\';")
            result1 = list(mycur.fetchall())
            # print(result)

            x = str(result)
            p = str(result1)
            print(type(x), type(p), p, x)
            a, b = x.find("'"), x.rfind("'")
            x1 = x[(a+1):b].lower()
            a, b = p.find("'"), p.rfind("'")
            p1 = p[(a+1):b].lower()
            print(p1,x1)
            if len(x1) == len(user):
                if x1 == user:
                    if p1 == passwd:
                        if len(passwd) == len(p1):
                            #print("great")
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        except Exception as e:
            print("authentication Failed",e)


#x=input()
#y=input()
#obj=Authenticator()

#obj.auth_main(x,y)
