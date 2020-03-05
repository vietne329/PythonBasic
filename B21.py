#Bài 21: map, filter trong Python

#1, map(): 
'''
-Hàm map này có tác dụng duyệt qua tất cả các phần tử của một hoặc nhiều list, dictionary hoặc tương tự như thế, 
sử dụng đơn giản với cú pháp như sau:
    map(function, iterable1, iterable2 ,...)
    -Trong đó:
        + function là hàm xử lý logic qua mỗi lần lặp giá trị trong interable1, ......
        + interable1, interable2 là các list, dict ,... các bạn cần lặp.
    Hàm map sẽ trả về một map object chứa các kết quả sau khi thực thi.
'''
def multiply(x):
    return x*x

result = map(multiply,[1,2,3,4,5])
list(result)

result2 = map(lambda x : x * x , [2,4,6,8])
list(result2)


result3 = map(lambda x,y : x + y , ['2','4'],['4','7'])
list(result3)

#2, filter(): Hàm này cũng có tác dụng duyệt qua các phần tử trong list, dict,... 
# nhưng khác với map là hàm này sẽ chỉ trả về những giá trị mà điều kiện trong function chấp nhận (có nghĩa là True).

result4 = filter(lambda x : x % 2 == 0 , [1,2,3,4,5,6,7,8,9,10])
list(result4)