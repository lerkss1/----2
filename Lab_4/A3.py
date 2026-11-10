is_valid = False
while not is_valid:
 packets = input("Введите строку из 0 и 1 (длина >= 5): ")

if len(packets) < 5:
    print("Неверный ввод. Длина строки должна быть не меньше 5.")
elif not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
else:

    is_valid = True
 

total_packets = len(packets)
lost_packets = packets.count('0')
max_streak = 0
current_streak = 0
for char in packets:
 if char == '0':
  current_streak += 1
if current_streak > max_streak:
 max_streak = current_streak
else:
 current_streak = 0
loss_percent = (lost_packets / total_packets) * 100
if loss_percent <= 1:
 quality = "Отличное качество"
elif loss_percent <= 5:
 quality = "Хорошее качество"
elif loss_percent <= 10:
 quality = "Удовлетворительное качество"
elif loss_percent <= 20:
  quality = "Плохое качество"
else:
 quality = "Критическое состояние сети"
print("\nВывод:")
print(f"Общее количество пакетов: {total_packets}")
print(f"Количество потерянных пакетов: {lost_packets}")
print(f"Длина самой длинной последовательности потерянных пакетов: {max_streak}")
print(f"Процент потерь: {loss_percent:.1f}%")
print(f"Качество связи: {quality}")