from sqlalchemy import create_engine

config={
    'username':'root',
    'password':'1234',
    'hostname':'localhost',
    'port':9090,
    'database':'myschool',
    'charset':'utf8mb4'
}

conn=None

def connect():
    global conn
    con_str_tpl='mariadb+pymysql://{username}:{password}@{hostname}:{port}/{database}?charset={charset}'
    con_str=con_str_tpl.format(**config)
    engine=create_engine(con_str)
    conn=engine.connect()
    return conn

def disconnect():
    global conn
    if conn!=None:
        conn.close()

if __name__=='__main__':
    connect()
    disconnect()