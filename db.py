import pymysql

def insert_user(userid, pw, name, phone):
    try:
        db = pymysql.connect(host='ruddnjs5547.mysql.pythonanywhere-services.com',
                   user='ruddnjs5547', password='12345678',
                   db='ruddnjs5547$mydb', charset='utf8')
        c = db.cursor()
        setdata = (userid, pw, name, phone)
        c.execute("INSERT INTO user_tb (id, pw, name, phone)  VALUES (%s, %s, %s, %s)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def get_idpw(userid, pw):
    ret = ()
    try:
        db = pymysql.connect(host='127.0.0.1',
                   user='root', password='1234',
                   db='taxidb', charset='utf8')
        c = db.cursor()
        setdata = (userid, pw)
        db.get_idpw(userid, pw)
        c.execute("SELECT * FROM user_tb WHERE id = %s AND pw = %s", setdata)
        ret = c.fetchone()
        #print(ret)
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

#get_idpw('aaaa', '123')