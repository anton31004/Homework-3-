name=input("Введите ваше имя: ")
surname=input("Введите ваше фамилию: ")
birthday=input("Введите ваше год рождения: ")
print(name+"_"+surname+"_"+birthday)
birthday=int(birthday)
birthday=birthday+60
birthday=str(birthday)
name, surname=surname, name
print(name+"_"+surname+"_"+birthday)
