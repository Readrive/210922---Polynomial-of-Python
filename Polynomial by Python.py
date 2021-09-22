class Polynomial:
    def __init__(self):
        self.coef= [] #계수를 리스트 안에 넣음
        

    def degree(self) :
        return len(self.coef) - 1 #계수의 list 길이를 반환
    

    def display(self, msg="f(x) = "):
        print(" ", msg, end='')
        deg = self.degree() #입력받은 계수의 개수를 deg 변수에 넣음

        for n in range(deg, 0, -1) : # [0차수, 1차수, 2차수, ..., n차수]
            print("%5.1f x^%d  + " % (self.coef[n], n), end='') #첫번째 소수점까지 나타내라
        print("%4.1f" % self.coef[0]) #첫번쨰 소수점 + 소수점 포함 4자리까지
            

    def add(self, b):
       p = Polynomial() 
       if self.degree() > b.degree() : #a의 계수의 수 > b의 계수의 수
           p.coef = list(self.coef) #p라는 새로운 계수에 a의 계수를 넣음
           for i in range(b.degree()+1) : #b의 계수 + 1 (list는 0부터 시작하니까)
               p.coef[i] += b.coef[i] 

       else : #a의 계수의 수 < b의 계수의 수
           p.coef = list(b.coef) #p라는 새로운 계수의 b의 계수를 넣음
           for i in range(self.degree()+1) : #a의 계수 + 1(list는 0부터 시작하니까)
               p.coef[i] += self.coef[i]
       return p #a와 b의 계수의 합이 넣어진 p를 반환


    def minus(self, b):
        p = Polynomial()
        if self.degree() > b.degree(): #a의 계수의 수 > b의 계수의 수
            p.coef = list(self.coef) 
            for i in range(b.degree()+1):
                p.coef[i] -= b.coef[i]

        elif self.degree() < b.degree(): #a의 계수의 수 < b의 계수의 수
            p.coef = list(b.coef) 
            for i in range(self.degree()+1):
                p.coef[i] -= self.coef[i]

        else: #a의 계수의 수 == b의 계수의 수
            if self.coef[-1] > b.coef[-1]:
                p.coef = list(self.coef)
                for i in range(b.degree() +1):
                    p.coef[i] -= b.coef[i]
            else:
                p.coef = list(b.coef)
                for i in range(self.degree()+1):
                    p.coef[i] -= self.coef[i]
        return p
                    

    def mul(self, b):
        p = Polynomial()
        if self.degree() > b.degree():
            p.coef = list(self.coef)
            for i in range(b.degree()+1):
                p.coef[i] *= b.coef[i]
        else:
            p.coef = list(b.coef)
            for i in range(self.degree()+1):
                p.coef[i] *= self.coef[i]
        return p


    def eval(self, b):
        #global sum
        sum = 0
        p = Polynomial()
        x = 2
        for i in range(self.degree(), -1, -1):
            re = self.coef[i] * x ** i
            sum += re
        return sum


def read_poly():
        instr = input("최고차항부터 차수를 순서대로 입력하시오: ")
        strlist = instr.split() #strlist라는 변수에 instr 자린 값을 넣음
        p = Polynomial()
        for coef in strlist : #coef = 계수
            val = float(coef) #계수를 float화한 걸 val에 넣음
            p.coef.insert(0, val) #처음부터 넣음
        return p


a = read_poly()
b = read_poly()

print("\n")
a.display("a(x) = ")
b.display("b(x) = ")

print("\n")
c = b.add(a) #다항식c = 다항식a + 다항식b
c.display("덧셈(x) = ") #다항식c를 display해서 출력
                     #계수값을 하나씩 받아서...
print("  덧셈(2) =  ", c.eval(b)) #다항식c에 2를 대입했을 때 나오는 값을 출력

print("\n")
d = b.minus(a)
d.display("뺄셈(x) = ")
print("  뺄셈(2) =  ", d.eval(b))

print("\n")
e = b.mul(a)
e.display("곱셈(x) = ")
print("  곱셈(2) =  ", e.eval(b))