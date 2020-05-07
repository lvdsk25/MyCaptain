list1 = []  
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    list1.append(ele) 
    
print("The list is:")
print(list1)
print("The positive numbers in the list are:")
for num in list1: 
    if num>=0:
        print(num)
