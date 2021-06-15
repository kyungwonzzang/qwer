from types import MethodDescriptorType
from flask import Flask, request, render_template, session, redirect
from werkzeug.utils import redirect
from func import ck_idpw # 내가 만든 id pw 체크함수
import db

app = Flask(__name__)
app.secret_key = b'aaa!111/'

@app.route('/')
def duck():
    return render_template('main.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/naver')
def hello3():
    return '안녕 나는 네이버야~'

@app.route('/coin')
def coin():
    #return render_template('coin.html')
    if 'user' in session:
        return '여기는 코인 거래소 사용자만'
    else:
        return redirect('/login') # 페이지 강제 이동

# 로그아웃(session 제거)
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/action_page', methods=['GET', 'POST'])
def action_page():
    if request.method == 'GET':
        return '나는 액션 페이지야'
    else:
        search = request.form['search']
        return '''당신은 "{}"로 검색을 했습니다.</br>
        결과를 보여드리겠습니다. 잠시만 기다려주세요.</br>
        리스트 쫙~~~~
        '''.format(search)

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
        return '회원가입 성공!!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        print(id,pw)
        ret = db.get_idpw(id, pw)
        if ret != None:
            session['user'] = ret[3] # 로그인 처리
        return ck_idpw(ret)

# if __name__ == '__main__':
#     app.run()