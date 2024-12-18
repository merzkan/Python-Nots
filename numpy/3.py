import numpy as np

number = np.array([[0,5,10],[15,20,25],[50,75,85]])

result = number[0] #[ 0  5 10]
result1 = number[2] #[50 75 85]
result2 = number[0,2] #10
result3 = number[1,2] #25
result4 = number[:]
#[[ 0  5 10] 
# [15 20 25] 
# [50 75 85]]
result5 = number[:,2] #[10 25 85]
result6 = number[:,0:2] 
#[[ 0  5]    
# [15 20]    
# [50 75]] 
result7 = number[-1] #[50 75 85]
result8 = number[-1,:] #[50 75 85]
result9 = number[:2,:2]
#[[ 0  5]
# [15 20]]

print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)

print("*******************************")

arr1 = np.arange(0,10)
arr2 = arr1 #referance
arr2[0] = 20
print(arr1)#[20  1  2  3  4  5  6  7  8  9]
print(arr2)#[20  1  2  3  4  5  6  7  8  9]

print("*******************************")

arc1 = np.arange(0,10)#[0 1 2 3 4 5 6 7 8 9]
arc2 = arc1.copy()#[20  1  2  3  4  5  6  7  8  9]
arc2[0] = 20
print(arc1)#[0 1 2 3 4 5 6 7 8 9]
print(arc2)#[20  1  2  3  4  5  6  7  8  9]