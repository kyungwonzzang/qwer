from types import MethodDescriptorType
from flask import Flask, request, render_template, session, redirect
from werkzeug.utils import redirect
import db

app = Flask(__name__)
app.secret_key = b'aaa!111/'

def ck_idpw(ret):
    if ret != None:
        return redirect('/loginsuccess')
    else:
        return redirect('/loginfail')

@app.route('/')
def main():
    return render_template('main.html')

# 로그아웃(session 제거)
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/join_action', methods=['GET', 'POST'])
def join_action():
    if request.method == 'GET':
        return '나는 액션 페이지야'
    else:
        userid = request.form['id']
        pwd = request.form['pwd']
        name = request.form['name']
        phone = request.form['phone']
        print(userid, pwd, name, phone)
        # 디비에 데이터 넣기
        db.insert_user(userid, pwd, name, phone)
        return redirect('/loginsuccess')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        userid = request.form['id']
        pwd = request.form['pwd']
        print(userid, pwd)
        ret = db.get_idpw(userid, pwd)
        if ret != None:
            session['user'] = ret[3] # 로그인 처리
            return ck_idpw(ret)

@app.route('/loginsuccess')
def loginsucess():
    return render_template('loginsuccess.html')

@app.route('/loginfail')
def loginfail():
    return render_template('loginfail.html')

@app.route('/duck')
def duck():
    if 'user' in session:
        return render_template('duck.html')
    else:
        return redirect('/login') # 페이지 강제 이동


@app.route('/ipduck')
def ipduck():
    return render_template('ipduck.html')

@app.route('/test/')
def test():
    return render_template('test.html')

@app.route('/joyuriz')
def joyuriz():
    return render_template('joyuriz.html')

@app.route('/joyuriz1')
def joyuriz1():
    return render_template('joyuriz1.html')

@app.route('/joyuriz2')
def joyuriz2():
    return render_template('joyuriz2.html')

@app.route('/joyuriz3')
def joyuriz3():
    return render_template('joyuriz3.html')

if __name__ == '__main__':
    app.run(debug=True)