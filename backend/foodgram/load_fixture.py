import os
import json
import django
from django.db import transaction, IntegrityError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodgram.settings')
django.setup()

from recipes.models import Ingredient

FILE_PATH = r"F:\Dev\foodgram-project-react-master\data\ingredients.json"

def load_data():
    if not os.path.exists(FILE_PATH):
        print(f"Файл не найден по пути: {FILE_PATH}")
        return

    with open(FILE_PATH, encoding='utf-8') as f:
        data = json.load(f)
        
    print(f"Найдено {len(data)} записей в JSON. Начинаю загрузку...")

    try:
        with transaction.atomic():
            for item in data:
                # Используем update_or_create для надежности
                obj, created = Ingredient.objects.update_or_create(
                    name=item['name'],
                    measurement_unit=item['measurement_unit'],
                    defaults={} # здесь можно обновить поля, если они изменятся
                )
            
        final_count = Ingredient.objects.count()
        print(f"Успех! В базе данных PostgreSQL теперь {final_count} ингредиентов.")
        
    except IntegrityError as e:
        print(f"Ошибка целостности базы данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    load_data()