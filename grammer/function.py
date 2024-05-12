# 함수
# 어떤 입력 값을 받아서 결과를 만들어주는 것
# 프로그래밍에서 함수란 특정 기능을 수행하는 코드

def mysum(a1,a2,a3):
    sum=a1+a2+a3
    return sum

sum1=mysum(1,2,3)
print(sum1)
#########################
num=10

def foo():
    num=20

foo()
print(num)
########################
num=10

def foo():
    global num
    num=20

foo()
print(num)