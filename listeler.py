x=5
y="6"
dogru=True
liste=[x, y, dogru, "Tarık"]
liste.append("armut") #listenin sonuna eleman ekler.
liste.insert(0,"yeni") # belirtilen yere eleman ekler.
cıkarılan=liste.pop() #Sondaki elemanı siler ve kullanır değişkene atar.
cıkan=liste.pop(2) #listedeki 2. elemanı siler ve değişkene atar.
#liste.remove("5") #belirtilen elemanı siler. kullanmaz değişkene atamaz.
liste.remove(liste[1]) #2. elemanı çıkarır.

liste2=[5,4,3,2,1]
liste.append(liste2) #liste nin sonuna liste2 yi ekler. listenin son elemanı yine bir liste olur.
print(liste)
liste.extend(liste2)# iki listeyi birleştirir. elemanları tek tek ekler.
print(liste)
a=liste[3][2] #iki boyutlu liste
c=liste.index(5) #listedeki 5 elemanının indexine erişir.
print(c)

liste2.sort() #liste2 yi sıralar.

print(liste2)

liste3=[5,4,3,2,1]
liste4=sorted(liste3) #liste3ü sıralamaz liste3ün sıralanmış halini liste4e kaydeder.
print(liste3)
print(liste4)
liste2.sort(reverse=True) #liste2 yi tersten sıralar.

liste4.reverse() #listeyi tersine çevirir. sıralama değil.
a=len(liste4) #listenin uzunluğunu verir.
print(a)

liste4.count(1) #liste4 te kaç tane 1 olduğunu sayar.
print(max(liste4))
print(min(liste4))

