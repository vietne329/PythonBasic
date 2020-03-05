#Bài 17: Các hàm xử lý chuỗi trong Python

#1, Capitalize() : Hàm này có tác dụng in hoa chữ cái đầu tiên của chuỗi.
string = "mai dac viet"
string2 = string.capitalize()
print(string2)

#2, Center(): Hàm này có tác dụng trả về chuỗi được hiển thị ở giữa một chuỗi.
#Chú ý: Nếu len nhỏ hơn độ dài chuỗi cần xử lý thì, hàm này sẽ trả về chuỗi ban đầu.

str = "viet"
str.center(10,'-')

#3, Count():Hàm này có tác dụng đếm xem trong chuỗi có bao nhiêu ký tự cần tìm.
str = "hom nay toi dang hoc Python"
count = str.count('o',0)
print(count)

#4.encode(): Hàm này có tác dụng encode (mã hóa) một chuỗi.
'''
    string.encode(type, mode)
    - type là kiểu encode của string. Mặc định sẽ là utf-8
    - mode là chế độ báo lỗi nếu có khi encode. Python hỗ trợ 6 dạng mode như sau:
        + strict - Chế độ nghiêm ngặt, nó sẽ hiển thị lỗi dưới UnicodeDecodeError exception. Đây là chế độ mặc định.
        + ignore - bỏ qua tất cả các lỗi nếu có.
        + replace - nó sẽ thay thế lỗi bằng dấu ?.
        + xmlcharrefreplace - chèn tham chiếu XML.
        
'''
str = "maidacviet"
encodestr = str.encode()
print(encodestr)

#5, decode(): Hàm này có tác dụng decode (giải mã) chuỗi trông Python.
string = b"maidacviet"
decodestr = string.decode()
print(decodestr)

#6, endswith(): Hàm này có tác dụng kiểm tra xem chuỗi hoặc khoảng chuỗi có được kết thúc bằng ký tự nào đó hay không. 
# Nó sẽ trả về True nếu đúng và False nếu sai.

str = "hom nay t rat la met moi"
str.endswith('i',0)

str.endswith('s',0)

#7, expandtabs(): Hàm này có tác dụng tìm kiếm thay thế \t bằng các ký tự khoảng trắng.
#string.expandtabs(len)
#Trong đó: len là số lượng khoảng trắng mà bạn muốn thay thế cho một \t. Mặc định thì len = 8.
str = "ta \tcon \tyeu \tnhau"
print(str.expandtabs(20))

#8, find(): Hàm này có tác dụng tìm kiếm một chuỗi trong một chuỗi hoặc khoảng chuỗi. 
# Nó sẽ trả về là vị trí bắt đầu của chuỗi tìm được trong chuỗi nếu tìm thấy và nếu không tìm thấy nó sẽ trả về  -1.

str = "het thuong can nho"
str.find("nho",0)

#9, index():Hàm này tương tự như hàm find() chỉ khác duy nhất là nếu như không tìm thấy thì hàm này sẽ gọi exception.
str = "yeu va yeu"
print(str.index("yeu"))
print(str.index("haha"))

#10, isalnum(): Hàm này có tác dụng kiểm tra xem một chuỗi có phải là chứa duy nhất các ký tự chữ hoặc chuỗi hay không? 
# Nó sẽ trả về True nếu chuỗi chỉ chứa các ký tự chữ hoặc số. 
# Và ngược lại nó sẽ trả về False nếu chuỗi chứa ký tự khác chuỗi và số.

str = "maidacviet"
str.isalnum()

str1 = "maidacviet.com"
str1.isalnum()

#11, isalpha(): Hàm này có tác dụng kiểm tra xem một chuỗi có phải là chứa duy nhất các ký tự chữ hay không? 
# Nó sẽ trả về True nếu chuỗi này chỉ chứa duy các ký tự chữ trong bảng chữ cái, 
# và sẽ trả về False nếu nó chứa số hoặc ký tự đặc biệt khác.

str = "noitinhyeuvatdau12"
str.isalpha()

str1 =  "noitinhyeuvatdau"
str1.isalpha()

#12, isdigit(): Hàm này có tác dụng kiểm tra xem một chuỗi có phải là chứa duy nhất các chữ số hay không? 
# Nó sẽ trả về True nếu đúng và False nếu sai.

str = "0961430764asd"
str.isdigit()

str1 = "0961430764"
str1.isdigit()

#13, islower(): Hàm này có tác dụng kiểm tra xem một chuỗi có phải là in thường hay không? Nó sẽ trả về True nếu đúng và False nếu sai.
str = "i love python"
str.islower()

str = "I lOve python"
str.islower()

str = '0iloveyou1'
str.islower()

#14, isupper():Hàm này có tác dụng kiểm tra xem một chuỗi có phải là in Hoa hay không? Nó sẽ trả về True nếu đúng và False nếu sai.
str = "VIETNAMYEUTHUONG"
str.isupper()

str = "VIETNAMYEUTHUONg"
str.isupper()

