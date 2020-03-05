#Bài 19: Xử lý số học với module math trong Python

#1,abs() : Hàm này có tác dụng trả về giá trị tuyệt đối của một số.
# Lưu ý: Hàm này không nằm trong module math, nên các bạn không cần phải import modules math.

myNumber = -10
print(abs(myNumber))

#2, fabs():Hàm này có tác dụng trả về giá trị tuyệt đối của một số va` chuyển đổi được cả complex number.
    # syntax: math.fabs(number)

import math
myNumber = -14.4

math.fabs(myNumber)

#3, ceil(): Hàm này có tác dụng chuyển đổi một số về dạng số nguyên của nó và số nguyên đó phải lớn hơn hoặc bằng số ban đầu. 
# Nói một cách đơn giản thì hàm này có tác dụng làm tròn lên 1 số.
    #syntax: math.ceil(number)

num1 = 4.3
math.ceil(num1)

#4, exp(): Hàm này có tác dụng trả về kết quả e^x, trong đó x là số mà các bạn cần tính.

num2 = 2
math.exp(2)

#5, floor(): Hàm này có tác dụng làm tròn một số về dạng số nguyên nhỏ hơn hoặc bằng số ban đầu. Nói cách khác thì là làm tròn xuống một số.
num3 = 3.8

math.floor(num3)

#6, log(): Hàm này sẽ trả về kết quả logarithm x, với x là số cần chuyển và x > 0.
num = 4

math.log(num)

#7, log10(): Hàm này tương tự như hàm log(), nhưng là dạng logarithm cơ số 10.
num4 = 100
math.log10(num4)

#8 max(): Hàm này có tác dụng trả về số lớn nhất trong các số được truyền vào. (dont need module math)

a = 10 ;b = 15; c = 9
max(a,b,c)

#9 min():Hàm này có tác dụng trả về số nhỏ nhất trong các số được truyền vào.
a = 10 ;b = 15; c = 9
min(a,b,c)

#10, modf(): Hàm này có tác dụng chuyển đổi một số về một tuple.uple này chứa phần thập phân và phần nguyên của số đó,
# lưu ý tất cả các giá trị trong tuple này đều ở dạng float. 

num5 = 5.32

math.modf(num5)

#11,pow(): Hàm này có tác dụng trả về kết quả của phép x^y, với x là tham số thứ nhất, y là tham số thứ 2.

math.pow(2,3)

#12,round(): Hàm này có tác dụng làm tròn số về dạng cần thiết.

num6 = 4.123143
round(num6,2)

#13,sqrt().Hàm này có tác dụng trả về căn bậc 2 của một số, với điều kiện số đó phải lớn hơn 0.

x = 100
math.sqrt(x)

#14,acos():Hàm này có tác dụng tính cosine của một số. Với điều kiện số đó phải nằm trong khoảng: -1<= x <=1.

x = 1
print(math.acos(x))

#15, cos(): Hàm này cũng trả về cosine của một số, nhưng số này được tính theo radian.
x = 90
math.cos(x)

#16, asin(): Hàm này có tác dụng trả về sine của một số. Với điều kiện số đó phải nằm trong khoảng: -1<= x <=1.
x = 1
print(math.asin(x))

#17,sin(): Hàm này cũng trả về sine của một số, nhưng số này được tính theo radian.
x = 1
print(math.sin(x))

#18, atan() - tan():Tương tự như với asin() - sin() và acos() - cos() ta cũng có atan() và tan() với chức năng là tính tangent của một số. 
x = 1
print(math.atan(x))

print(math.tan(x))

#19, radians():Hàm này có tác dụng chuyển đổi từ độ sang radians.
x = 1
print(math.radians(x))


