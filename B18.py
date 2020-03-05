#Bài 18: Các hàm xử lý list trong Python

#1, list() : Hàm này có tác dụng chuyển đổi kiểu dữ liệu của một biến sang dạng list.

str = "Mai Dac Viet"
list(str)

tup = ('A','B',1,2,'C')
list(tup)

#2,len() : Hàm này trả về số lượng phần tử có trong list.

myList = [1,'Valentie',2,'C']

len(myList)

#3, max(): Hàm này sẽ trả về phần tử có giá trị lớn nhất trong list. Nếu là chuỗi thì nó sẽ trả về phần tử có độ dài chuỗi dài nhất, nếu là số thì nó sẽ trả về phần tử có số lớn nhất.

myList = ['3','Valentie','1','C']

max(myList)

#4 min(): Hàm này sẽ trả về phần tử có giá trị nhỏ nhất trong list. Nếu là chuỗi thì nó sẽ trả về phần tử có độ dài chuỗi ngắn nhất, nếu là số thì nó sẽ trả về phần tử có số nhỏ nhất.

myList = ['3','Valentie','1','C']

min(myList)

#5, append(): Phương thức này có tác dụng thêm phần vào cuối của một list.
myList = ['3','Valentie','1','C']
myList.append('Viet')
print(myList)

#6, extend(): Hàm này có tác dụng kế thừa lại các phần tử của list2 và thêm vào trong list1.

listA = ['A','B','C']
listB = ['D','E','F']

listA.extend(listB)
print(listA)


#7, count(): Phương thức này có tác dụng đếm số lần xuất hiện của một thành phần trong list!

listA = ['A','B','A','A','C']
listA.count('A')

#8, index(): ương thức này có tác dụng trả về index xuất hiện đầu tiên của phần tử mà bạn muốn tìm và nếu như không tìm thấy thì nó sẽ gọi exception.

listA = ['A','B','A','A','C']

listA.index('A')

#9,insert(): Phương thức có tác dụng thêm phần tử vào vị trí index của list, và các phần tử sau index đó sẽ được đẩy về phía sau.

listB = ['D','E','F']
listB.insert(0,'Z')

print(listB)

#10,reverse(): Phương thức này có tác dụng đảo ngược vị trí của các phần tử trong list.
listB = ['D','E','F']
listB.reverse()
print(listB)

#11. remove(): Phương thức này có tác dụng xóa phần tử khỏi list.
listB = ['D','E','F']
listB.remove('D')
print(listB)

#12.pop(): Phương thức này có tác dụng xóa bỏ phần tử trong list dựa trên index của nó.
listB = ['D','E','F']
print(listB.pop(1))
print(listB)

#13.sort(): Phương thức này có tác dụng sắp xếp lại các phần tử trong list theo một thứ tự xác định.
'''
    mylist.sort(reverse, key)
    -mylist là list mà các bạn muốn sắp xếp.
    -reverse là một boolean cấu hình kiểu sắp xếp. Nếu reverse = True thì list sẽ được sắp xếp từ lớn đến bé, 
    nếu reverse = False thì list sẽ được sắp xếp theo thứ tự từ bé đến lớn. Mặc định thì reverse = False.
    -key là callback def để xử lý list hoặc là một lamda function (thường được dùng để sắp xếp các list tuple hoặc dictionary).
'''
l = ['D','C','H']

print(l.sort())

#14, clear(): Phương thức này có tác dụng xóa bỏ hết tất cả các phần tử trong list.
l = ['D','C','H']

print(l.clear())

