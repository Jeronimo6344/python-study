# 패키지 참조
from flask import Flask, render_template

# Flask 메인 객체 생성
app = Flask(__name__)

# 특정 함수를 웹 상에 URL로 노출
@app.route("/hello")
def hello():
    html="""Hello Flask~!!
    This is Flask Webpage :)"""
    return html

@app.route("/world")
def world():
    html="""<h1>안녕 플라스크~!!</h1>
    <p style='color:blue'>첫 번째 플라스크 웹 페이지</p>"""
    return html

# 미리 준비된 웹페이지 화면을 웹 브라우저에게 전달하기
@app.route('/myfood')
def myfood():
    return render_template('myfood.html')

# 딕셔너리 데이터를 웹 브라우저에게 전달함 --> JSON 구조
@app.route('/mydata')
def mydata():
    mydict={'name':'LEE','age':24,'height':175,'weight':82}
    return mydict

# Flask 웹 서버 가동
if __name__ == "__main__":
    app.run(port=9091, debug=True)

# app과 if문 사이에 "함수"를 넣자...!!! (순서 고정)