"""
Модуль subprocess дает разработчику возможность запускать процессы из программ Python.
Другими словами можно запускать приложения и передавать им аргументы при помощи модуля subprocess
Был внедрен в Python для замены модуля os, таких как os.popen, os.spawn, os.system

Функция вызова 
Класс Popen 
Как связываться с созданным процессом


Функция call позваоляет вам вызвать другую программу, дожидаться завершения команды и вернуть код возврата
Она принимает несколько аргументов 

Класс Popen Python выполняет дочернюю программу в новом процессе. 
В отличие от метода call, он не дожидается конца выполнения вызванного процесса, если вы не укажете это в методе wait.

Запустить дочерний процесс, он будет выводить в stdout в консоль, 
но так как мы не можем подступится к содержимому,
будем посылать сигнал и приостанавливать выполнение дочерниго процесса ....


"""
import subprocess
import os
import time

def main(args):
	
	print(os.getpid())
	"""
	#надо захватить вывод с помощью capture_output
	p1 = subprocess.Popen(["ls", "-l"], capture_output = True, text = True)
	
	print("\n*****************\n")
	
	time.sleep(10)
	p1.terminate()
	#print(p1.stdout.decode()) # можно не использовать decode, можно добавить ...
	## ... аргумент в функцию text = True
	print(p1.stdout)
	"""
	#i с diagsalvom vse rabotaet
	#p2 = subprocess.Popen("./diagslave", stdout=subprocess.PIPE, shell=True)
	
	p2 = subprocess.Popen("ping www.yandex.ru", stdout=subprocess.PIPE, shell=True)

	
	print(os.getpid())
	print(os.getppid()) 
	# нормально все 
	print("\n*****************\n")
	while p2.poll() is None:
		print(p2.stdout.readline())


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
