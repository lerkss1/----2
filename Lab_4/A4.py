def check_card_validity(card_number):
    # Убираем все пробелы и дефисы, если пользователь их ввел
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Проверяем, что строка состоит только из цифр
    if not card_number.isdigit():
        return False, "Ошибка: номер карты должен содержать только цифры."
    

    if len(card_number) < 13 or len(card_number) > 19:
        return False, "Ошибка: неверная длина номера карты."


    total_sum = 0
 
    for i, char in enumerate(reversed(card_number)):
        digit = int(char)
        
    
        if i % 2 == 1:
            digit *= 2

            if digit > 9:
                digit -= 9
                
        total_sum += digit

   
    if total_sum % 10 == 0:
        return True, "Валидный номер карты!"
    else:
        return False, "Невалидный номер карты (ошибка контрольной суммы)."

if __name__ == "__main__":
    user_card = input("Введите номер кредитной карты: ")
    
    is_valid, message = check_card_validity(user_card)
    
    print(message)
