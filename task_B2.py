def calculate_wind_chill(temp_f, wind_speed):
    """Вычисляет температуру ветрового охлаждения по формуле."""
    # Формула из задания. Оператор ** означает возведение в степень.
    wc = 35.74 + (0.6215 * temp_f) - (35.75 * (wind_speed  0.16)) + (0.4275 * temp_f * (wind_speed  0.16))
    return wc

def process_weather_data(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_filename} не найден.")
        return

    # Списки для хранения результатов
    report_lines = []
    wc_effects = []

    # Формируем заголовок отчета
    report_lines.append("Time        WC temp    WC Effect")
    report_lines.append("-" * 35)

    # Обрабатываем строки, начиная с 3-й (индекс 2), так как первые две - шапка
    for line in lines[2:]:
        # Разбиваем строку по пробелам или табуляции
        parts = line.split()
        
        # Проверка, что строка не пустая и содержит все 3 нужных элемента
        if len(parts) >= 3:
            time_str = parts[0]
            try:
                temp = float(parts[1])
                wind = float(parts[2])
                
                # Вычисляем WC Effect
                wc_effect = calculate_wind_chill(temp, wind)
                wc_effects.append(wc_effect)
                
                # Форматируем строку для вывода (выравнивание как в примере)
                # :<12 - выравнивание по левому краю шириной 12 символов
                # :>5.1f - выравнивание по правому краю, 1 знак после запятой
                formatted_line = f"{time_str:<12}{temp:>5.1f}     {wc_effect:>6.1f}"
                report_lines.append(formatted_line)
                
            except ValueError:
                # Пропускаем строки, где данные не являются числами (например, разделители)
                continue

    # Вычисляем среднее значение
    if wc_effects:
        average_wc = sum(wc_effects) / len(wc_effects)
        report_lines.append("-" * 35)
        # Форматируем строку со средним значением
        avg_text = f"The average adjusted temperature, based on {len(wc_effects)} observations, was {average_wc:.1f}"
        report_lines.append(avg_text)
    else:
        report_lines.append("Нет данных для обработки.")

    # Записываем результат в выходной файл
    with open(output_filename, 'w') as outfile:
        for line in report_lines:
            outfile.write(line + '\n')
            
    print(f"Обработка завершена. Результаты сохранены в {output_filename}")

# --- Основная часть программы ---
# Измените цифру 1 на номер вашего варианта, если нужно
input_file = "1.WCData.txt"   
output_file = "1.WindChillReport.txt"

process_weather_data(input_file, output_file)
