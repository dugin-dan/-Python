#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
from translate import Translator
translator= Translator(from_lang="en",to_lang="ru")
new_f = open("text_4_new.txt", "w")
with open("text_4.txt", "r") as my_f:
    for line in my_f:
        str = line.split(" ")
        str[0] = translator.translate(line.split(" ")[0])        
        new_f.write(" ".join(str))
new_f.close()
with open("text_4_new.txt") as f:
    print(f.read())