import numpy as np

result  = np.array([1,3,5,7,9])#[1 3 5 7 9]
result1 = np.arange(1,10,2)#[1 3 5 7 9]
result2 = np.zeros(10)#[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
result3 = np.ones(10)#[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
result4 = np.linspace(0,100,5)#[  0.  25.  50.  75. 100.]
result5 = np.linspace(0,5,5)#[0.   1.25 2.5  3.75 5.  ] 
result6 = np.random.randint(0,10)# 7 random number
result7 = np.random.rand(5)#[0.97171599 0.21587301 0.65713566 0.79770069 0.15782929]
result8 = np.random.randn(5)#[-0.43047002 -0.3992756  -1.15964112 -0.20703405  0.26437937] negatif sayılarda oluşturur.

print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print("*******************************")

rnd_numbers = np.random.randint(1,100,10)# [32 75 44 33 27 31 12 74  5 89] random sayı üretir 10 tane ile100 arasında
rnd_max = rnd_numbers.max()#89
rnd_min = rnd_numbers.min()#5
rnd_avarage = rnd_numbers.mean()#42.2    sayıların ortalaması
rnd_index_max = rnd_numbers.argmax()# 9  üretilen max sayının indexi
rnd_index_min = rnd_numbers.argmin()# 8   üretilen min sayının indexi
print(rnd_numbers)
print(rnd_max)
print(rnd_min)
print(rnd_avarage)
print(rnd_index_max)
print(rnd_index_min)

print("*******************************")

np_array = np.arange(50)
#[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# 48 49]
np_multi = np_array.reshape(5,10) #5satır 10 sütun
#[[ 0  1  2  3  4  5  6  7  8  9]
# [10 11 12 13 14 15 16 17 18 19]
# [20 21 22 23 24 25 26 27 28 29]
# [30 31 32 33 34 35 36 37 38 39]
# [40 41 42 43 44 45 46 47 48 49]]
print(np_array)
print(np_multi)
print(np_multi.sum(axis=1)) #[ 45 145 245 345 445] satırların toplamı
print(np_multi.sum(axis=0)) #[100 105 110 115 120 125 130 135 140 145] sütunların toplamı
