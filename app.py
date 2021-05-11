from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/a')
def hello():
    return 'Hello, World!aaaaa'

@app.route('/b')
def hello2():
    return 'Hello, World!bbbbb'

@app.route('/naver')
def hello3():
    return '안녕 나는 네이버야~'

@app.route('/duck')
def duck():
    return '''
            <!DOCTYPE html>
                <html>
                <body>

                <h2>최예나</h2>
                <img src="https://newsimg.hankookilbo.com/cms/articlerelease/2021/02/07/76990007-7d18-4c56-8f89-e082ad68dd35.jpg" alt="Trulli" width="500" height="333">

                </body>
                </html>
            '''



if __name__ == '__main__':
    app.run()
# 웹브라우저에 http://127.0.0.1:5000/naver
# 위와같이 접속 하면 안녕 나는 네이버야~
# 라는 글자가 나타나게 하기