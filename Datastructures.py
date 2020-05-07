#Assigning elements to different lists

test_list = [10, 40, 55, 67, 72, 23] 
  
print ("The original list is : " + str(test_list)) 
  

var1, var2, var3 = [test_list[i] for i in (1, 3, 5)] 

print ("The variables are : " +  str(var1) +  " " + str(var2) + " " + str(var3)) 




#Accessing elements from a tuple

tup1 = ('physics', 'chemistry', 'biology', 'social');
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0:3]: ", tup1[0:3];
print "tup2[1:5]: ", tup2[1:5];


#Deleting different Dictionary elements
test_dict = {"Harry" : 50, "Ron" : 100, "Hermoine" : 90, "Malfoy" : 80} 
print ("The dictionary before performing remove is : " + str(test_dict)) 
removed_value = test_dict.pop('Harry') 
print ("The dictionary after remove is : " + str(test_dict)) 
print ("The removed key's value is : " + str(removed_value))   
print ('\r') 
  
print ("The dictionary after remove is : " + str(test_dict))
