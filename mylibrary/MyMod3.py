class Calc:
    def plus(self,x,y):
        return x+y
    
    def minus(self,x,y):
        return x-y
    
my_calc=Calc()              # 객체 반드시 지정하고 함수 사용해야함!!!

if __name__=="__main__":
    print(my_calc.plus(10,20),my_calc.minus(10,20))