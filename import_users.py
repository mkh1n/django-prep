import django, csv, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoestore.settings')
django.setup()

from products.models import User


with open('data/users.csv', 'r', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f, delimiter=';'):
        User.objects.create_user(
            username=row['Логин'].strip(),
            password=row['Пароль'].strip(),
            first_name = row['ФИО'].split(' ')[0],
            last_name = row['ФИО'].split(' ')[1] + ' ' + row['ФИО'].split(' ')[2],
            role = row['Роль сотрудника'].strip(),
        )
        print(f"Успешно загружен {row['Логин']}")