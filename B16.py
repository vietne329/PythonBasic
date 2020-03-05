#Bài 16: Exception trong Python

def sum(a, b):
    return a / b

sum(6,2)

try:
    print(sum(6,0))
except ZeroDivisionError:
    print("Co loi xay ra")