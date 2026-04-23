import django, csv, os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoestore.settings')
django.setup()

from products.models import Product, Supplier, Manufacturer, Category

with open('data/products.csv', 'r', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f, delimiter=';'):
        cat, _ = Category.objects.get_or_create(name = row['Категория товара'].strip())
        sup, _ = Supplier.objects.get_or_create(name = row['Поставщик'].strip())
        man, _ = Manufacturer.objects.get_or_create(name = row['Производитель'].strip())

        Product.objects.get_or_create(
            article = row['Артикул'],
            defaults={
                'name': row['Наименование товара'].strip(),
                'unit_type': row['Единица измерения'].strip(),
                'price': row['Цена'].strip(),
                'supplier': sup,
                'manufacturer': man,
                'category': cat,
                'discount': row['Действующая скидка'].strip(),
                'stock_quantity': row['Кол-во на складе'].strip(),
                'description': row['Описание товара'].strip(),
                'photo': row['Фото'].strip()
            }
        )
        print(f"Успешно загружен {row['Артикул']}")
        