from types import MethodDescriptorType
from flask import Flask, request, render_template
from func import ck_idpw # 내가 만든 id pw 체크함수
app = Flask(__name__)

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
    return render_template('coin.html')

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
        userid = request.form['userid']
        pwd = request.form['pwd']
        name = request.form['name']
        phone = request.form['phone']
        print(userid, pwd, name, phone)
        return '회원가입 성공!!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        print(id,pw)
        return ck_idpw(id, pw)

if __name__ == '__main__':
    app.run()

# 웹브라우저에 http://127.0.0.1:5000/naver
# 위와같이 접속 하면 안녕 나는 네이버야~
# 라는 글자가 나타나게 하기

# id == a
# pw == 123
# 로그인 했을때 맞으면 성공 , 틀리면 실패 만들어보기