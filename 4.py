years=int(input("Введите количество лет: "))
exp=int(input("Введите количество экспонатов: "))
kolexp=(years*365*8*60)/5
kolmin=exp*5
kolhours=kolmin/60
koldays=kolhours/8
kolyears=koldays/365
print("Количество просмотренных экспонатов за указанный период равняется: ", kolexp )
print("Количество веремени, которое понадобятся для просмотра экспонатов:","\n В минутах:",int(kolmin),"\n В часах:", int(kolhours), "\n В днях:", int(koldays),"\n В годах:", int(kolyears))