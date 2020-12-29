# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def get_user_personal_data(**kwargs):
    """Return personal data as a dictionary."""
    return kwargs


pers_data = get_user_personal_data(name=(input('Enter name: ')), surname=(input('Enter surname: ')),
                                   birth_year=(input('Enter year of birth: ')),
                                   resedence_city=(input('Enter city of resedence: ')),
                                   email=(input('Enter email: ')), phone_number=(input('Enter phone number: ')))
print(pers_data)
