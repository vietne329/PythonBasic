#Vòng lặp for: 

name = "Mai Dac Viet"
for i in name :
    print(i)


for i in range(0,10) :
    for j in range (i,10) :
        print( j , end = " ")
    print("")


#Lòng lặp while:
# Vòng lặp while trong Python dùng để lặp các dữ liệu mà giá trị ngừng có của nó là chưa biết trước

#VD: Mình sẽ viết một vòng lặp while in ra dãy số từ 1 đến 10.
i = 1
while(i <= 10):
    print(i, end = " ")
    i += 1

#Đối với vòng lặp while này thì chúng ta cũng có thể lồng nó lại với nhau được.
i = 1 
while(i <= 10) :
    j = 1
    while(j <= 10 - i):
        print(j, end = " ")
        j += 1
    print("")
    i += 1
