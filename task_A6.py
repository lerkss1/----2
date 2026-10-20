N = int(input("Введите количество секунд с начала суток: "))
hours = N // 3600
minutes = (N % 3600) // 60
seconds = N % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")