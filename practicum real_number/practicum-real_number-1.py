import math # Импортируем библиотеку для "продвинутых" вычислений

print("=== Задача A ===")
input("Нажмите Enter для начала работы программы.") # Для красоты

onePhoto = float(input("Размер одной фотографии (в мегабайтах): ")) # Принимаем значения
storageCapacity = int(input("Объём хранилища (в гигабайтах): "))

storageCapacityInMB = storageCapacity * 1024 # Переводим гигабайты в мегабайты
photosAmount = storageCapacityInMB // onePhoto # Делим переведённые гигабайты на размер одной фотографии (делим без остатка)

# Формируем ответ 
print("В хранилище объёмом " + str(storageCapacity) + " ГБ поместится " + str(math.floor(photosAmount)) + " фотографий.")
# math.floor - ПРИНУДИТЕЛЬНОЕ округление в МЕНЬШУЮ сторону
print("Создал: Стрекачев Владимир, 2021")
input("Нажмите Enter для завершения работы программы.") # Для корректной работы EXE-файла (и для красоты)