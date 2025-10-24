class Member:
    def __init__(self,username,email):
        print("------ 생성자가 실행되었습니다. ------")
        self.username=username
        self.email=email

    def view_info(self):
        tpl="이름: {0} / 이메일: {1}"
        print(tpl.format(self.username, self.email))

if __name__=="__main__":
    m=Member("hello", "hello@naver.com")
    m.view_info()