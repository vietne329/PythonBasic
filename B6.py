'''
                                Bài 6: List trong Python
1, List là gì? và khai báo list trong Python.
- List trong Python là một dạng dữ liệu cho phép lưu trữ nhiều kiểu dữ liệu khác nhau trong nó,
   và chũng ta có thể truy xuất đến các phần tử bên trong nó thông qua vị trí của phần tử đó trong list.
- Ở đây, nếu như bạn nào đã tìm hiểu qua một ngôn ngữ nào đó thì có thể coi list trong Python như một mảng tuần tự trong các ngôn ngữ khác.

Để khai báo một list trong Python thì chúng ta sử dụng cặp dấu [] và bên trong là các giá trị của list.
    [value1, value2,..., valueN]

example: name = ["Viet","Nam","Dao","Dat","Dung","Khanh"]

2, Truy cập đến các giá trị trong list.
    - Để truy cập đến các phần tử trong list thì các bạn làm tương tự như đối với chuỗi.
    - Các phần tử trong một list được đánh dấu bắt đầu từ 0 theo chiều từ trái sang phải 
        và từ -1 theo chiều từ phải qua trái.
- Trong trường hợp bạn muốn in ra một phần của list thì bạn sử dụng cú pháp sau:
                    list[start:end]

3, Sửa đổi và xóa bỏ giá trị phần tử trong list.
- Sau khi bạn đã truy cập được đến các phần tử trong list rồi thì bạn có thể xử lý nó như nào tùy thích theo 
    ý của bạn (sửa - xóa).
- Update :
    + Để sửa giá trị của các phần tử trong list thì các bạn chỉ cần truy cập đến phần tử mà mình cần sửa đổi 
    và tiến hành gán giá trị mới cho nó.
-Delete:
    + Để xóa một hoặc nhiều phần tử trong list thì các bạn cần truy cập đến phần tử cần xóa và dùng hàm del để xóa. 
        Và sau khi chúng ta xóa phần tử trong list thì index của list sẽ được cập nhật lại.

4, List lồng nhau.
    -Do list có thể chứa nhiều kiểu dữ liệu khác nhau lên chúng ta hoàn toàn có thể khai báo một list chứa một hoặc nhiều list khác nhau.
    -Và cứ như thế chúng ta có thể lồng N list khác vào trong list.
    - Đối với list lồng nhau như này thì chúng ta chũng truy xuất đến các phần tử như bình thường, theo cấp từ ngoài vào trong.

'''
name = ["Viet","Nam","Dao","Dat","Dung","Khanh"]
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

name[4] = "Khanhhh"  # update tên thằng Khánh
print(name[4])


name = ["Viet","Nam","Dao","Dat","Dung","Khanh"]
del name[3] #bay màu tk Đạt
for i in name :
    print(i)

#List lồng nhau: 
myNumber = [1,2,3,4,5]
myName = ["Viet","Nam","Dao","Dat","Dung","Khanh",myNumber]

print(myName)

#VD: Mình sẽ truy cập vào phần tử dầu tiên trong list myNumber.
myNumber = [1,2,3,4,5]
myName = ["Viet","Nam","Dao","Dat","Dung","Khanh",myNumber]

myName[6][0]




