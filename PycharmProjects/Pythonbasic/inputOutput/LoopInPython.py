


a = [1, 2, 3.5]
b = ["abcd", "xy", "aăâ"]
#----------------------- Loop in Python. -----------------
#..... using "for:" .....
for x in a:
    print("Phần tử: ",x)
print("\n\nHết.")

for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], "_")


#..... using recursion(đệ quy) .....
# in ra các kí tự của b[-1]
str = b[0]
n = 0
def In_Các_Kí_tự_của_Chuỗi (str, n):
    print (str[n])
    if (n<len(str)-1):
        return In_Các_Kí_tự_của_Chuỗi(str,n+1)
    else:
        return

#..... call the recursion .....
print ('function:')
In_Các_Kí_tự_của_Chuỗi(str,0)



#..... using While() .....
print ("Begin of while.")
i = 0
array = [1, 2, 3, 7]
while ( i < 4):
    print ("the index: ", i)    
    print("Value is: ", array[i], "\n")
    i = i+1

# -----------------------------------------------------------