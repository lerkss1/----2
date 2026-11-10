import random
import time

while True:
    try:
        n = int(input("Введите количество примеров: "))
        break
    except ValueError:
        print("Ошибка: необходимо ввести целое число.")
correct_count = 0
total_time = 0.0

for i in range(1, n + 1):
    print(f"Вопрос {i}/{n}")
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_answer = a * b

start_time = time.time()

while True:
    try:
        user_answer = int(input(f"{a} x {b} = "))
        break  
    except ValueError:
        print("Пожалуйста, введите целое число!")
        

end_time = time.time()
time_spent = end_time - start_time
total_time += time_spent

if user_answer == correct_answer:
    correct_count += 1
    print(f"Верно! (Время: {time_spent:.1f} сек)")
else:
    print(f"Неверно! Правильно: {correct_answer} (Время: {time_spent:.1f} сек)")  
    print ("=======================================")
    print ( "СТАТИСТИКА: " )
    print ("========================================")
    print(f"Щбщее время:{total_time:.1f}секунд")
if n> 0:
    avg_time = total_time / n
    percent_correct = (correct_count /
n) * 100
    print (f"Среднее время на вопрос:{avg_time: 1f} cek")
    print (f"Правильных ответов:{correct_count}/{n}")
    print (f"Процент правильных:{percent_correct:.1f}%")
else:
    print ("ВЫ не решили ни одного примера.")