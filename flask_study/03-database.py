# 패키지 참조
from flask import Flask, request
from sqlalchemy import text
import datetime as dt
from mylibrary import MyDB

# Flask 메인 객체 생성
app=Flask(__name__)
app.json.sort_keys=False        # 출력 결과의 JSON 정렬 방지

# GET - 다중행 데이터 조회하기
@app.route('/departments',methods=['GET'])
def get_list():
    sql=text('SELECT id, dname, loc, phone, email FROM departments')
    conn=MyDB.connect()
    result=conn.execute(sql)
    MyDB.disconnect()
    resultset=result.mappings().all()
    for i in range(0,len(resultset)):
        resultset[i]=dict(resultset[i])
    return {
        'result':resultset,
        'timestamp':dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

# GET - 단일행 데이터 조회하기
@app.route('/departments/<id>',methods=['GET'])
def get_item(id):
    sql=text("""SELECT id, dname, loc, phone, email, established, homepage
             FROM departments WHERE id=:id""")
    conn=MyDB.connect()
    result=conn.execute(sql,{'id':id})
    MyDB.disconnect()
    resultset=result.mappings().all()
    return {
        'result':dict(resultset[0]),
        'timestamp':dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }


# 전역 예외 처리
@app.errorhandler(Exception)
def error_handling(error):
    MyDB.disconnect()
    return {
        'message':''.join(error.args),
        'timestamp':dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }, 500

# POST - 데이터 저장하기
@app.route('/departments',methods=['POST'])
def post():
    conn=MyDB.connect()

    # 데이터 저장
    dname=request.form.get('dname')
    loc=request.form.get('loc')
    phone=request.form.get('phone')
    email=request.form.get('email')
    established=request.form.get('established')
    homepage=request.form.get('homepage')
    sql=text('INSERT INTO departments (dname, loc, phone, email, established, homepage) VALUES (:dname, :loc, :phone, :email, :established, :homepage)')
    params={
        'dname':dname, 'loc':loc, 'phone':phone, 'email':email, 'established':established, 'homepage':homepage
    }
    conn.execute(sql,params)
    conn.commit()

    # 데이터 저장 결과 조회
    pk_result=conn.execute(text('SELECT LAST_INSERT_ID()'))
    pk=pk_result.scalar()
    sql=text('SELECT id, dname, loc, phone, email, established, homepage FROM departments WHERE id=:id')
    result=conn.execute(sql,{'id':pk})
    resultset=result.mappings().all()

    MyDB.disconnect()

    return {
        'result':dict(resultset[0]),
        'timestamp':dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

# PUT - 데이터 수정하기  -> where절에 사용할 PK값을 PATH 파라미터로 정의
@app.route('/departments/<id>',methods=['PUT'])
def put(id):
    conn=MyDB.connect()

    # 데이터 수정
    dname=request.form.get('dname')
    loc=request.form.get('loc')
    phone=request.form.get('phone')
    email=request.form.get('email')
    established=request.form.get('established')
    homepage=request.form.get('homepage')
    sql=text('UPDATE departments SET dname=:dname, loc=:loc, phone=:phone, email=:email, established=:established, homepage=:homepage WHERE id=:id')
    params={
        'id':id, 'dname':dname, 'loc':loc, 'phone':phone, 'email':email, 'established':established, 'homepage':homepage
    }
    conn.execute(sql,params)
    conn.commit()

    # 데이터 수정 결과 조회
    pk_result=conn.execute(text('SELECT LAST_INSERT_ID()'))
    pk=pk_result.scalar()
    sql=text('SELECT id, dname, loc, phone, email, established, homepage FROM departments WHERE id=:id')
    result=conn.execute(sql,{'id':id})
    resultset=result.mappings().all()

    MyDB.disconnect()

    return {
        'result':dict(resultset[0]),
        'timestamp':dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

# DELETE - 데이터 삭제하기 -> where절에 사용할 PK값을 PATH 파라미터로 정의
@app.route('/departments/<id>',methods=['DELETE'])
def delete(id):
    conn=MyDB.connect()

    # 참조키를 고려하여 데이터 삭제구문 준비
    sql1=text('DELETE FROM enrollments WHERE subject_id IN (SELECT id FROM subjects WHERE department_id=:id) OR student_id IN (SELECT id FROM students WHERE department_id=:id)')
    sql2=text('DELETE FROM subjects WHERE department_id=:id')
    sql3=text('DELETE FROM students WHERE department_id=:id')
    sql4=text('DELETE FROM professors WHERE department_id=:id')
    sql5=text('DELETE FROM departments WHERE id=:id')

    params={'id':id}

    conn.execute(sql1,params)
    conn.execute(sql2,params)
    conn.execute(sql3,params)
    conn.execute(sql4,params)
    conn.execute(sql5,params)

    conn.commit()
    MyDB.disconnect()

    return {
        'timestamp':dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

# Flask 웹 서버 가동
if __name__=='__main__':
    app.run(host='127.0.0.1',port=9091,debug=True)