#SORU6
"""
Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
bulunmaktadır. 
Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de 
tıp fakültesi öğrenci sırasına aittir. 
Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız
"""

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
for index,ogrenci in enumerate(ogrenciler):
    if index<3:
        index += 1
        print("Mühendislik Fakültesi",index,". öğrenci: ",ogrenci)
    else:
        index -= 2
        print("Tıp Fakültesi",index,". öğrenci: ",ogrenci) 
   
    


      
     
    
    