
import pymysql

def insert_user(userid, pw, name, phone):
    try:
        db = pymysql.connect(host='ruddnjs5547.mysql.pythonanywhere-services.com',
                   user='ruddnjs5547', password='asd123456',
                   db='ruddnjs5547$mydb', charset='utf8')
        c = db.cursor()
        setdata = (userid, pw, name, phone)
        c.execute("INSERT INTO user (id, pw, name, phone) VALUES (%s, %s, %s, %s)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def get_idpw(userid, pw):
    ret = ()
    try:
        db = pymysql.connect(host='ruddnjs5547.mysql.pythonanywhere-services.com',
                   user='ruddnjs5547', password='asd123456',
                   db='ruddnjs5547$mydb', charset='utf8')
        c = db.cursor()
        setdata = (userid, pw)
        c.execute("SELECT * FROM user WHERE id = %s AND pw = %s", setdata)
        ret = c.fetchone()
        #print(ret)
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret