#SORU7
"""
Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
almaktadır. Zip kullanarak ders bilgilerini bastırınız
"""
ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for a,b,c in zip(ders_kodu,kredi,kontenjan):
    print('Kredisi {} olan {} kodlu dersin kontenjanı {} kişidir.'.format(b,a,c) )
    


