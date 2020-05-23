
#АЛГОРТИМ КАК РАБОТАЕТ ПРОГРАМУ
#####1 Создайте случайный начальный тур и установите начальную температуру.
# 2 Задайте число для выполняемых итераций, определяемое длиной эпохи.
#3 Случайно выберите два города в туре и выполните операцию «2-opt»
#4 Если получен тур с более коротким расстоянием, примите новый тур. В противном случае примите новый тур с определенной вероятностью, определяемой разницей между старым и новым расстояниями и текущей температурой.
#5 Повторите 3-4 для количества итераций, определенных в 2.
#6 Если условие остановки выполнено, прекратите. В противном случае перейдите к 7.
# 5Уменьшите температуру и повторите 2-5.)####


from satsp import solver

#Матрица расстояния является массивом, я, запись J расстояние от места я на место В ККМ(1000КМ), 
#где индексы массива соответствуют адресам в следующем порядке:
#0. МОСКВА - 1. УФА - 3. КАЗАНЬ - 4. ПЕРМ - 5. САМАРА

solver.Solve(city_list =None, dist_matrix = [[0,2, 3 ,8 ,13],
                                            [2, 0, 9, 10 ,11],
	                                        [3, 7, 0, 6  ,14],
                                            [4, 8, 9, 0, 17],
                                            [5, 3, 34,2,  0]], 
          #dist_matrix : матрица N * N, содержащая расстояния между N городами. 
           #city_list пропущен, программа рассчитает эклидовы расстояния между городами. 
            start_temp = None, \
      #start_temp : начальная температура для SA. Если значение не указано, 
      #программа оценит начальную температуру,
      # используя небольшую выборку из данных
     #альфа : скорость охлаждения для SA. Если Noneбудет принято,
      # программа будет вычислять альфа , если stop_temp и эпохи приведены. 
      #В противном случае альфа устанавливается на 0,99.


     #эпох : количество эпох для SA. Решающий фактор для времени работы алгоритма.
    # Программа прекратит работу после этого количества эпох. 
    # Если Noneпройдено и заданы stop_temp и alpha , программа рассчитает количество эпох.
    #  В противном случае условие остановки будет переключено на улучшение после определенного количества эпох, 
    #  где число определяется с помощью stopping_count .
   #epoch_length : количество итераций в каждой эпохе. 
    #По умолчанию установлено значение min (100, N * (N-1) / 2)
   #epoch_length_factor : скорость, с которой длина эпох увеличивается в каждой эпохе. Должно быть больше или равно 1.
  # По умолчанию 1.00. Небольшое значение рекомендуется для больших случаев


   #Другие функции , обеспечиваемые solver: solver.GetBestDist(): возвращают общее расстояние лучшего TSP тур solver.
   #GetBestTour(): возвращают список городов лучшего TSP тур solver.
   #PrintBestTour(): Выход картины рисунка лучшего TSP тур solver.
  #PrintConvergence(): Участок конвергенции расстояний в конце каждой эпохи
            stop_temp = None, alpha = None, epochs = None, epoch_length = None, \
 #epoch_length_factor : скорость, с которой длина эпох увеличивается в каждой эпохе. Должно быть больше или равно 1.
          epoch_length_factor =int(input("ввидите скорость, с которой длина эпох увеличивается в каждой эпохе: ")) ,
   #stopping_count : количество эпох, после которых программа остановится, если не будет сделано никаких улучшений.            
          stopping_count =int(input("ввидите количество эпох: ")), screen_output = True)

solver.PrintSolution()
