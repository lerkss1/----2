import string

password = input ("Введите пароль: ")
errors = []

if len(password) != 8:
    errors.append ("Длина пароля неравна 8")

if not any (c.isupper() for c in password):
    errors.append("В пароле отсутствуют заглавные буквы")

if not any (c.islower() for c in password):
    errors.append("В пароле отсутствуют строчные буквы")

if not any (c.isdigit() for c in password):
    errors. append ("В пароле отсутствуют цифры")

allowed_specials = "*-#"
if not any ( c in allowed_specials for c in password):
    errors.append ("В пароле отсутствуют специальные символы")

allowed_chars = string.ascii_letters +string.digits + allowed_specials
has_invalid = False
for c in password:
   if c not in allowed_chars:
     has_invalid = True
     break
if has_invalid:
    errors.append("В пароле используются непредусмотренные CИМВОЛЫ")

if not errors:
  print ( "Надежный пароль")
else:
 for err in errors:
   print (err)