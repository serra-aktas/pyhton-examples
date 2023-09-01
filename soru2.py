#SORU2
#Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, 
#kelime kelime ayırınız

text = "The goal is to turn data into information, and information into insight"

#beklenen çıktı
# ['THE','GOAL','IS','TO','TURN','DATA','INTO','INFORMATION','AND','INFORMATION','INTO','INSIGHT']


uppercase_text = text.upper()

new_text = uppercase_text.replace(',','').replace('.','')

final_text = new_text.split()

print(final_text)