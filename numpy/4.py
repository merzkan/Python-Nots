import numpy as np

number1 = np.random.randint(10,100,6)
number2 = np.random.randint(10,100,6)

print(number1) #[73 92 46 29 27 83]
print(number2) #[28 34 65 43 86 10]

result = number1 + number2
result1 = number1 + 10

print(result) #[101 126 111  72 113  93]
print(result1) #[ 83 102  56  39  37  93]

print("*******************************")

num1 = np.random.randint(10,100,6)
num2 = np.random.randint(10,100,6)

mnum1 = num1.reshape(2,3) #2 satır 3 sütun
mnum2 = num2.reshape(2,3)

result3 = np.vstack((mnum1,mnum2)) #v vertical dikey
result4 = np.hstack((mnum1,mnum2)) #h horizontal yatay


print(mnum1)
#[[14 93 85]
# [87 14 50]]
print(mnum2)
#[[72 38 20]
# [78 63 42]]
print(result3)
#[[14 93 85]
# [87 14 50]
# [72 38 20]
# [78 63 42]]
print(result4)
#[[14 93 85 72 38 20]
# [87 14 50 78 63 42]]


print("*******************************")


numt1 = np.random.randint(10,100,6)
print(numt1) #[34 91 64 80 31 93]
result5 = numt1 >= 50
result6 = numt1 %2 == 0

print(result5)#[False  True  True  True False  True]
print(result6)#[ True False  True  True False False]
print(numt1[result5])#[91 64 80 93]
print(numt1[result6])#[34 64 80]
