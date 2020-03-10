#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_process.py
#  
#  Copyright 2020 comp <semion@comp>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
"""
Здесь стоит помнить, что цикл будет работать до тех пор пока вызываемое приложение 
не отошлет в канал символ конца файла EOF, сигнализируя о завершении работы.


Если вызываемая программа работает в бесконечном цикле или ожидает ввода данных 
от пользователя или просто долго не завершает свою работу (не посылает EOF)
то любой метод чтения перейдет в режим ожидания данных от вызываемой программы и 
«повесит» основную программу
"""

#documentation
#https://docs.python.org/3/library/multiprocessing.html
#https://codecamp.ru/documentation/python/1393/subprocess-library

#EOF - end of file - индикатор ос, означающий, что данные в источнике закончились.

import os
import multiprocessing as mp
import time


##какие методы есть в модуле multiprocessing
## модуль multiprocessing представляет различные механизмы для взаимодейсввия процессов - 
## - механизмы взаимодействия IPC - Queue, Pipe
## - механизмы взаимодействия через разделяемую процессами память Value,Array
## - специфичные механизмы, такие как Manager и Pool - пул потоков

## Класс Process очень похож на класс Thread модуля threading. 
## Данный класс находится в модуле multiprocessing
## Два основных метода - это start(), join() 
## At first, we need to write a function, that will be run by the process. Then, we need to instantiate a process object.



##
##	ещё есть - 
##			thread - не возможно использовать так как gil 
##		    threading - аналагично thread
## 			subprocess(в переводе - подпроцесс) - свовсем другой модуль 
## 			multiprocessing - multiprocessing работает с процессами
## 			multiprocessing.dummy использует треды (со всеми присущими им ограничениями)

## Класс Pool
## Используется для показа пула рабочих процессов 

## popen.poll() - если процесс завершил работу - вернёт код возврата, в ином случае None
##

## Связь между процессами - модули нашего multiprocessing включают в себя два главных метода: Queue и Pipe. 

## !!!
## map - map(function, [1,2,3,4])
## Применяет указанную функцию к каждому элементу указанной последовательности/последовательностей.
## !!!

# for connection 
def creator(data, queue):
	print("WORKING CREATOR,DATA IN START", data, "||" ,"time = ", time.ctime())
	tmp = data * 20 
	queue.put(tmp)
	print("WORKING CREATOR,DATA IN END", tmp)

	
def consumer(queue):
	data = queue.get()
	print("WORKING CREATOR,DATA EQUALS", data, "||" ,"time = ", time.ctime())




def foo():
	print("\n\nSTART WORKING")	
	print("this functions simple working, her pid = ", os.getpid(), "||" ,"time = ", time.ctime())
	print("this functions simple working, her parent ppid = ", os.getppid(), "||" ,"time = ", time.ctime())
	
	"""
	## !!!
	l = [i for i in range(1000000000)] # при данной штукенции зависает комп, на время создания списка в отдельном процессе или что-то типо того
									   # и ещё процессы запускаются не в одно время. И какая речь о параллельных вычислениях 
									   
	l = [i for i in range(100000000)] # до ста миллионов работает все нормально, после ста задержка между созданием процессов в 6 секунд
	## !!!
	"""
	
	l = [i for i in range(10000000)] # 

	"""
	for i in range(len(l)): 
		l[i] += 1
		print(l[i])
	"""
	
	print("END WORKING")
		
	#класс Process дает возможность вам получить доступ к названию вашего процесса. Давайте посмотрим:
	print("NAME GENERATED PROCESS")
	proc_name = mp.current_process().name
	print("process name = ", proc_name)
	
	print("this functions simple working, her pid = ", os.getpid())

def main(args):
	
	print("NAME BASIC PROCESS")
	proc_name = mp.current_process().name
	print("process name = ", proc_name)
	
	pid = os.getpid()
	print("pid = ", pid)
	
	#number core in your pc 
	#not number core, number threads in your pc 
	cpu_count = mp.cpu_count()
	print("cpu_count = ", cpu_count)
	
	nproc = mp.Process(target = foo)
	nproc.start()
	nproc.join()
	
	nproc_2 = mp.Process(target = foo)
	nproc_2.start()
	nproc_2.join()
	
	#********///\\\********
	print("********///\\\********")
	queue = mp.Queue() ## принадлежит модулю mp
	creator_proc = mp.Process(target= creator, args = (3, queue))
	consumer_proc = mp.Process(target=consumer, args = (queue,))
	creator_proc.start()
	consumer_proc.start()
	
	"""
	print("TAKE DATA FOR QUEUE IN MAIN PROCESS")
	print(queue.get()) ## we can get data for queue in parent process
	"""
	
   

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
