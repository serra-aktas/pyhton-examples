#Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

#Adım 1: Verilen listenin eleman sayısına bakınız.

lst_bir = len(lst)
print(lst_bir)

#Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.

print(lst[0],lst[10])

#Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

new_list = lst[:4]
print(new_list)

#Adım 4: Sekizinci indeksteki elemanı siliniz.

del lst[8]
print(lst)

#Adım 5: Yeni bir eleman ekleyiniz.

lst.append("high")
print(lst)

#Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(8,"N")
print(lst)
 

