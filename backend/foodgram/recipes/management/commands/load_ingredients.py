import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from recipes.models import Ingredient, Tag

class Command(BaseCommand):
    help = 'Загрузка ингредиентов из JSON файла'

    def handle(self, *args, **options):
        # 1. Проверяем, куда мы вообще пишем
        db_name = settings.DATABASES['default']['NAME']
        db_host = settings.DATABASES['default']['HOST']
        self.stdout.write(f'Попытка записи в базу: {db_name} на хосте: {db_host}')

        # 2. Путь к файлу (используй абсолютный для надежности)
        file_path = r"F:\Dev\foodgram-project-react-master\data\ingredients.json"
        
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'Файл не найден: {file_path}'))
            return

        # 3. Сама загрузка
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
            ingredients_to_create = []
            
            for item in data:
                # Используем update_or_create, чтобы не плодить дубли
                Ingredient.objects.update_or_create(
                    name=item['name'],
                    measurement_unit=item['measurement_unit']
                )

        final_count = Ingredient.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'Загрузка завершена! Объектов в таблице {Ingredient._meta.db_table}: {final_count}'
        ))