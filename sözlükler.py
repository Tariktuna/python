sozluk={'one':'bir','two':[2,10,3,1]}

a=sozluk.get('two') #two nun karşılığına ulaşır.
print(a)

b=sozluk.get('bir')
print(b)

sozluk['one']=1 #one ı 1 olarak değiştirir.

sozluk.update({'two':2}) #two elemanını 2 yapar.

sozluk.update({'three':3}) #three elemanını ekler.
print(sozluk)
del sozluk['one'] #one ı siler. tavsiye edilmeyen metod.
sozluk.pop('two') #two yu siler. değer döndürür. tavsiye edilen metod.
sozluk.update({'four':4})
print(sozluk)
c=sozluk.items() #keys values döndürür.
d=sozluk.keys() #keysleri döndürür.
e=sozluk.values() #valuesleri döndürür.
print(c)
print(d)
print(e)
