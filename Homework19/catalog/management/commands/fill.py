import json
from config.settings import BASE_DIR

from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Заполнение базы данных данными из нескольких файлов'

    def handle(self, *args, **kwargs):


        Product.objects.all().delete()
        Category.objects.all().delete()

        try:
            with open(BASE_DIR / 'category.json', 'r', encoding='utf-8-sig') as file:
                category_data = json.load(file)
                for item in category_data:
                    Category.objects.create(
                        pk=item['pk'],
                        category_name=item['fields']['category_name'],
                        disc=item['fields']['disc']
                )
            with open(BASE_DIR / 'product_card.html.json', 'r', encoding='utf-8-sig') as file:
                product_data = json.load(file)
                for item in product_data:
                    category_name = item['fields']['category']
                    category = Category.objects.get(pk=category_name)
                    Product.objects.create(
                        pk=item['pk'],
                        product_name=item['fields']['product_name'],
                        product_disc=item['fields']['product_disc'],
                        image=item['fields']['image'],
                        category=category,
                        price=item['fields']['price'],
                        data_created=item['fields']['data_created'],
                        data_changed=item['fields']['data_changed']
                )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при импорте данных: {e}'))

        else:
            self.stdout.write(self.style.SUCCESS('Данные успешно добавлены в базу данных'))