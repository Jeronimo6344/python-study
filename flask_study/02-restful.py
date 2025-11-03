# 패키지 참조
from flask import Flask, request

# Flask 메인 객체 생성
app=Flask(__name__)

# GET 방식의 데이터 수신
@app.route('/parameter',methods=['GET'])
def get():
    my_num1=request.args.get('num1')
    my_num2=request.args.get('num2')

    sum1=my_num1+my_num2
    sum2=int(my_num1)+int(my_num2)

    mydict={
        'expr': "%s + %s" %(my_num1,my_num2),
        'sum1': sum1,
        'sum2': sum2
    }

    return mydict

# POST 방식의 데이터 수신
@app.route('/parameter',methods=['POST'])
def post():
    x=request.form.get('x')
    y=request.form.get('y')
    z=int(x)*int(y)
    return {
        'expr': '%s * %s' %(x,y),
        'z': z
    }

# PUT 방식의 데이터 수신
@app.route('/parameter',methods=['PUT'])
def put():
    a=request.form.get('a')
    b=request.form.get('b')
    c=int(a)-int(b)
    return {
        'expr': '%s - %s'%(a,b),
        'c': c
    }

# DELETE 방식의 데이터 수신
@app.route('/parameter',methods=['DELETE'])
def delete():
    m=request.form.get('m')
    n=request.form.get('n')
    o=int(m)/int(n)
    return {
        'expr': '%s / %s' %(m,n),
        'o': o
    }

# PATH 방식의 데이터 수신
@app.route('/parameter/<myname>/<myage>',methods=['GET'])
def path_params(myname,myage):
    msg='안녕하세요 {name}님. 당신은 {age}세 입니다.'
    return {
        'msg': msg.format(name=myname, age=myage)
    }

# 예외 발생 시 호출되는 함수 정의
@app.errorhandler(Exception)
def error_handling(error):
    return ({'message':str(error)},500)

# Flask 웹 서버 가동
if __name__=='__main__':
    app.run(port=9091,debug=True)