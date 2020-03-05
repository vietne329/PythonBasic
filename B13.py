#Bài 13: Input và Đọc ghi file trong Python

'''
1, Input.
- Trong Python có cung cấp cho chúng ta hàm input để nhận dữ liệu từ người dùng nhập vào trong commandline. Sử dụng với cú pháp như sau:
            input(something)

'''

name = input("What is your name ?")
print("Name: "+name)

'''
2, Đọc ghi file.
- File là một thứ rất cần thiết trong các dự án, ví dụ như chúng ta cần phải ghi log ra một file để sau này có thể kiểm soát được....
- Và ngôn ngữ lập trình nào cũng hỗ trợ chúng ta làm việc với file.

Mở file.
Để mở file trong Python chúng ta sử dụng hàm open với cú pháp như sau:

open(filePath, mode, buffer)
    Trong đó:

- filePath là đường dẫn đến địa chỉ của file.
- mode là thông số thiết lập chế độ chúng ta mở file được cấp những quyền gì? Mặc địn mode sẽ bằng r (xem các mode ở dưới).
- buffer là thông số đệm cho file mặc định thì nó sẽ là 0.

    Các chế độ mode.

Mode	Chú thích
r	Chế độ chỉ được phép đọc.
rb	Chế độ chỉ được phép đọc nhưng cho định dạn nhị phân.
r+	Chế độ này cho phép đọc và ghi file, con trỏ nó sẽ nằm ở đầu file.
rb+	Chế độ này cho phép đọc và ghi file ở dạng nhị phân, con trỏ sẽ nằm ở đầu file.
w	Chế độ ghi file, nếu như file không tồn tại thì nó sẽ tạo mới file và ghi nội dung, còn nếu như file đã tồn tại nó sẽ ghi đè nội dung lên file cũ.
wb	Tương tự chế độ w nhưng đối với nhị phân.
w+	Mở file trong chế độ đọc và ghi. còn lại như w.
wb+	Giống chế độ w+ nhưng đối với nhị phân
a	Mở file trong chế độ ghi tiếp. Nếu file đã tồn tại rồi thì nó sẽ ghi tiếp nội dung, và nếu như file chưa tồn tại thì nó sẽ tạo một file mới và ghi nội dung vào đó.
ab	Tương tự a nhưng đối với nhị phân.
a+	Mở file trong chế độ đọc và ghi tiếp nội dung, còn lại cơ chế giống chế độ a.
ab+	Tương tự chế độ a+ nhưng đối với nhị phân.



'''

fopen = open(r"test.txt")
for i in fopen :
    print(i)
fopen.close()

'''
Đóng file.
- Để đóng một file đang được mở, thì chúng ta sử dụng phương thức close() với cú pháp như sau:

fileObject.close()
- Trong đó, fileObject là đối tượng mà chúng ta thu được khi sử dụng hàm open().

- Để đảm bảo quy chế đóng mở và giải phóng bộ nhớ cho chương trình thì các bạn phải luôn nhớ đống file khi kết thúc phiên làm việc.
'''


'''
Đọc file.
- Sau khi đã mở được file ra rồi, để đọc được file thì chúng ta sử dụng phương thức read với cú pháp:

            fileObject.read(length);
-Trong đó:

- fileObject là đối tượng mà chúng ta thu được khi sử dụng hàm open().
- length là dung lượng của dữ liệu mà chúng ta muốn đọc, nếu để trống tham số này thì nó sẽ đọc hết file hoặc nếu file lớn quá thì nó sẽ đọc đến khi giới hạn của bộ nhớ cho phép.
'''

fw =  open("test.txt","w")

fw.write("Mai Dac Viet")

fw.close()