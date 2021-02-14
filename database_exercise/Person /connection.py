import pymysql


class Connect_to():

    def connect_to_database(self):
        try:
            cn = pymysql.Connect(host="localhost", user="poulstar",
                                 password="poulstar", db="information")
            cr = cn.cursor()
            print("connected")
        except:
            print("not connected")
        finally:
            print("I'm a programmer")

        return cn, cr


Connect_to().connect_to_database()
