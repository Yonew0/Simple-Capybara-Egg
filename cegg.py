import time
from colorama import Fore
import random

# это типо проверяет какая капибара вам выпала
def check():
	print(f"{Fore.BLUE}Ожидаем ответа...{Fore.WHITE}")
	time.sleep(5)

	random_gent = random.randint(0, 100)

	if random_gent > 45:
		print("Вам выпала обычная капибара.")
	elif random_gent <= 45:
		print(f"{Fore.GREEN}Вам выпала редкая капибара!")
	elif random_gent <= 15:
		print(f"{Fore.PURPLE}Вам выпала эпическая капибара!")

	input(f"{Fore.WHITE}")

# а это типо создает начальный текст и запускает функцию чек
def start():
	print(f'''{Fore.RED}
		Добро пожаловать в прогамму с нормальным расчётом
		яйца капибары для видео!
		{Fore.WHITE}
		Обычная - 50 %
		Редкая - 35 %
		Эпическая - 15 %''')

	check()

# запуск функции старт
start()