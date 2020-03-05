
#Bài 12: Hàm trong Python

def hello():
    print("Hello World")

hello()

def sum(a,b):
    return a + b

r = sum(1,2)
print(r)

def sum2(*num):
    result = 0
    for i in num :
        result = result + i
    return result
    
print(sum2(1,2,3,4,5))