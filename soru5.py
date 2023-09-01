#SORU5

"""
Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
return eden fonksiyon yazınız

"""
l = [2,13,18,93,22]

def all_list(list):
    even_list = []
    odd_list  = []
    
    for num in list :
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
            
    return even_list,odd_list

even_list, odd_list = all_list(l)

print("çift sayılar:", even_list)
print("tek sayılar:", odd_list)



