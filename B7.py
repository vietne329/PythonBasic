'''
1, Tuple Trong Python là gì?
- Tuple trong Python là một kiểu dữ liệu dùng để lưu trữ các đối tượng không thay đổi về sau (giống như hằng số).
- Còn lại thì cách lưu trữ của nó cũng khá giống như kiểu dữ liệu list.

- Để khai báo một enum thì mọi người sử dụng cú pháp sau:
    (val1, val2,.., valn)

VD: Mình sẽ khai báo 1 Tuple chứa các ngày trong tuần.
day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')

- Nếu bạn khai báo 1 biến chứa các giá trị mà không được bao quang bởi dấu () thì Python cũng nhận định nó là một tuple 
    (nhưng mình khuyên mọi người lên sử dụng cách đầu tiên cho code được tường minh).

VD:

day = 'monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday'

- Và nếu như bạn muốn khai báo 1 tuple trống thì bạn chỉ cần khai báo như sau:
a = ();

- Còn nếu như tuple của bạn chỉ chứa duy nhất một giá trị thì bắt buộc bạn phải thêm một dấu , nữa đằng sau giá trị đó.

VD:

a = (10,)

2, Truy cập đến các phần tử trong Tuple.
- Để truy cập đến các phần tử trong Tuple thì các bạn thực hiện tương tự như đối với chuỗi và list.
- Các phần tử trong Tuple được đánh dấu từ 0 theo chiều từ trái qua phải.
- Và ngược lại từ -1 theo chiều từ phải qua trái.

VD: Mình sẽ truy cập đến các phần tử trong tuple day ở trong VD trên.

day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
day[0] # monday

day[-2] # saturday

- Và nếu như bạn muốn lấy ra một tuple con trong tuple hiện tại thì bạn có thể sử dụng cú pháp sau (giống với list và string):

tupleName[start:end]

Trong đó:
- start là vị trí bắt đầu lấy. Nếu để trống start thì nó sẽ lấy từ đầu Tuple.
- end là vị trí kết thúc. Nếu để trống end thì nó sẽ lấy đến hết Tuple.

3, Các tác vụ khác trên Tuple.

Xóa Tuple.
- Như mình đã nói ở trên thì khi một tuple đã được khai báo giá trị thì chúng ta không thể sửa đổi hay xóa các giá trị đó được mà
  chúng ta chỉ có thể xóa cả tuple đi được thôi.
- Để xóa một hay nhiều tuple thì chúng ta sử dụng hàm del .

Mình sẽ xóa Tuple day.

day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
del day

-> print(day) # Error: name 'day' is not defined

- Thêm mới phần tử.
- Thực ra đây chỉ là cách lách luật thôi, chứ một tuple đã được khai báo thì chúng ta chỉ được gọi và không được sửa đổi hay thêm mới bất cứ một cái gì cả. Nhưng chúng ta có thể tạo ra được một tuple mới từ các tuple đã có bằng biểu thức + hai tuple.

VD: Mình sẽ ghép 2 tuple day1 và day2 thành tuple day.

day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday')

day = day1 + day2

print(day)
# ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

4, Tuple lồng.
- Cũng giống như list, bạn cũng có thể khai báo các tuple lồng nhau.
VD:

day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday', day1)

# day = day1 + day2

print(day2)
# ('thursday', 'friday', 'saturday', 'sunday', ('monday', 'tuesday', 'wednesday'))

print(day2[4][0]) # monday

Và bạn có thể lồng bao nhiêu cấp cũng được. Và lồng bất cứ một kiểu dữ liệu nào cũng ok.

'''