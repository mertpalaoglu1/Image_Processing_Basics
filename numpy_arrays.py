import numpy as np
mylist = [1,2,3]

type(mylist)
myarray = np.array(mylist) #Burada listenin tipini array'a çeviriyoruz.
type(myarray)

'''Birden fazla boyutlu array oluşturma '''
np.arange(start=0, stop=10, step=2,) #ikişerli 0dan 9'a giden array oluşturduk.
print(np.zeros(shape=(3,3))) #matrix float olarak oluşturur numberları 0. diye
print(np.ones((3,2))) #matrix float olarak oluşturur numberları 1. diye

'''Bazı Dizi işlemleri'''
np.random.seed(101)#randomlar için seed atadık aynı oluşsun diye
arr = np.random.randint(low=0,high=100,size=10)
print(arr)
arr2 = np.random.randint(0,100,10)
print(arr2)

print(arr.max()) #en yüksek argüman değeri nedir?
print(arr.argmax()) #hangi indexte?
print(arr.min())
print(arr.argmin()),
print(arr.mean()), #ortalama
print(arr.reshape((2,5))), #yeniden boyutlandırma arraydeki sayıya uygun olacak.


''' Indexing ve Slicing '''
matrix = np.arange(0,100).reshape(10,10)
print(matrix)
row = 2 
column = 9

print(matrix[row,column]) #tek item almak için 

print(matrix[:,1]) #1 indexli columnu komple alıp row gibi gösterdi.
print(matrix[:,1].reshape(10,1)) #böyle yaparsak column gibi gelir.

print(matrix[5,:]) #5 indexli rowu komple aldı.

print(matrix[1:4,1:4]) #1 ve 4'e kadar indexli kısmı kesip aldık 3x3 matrix yaptık. 4 dahil değil.
matrix[1:4,1:4]=0 # o aralığı 0 yaptı.
print(matrix)
mynewMatrix=matrix.copy() 