#15, isnumeric(): Hàm này có tác dụng kiểm tra xem một chuỗi có phải chỉ chứa duy nhất các ký tự số hay không?
#  Nó sẽ trả về True nếu đúng và False nếu sai.

str = '0129312412'
str.isnumeric()

str = '0129312412asd'
str.isnumeric()

#16.isspace():Hàm này có tác dụng kiểm tra xem một chuỗi có phải chỉ chứa duy nhất các ký tự khoảng trắng không? 
# Nó sẽ trả về True nếu đúng và False nếu sai.

str = "   "
str.isspace()

str = "  as "
str.isspace()

#17, istitle():Hàm này có tác dụng kiểm tra xem một chuỗi có phải là title hay không, chuỗi title là chuỗi có các chữ cái đầu đều được in hoa. 
# Nó sẽ trả về True nếu đúng và ngược lại False nếu sai.

str = "Hello"
str.istitle()

str = "hello"
str.istitle()

#18, join(): Hàm này có tác dụng join squence bởi string.
str1 = '*'
str2 = 'VIET'

str1.join(str2)

str1 = '-'
str2 = 'VIET'

str1.join(str2)

#19, len():Hàm này có tác dụng trả về độ dài của chuỗi.

str ="mai dac viet"
len(str)

#20, ljust(): 
str = "viet"
str.ljust(10,'-')

#21, rjust(): 
str = "viet"
str.rjust(10,'-')

#22,lower().
str = "MAIDACVIET"
str.lower()

#23, upper().

str = "mai Dac viet"
str.upper()

#24, lstrip(): Hàm này có tác dụng loại bỏ đi các ký tự char ở phía đầu của chuỗi.

str = "  obama"

print(str.lstrip())

str = "----viet"

print(str.lstrip("-"))

#25,rstrip().
str = "obama     "

print(str.rstrip())

str = "viet----"

print(str.rstrip("-"))

#26,strip().
str = "   obama     "

print(str.strip())

str = "----viet----"

print(str.strip("-"))

#27,rfind(): Tương tự như hàm find(), nhưng hàm này nó sẽ trả về index của chuỗi cuối cùng tìm được trong chuỗi. 
# Cú pháp sử dụng tương tự hàm find().

str = 'viet va viet'
str.rfind('viet')

#28,rindex(): Tương tự như hàm index(),nhưng hàm này nó sẽ trả về index của chuỗi cuối cùng tìm được trong chuỗi. 
# Cú pháp sử dụng tương tự hàm index().

str = 'hello and goodbye'
str.rindex('o')

#29,replace():Hàm này có tác dụng tìm kiếm và thay thế chuỗi tìm được bằng chuỗi mới.

str = 'mai tat dat'
str.replace('dat','viet')

#30, max(): Hàm này trả về chữ cái có độ sắp xếp cuối cùng theo bảng chữ cái alphabet nằm trong chuỗi.

str = 'dcba'
max(str)

#31, min(): Hàm này trả về chữ cái có độ sắp xếp đầu tiên theo bảng chữ cái alphabet nằm trong chuỗi.

str = 'sdmoasd'
min(str)

#32, title():Hàm này có tác dụng chuyển đổi chuỗi sang kiểu title (xem ở trên).

str = 'sun flower'
str.title()

#33, swapcase(): Hàm này có tác dụng chuyển đổi chuỗi sang dạng nghịch đảo của nó (nghịch đảo ở đây là hoa - thường).

str = "mai DAC viet"
str.swapcase()

#34,zfill(): Hàm này có tác dụng như hàm ljust() , nhưng nó sẽ chỉ thêm được các ký tự zero (số 0) và trước chuỗi thôi.

str = "hello"
str.zfill(10)

#35, isdecimal(): Hàm này có tác dụng gần như hàm isdigit(), 
# nó sẽ trả về True nếu chuỗi cần kiểm tra chỉ chứa các số thập phân, và ngược lại....

str = 'abc123'
str.isdecimal()

str = '123'
str.isdecimal()

#36,split(): Hàm này có tác dụng tác chuỗi thành mảng bởi các char.
'''
        string.split(char, max)
        char là ký tự các bạn tìm và tách chuỗi bởi nó. Mặc định thì char = khoảng trắng.
        max là số lượng chuỗi tách tối đa.
'''
str = 'mai dac viet'
print(str.split())

print(str.split("a"))

print(str.split("a",1))

#37,splitlines():Hàm này sẽ tách chuỗi bởi các ký tự \n.
str = "hom\nnay\ntroi\nrat\ndep"
print(str)

str.splitlines()

#38, startswith(): Hàm này có tác dụng kiểm tra xem chuỗi hoặc khoảng chuỗi có được bắt đầu bằng ký tự nào đó hay không. 
# Nó sẽ trả về True nếu đúng và False nếu sai.

str = 'helloworld'
str.startswith('h')

str.startswith('h',1,len(str))

#39, maketrans(): Hàm này có tác dụng tạo ra các translation cho chuỗi. Dùng kết hợp với phương thức translate().


