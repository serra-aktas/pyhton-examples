#SORU4

#Verilen sözlük yapısına aşağıdaki adımları uygulayınız

dict = {'Christian' : ["America",18],
        'Daisy' : ["England",12],
        'Antonio' : ["Spain",22],
        'Dante' : ["Italy",25],}

#Adım 1: Key değerlerine erişiniz.

my_dict = dict 
print(my_dict.keys())


#Adım 2: Value'lara erişiniz.

print(dict.values())

#Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

my_dict = dict
my_dict['Daisy'][1] = 13
print(my_dict)

#Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

my_dict = dict
my_dict['Ahmet'] = ["Turkey",24]
print(my_dict)

#Adım 5: Antonio'yu dictionary'den siliniz

my_dict = dict
del my_dict['Antonio']
print(my_dict)

