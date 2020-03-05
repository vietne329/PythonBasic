'''
1, Dictionary là gì?
- Kiểu dữ liệu dictionary trong Python là một kiểu dữ liệu lưu trữ các giá trị chứa key và value ,nhìn một cách tổng quát thì nó giống với Json.
 Và đối với kiểu dữ liệu này thì các giá trị bên trong nó không được sắp xếp theo một trật tự nào cả.

- Để khai báo một dictionary chúng ta sử dụng cặp dấu {} theo cú pháp sau:
person = {
    'name': 'Vũ Thanh Tài',
    'age': 22,
    'male': True,
    'status': 'single'        
    }

2, Truy cập đến các phần tử trong dictionary.
- Ở trên mình có nói là các phần tử trong dictionary được sắp xếp không theo một thứ tự nào cả, nên cũng chính vì điều đó mà chúng ta không thể
  nào sử dụng được cú pháp như đối với string và list mà chúng ta sẽ dựa vào các key của nó để truy xuất.
- Để truy cập đến các phần tử trong dictionary thì các bạn sử dụng cú pháp sau:
        dicName[key]
3, Thay đổi giá trị của dictionary.
- Để thay đổi giá trị của phần tử trong dictionary thì ta cũng là tương tự như 
   đối với list là truy cập đến phần tử cần truy cập và thay đổi giá trị của nó.
4, Xóa phần tử trong diction.
- Để xóa một phần tử trong dictionary thì chúng ta sử dụng hàm del và chọn phần tử cần xóa.
- Và nếu như bạn muốn xóa tất cả các phần tử bên trong dictionary thì bạn sử dụng phương thức clear theo cú pháp:
                    dictName.clear();
    Trong đó, dictName là dictionary mà bạn muốn xóa hết phần tử.

-Và nếu như bạn muốn xóa hẳn dictionary thì bạn dùng hàm del để xóa

5, Dictionary lồng nhau.

Cũng giống như kiểu dữ liệu list, tuple thì trong dicrtionary các bạn cũng có thể lồng bất kỳ kiểu dữ liệu nào bạn thích vào trong nó.

VD: Mình sẽ lồng một dictionary vào trong dictionary và đồng thời truy vấn luôn đến dictionary con.

person = {
    'name': 'Vũ Thanh Tài',
    'option': {
                'age': 22,
                'male': True,
                'status': 'alone'
            }        
    }

print(person['option']['age'])
# 22
'''
myProfile = {
    'name':'Mai Dac Viet',
    'age' : 21 ,
    'school' : 'PTIT',
    'grade' : 3
}
myProfile['name']
# -> Mai Dac Viet


myProfile['grade'] = 4
print(myProfile)


del myProfile['grade']
print(myProfile)

