'''
1.Các ký tự đặc biệt trong chuỗi.
- Để sử dụng các ký tự đặc biệt trong Python khi in ra dữ liệu thì mọi người sử dụng ký tự " \ " trước nó.
- Khi bạn muốn in ra dấu "" thì phải format dưới dạng \" content \"
content: là nội dung trong dấu " ... "
example:
print(" Toi ten la \" Mai Dac Viet \"  ")
-> output: Toi ten la " Mai Dac Viet "

Các ký tự đặc biệt khác:

\n ngắt xuống dòng và bắt đầu dòng mời.
\t đẩy nội dung phía sau nó cách 1 tab.
\a chuông cảnh báo.
\b xóa bỏ khoảng trắng phía trước nó.

2.Format chuỗi:
    - Định dạng chuỗi được format như sau: 
   '{} {}'.format('one', 'two')

    Trong dấu {} được nội dung bạn muốn định dạng , nếu muốn sắp xếp theo thứ tự thì đánh dấu stt.

    -> output : one two

    ex: '{1} {0}.format('em','ơi')'

    ->  output: 'ơi em'

3, Truy cập tới từng giá trị của chuỗi.
    Để truy cập vào phần tử của chuỗi ta làm như sau: 
    string_name[index]

    index: chỉ số phần tử của chuỗi mà bạn muốn truy cập

    example: 
    str = "Hello World"
    str[3] 
    -> output: 'l'

    - Bạn có thể truy cập 1 đoạn theo cách sau: string_name[first:end]

    str[0:4]
    -> output: 'Hello'

'''