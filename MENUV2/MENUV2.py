import random
ludi=[]
rost=[]
def menu():
	print("1 - Добавить человека и его рост в список \n2 - Удалить человека из списка")
	print("3 - Найти самых высоких или низких")
	print("4 - Найти средний рост первых N людей")
	print("5 - показать список людей и их рост")

def inimesed():
	ludi.append(input("Введите имя человека "))
	rost.append(random.randint(160,220))

for i in range(int(input("Сколько людей хотите? "))):
	inimesed()

def delete():
	nam = input("Введите имя кого хотите удалить")
	i = 0
	while nam in inimesed:
		i = ludi.index(nam)
		ludi.remove(nam)
		rost.pop(i)

def average():
	n = int(input("Введите N первых людей"))
	i = 0
	summa = 0
	while i < n:
		summa += rost[i]
		i += 1
	sredny = summa / n
	return sredny
def add():
	n = input()
	r = int(input())
	ludi.append(n)
	rost.append(r)
def remove():
	n = input()
	i = ludi.index(n)
	ludi.remove(n)
	rost.pop(i)
def find(max):
	rost_m = rost[0]
	if max:
		rost_max = []
		ludi_max = []
		rost_copy = rost.copy()
		for a in rost:
			if a > rost_m:
				rost_m = a
		for a in rost:
			try:
				i = rost_copy.index(rost_m)
				rost_copy.pop(i)
				ludi_max.append(ludi[i])
			except:
				break
		return rost_m, ludi_max		
	else:
		rost_max = []
		ludi_max = []
		rost_copy = rost.copy()
		for a in rost:
			if a < rost_m:
				rost_m = a
		for a in rost:
			try:
				i = rost_copy.index(rost_m)
				rost_copy.pop(i)
				ludi_max.append(ludi[i])
			except:
				break
		return rost_m, ludi_max
		
while True:
	menu()
	a = input()
	if a == "1":
		add()
	elif a == "2":
		remove()
	elif a == "3":
		print(find(input("max? min? ") == "max"))
		print("Список людей и их рост")
	elif a == "4":
		print(average())
		print("Средний рост")
	elif a == "5":
		print(ludi)
		print(rost)
