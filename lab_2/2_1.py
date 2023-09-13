def is_password_good(password):
    if (len(password) > 10 and any(map(lambda x: x.islower(), password))
            and any(map(lambda x: x.isupper(), password)) and any(map(lambda x: x.isalpha(), password))):
        return True
    else:
        return False


passw = input("Введите пароль для проверки его корректности: ")

print("Пароль прошел проверку на валидность" if is_password_good(
    passw) else "Пароль не прошел проверку на валидность")
