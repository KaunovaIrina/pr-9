import re

def validate_email(email):
    """Проверяет правильность формата email."""
    # Регулярное выражение для проверки email
    pattern = r'^(?![0-9])[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def parse_email(email):
    """Разбирает email на имя пользователя и доменное имя."""
    if validate_email(email):
        username, domain = email.split('@')
        return username, domain
    else:
        raise ValueError("Некорректный формат email.")

def main():
    email = input("Введите ваш email: ")
    
    try:
        username, domain = parse_email(email)
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
