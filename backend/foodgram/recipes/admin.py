from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from .models import Ingredient, Recipe, Tag

class IngredientResource(resources.ModelResource):
    # Если в вашей модели поля называются так же, как в JSON,
    # то дополнительные настройки не нужны.
    # Но мы укажем 'import_id_fields', чтобы Django не ругался на отсутствие ID в файле.
    
    class Meta:
        model = Ingredient
        # Указываем, что определять уникальность будем по имени, а не по ID
        import_id_fields = ('name',) 
        fields = ('name', 'measurement_unit')
        # Эта опция заставит импорт пропускать неизмененные строки
        skip_unchanged = True
        # Эта опция позволит создавать записи без указания ID в JSON
        report_skipped = True

@admin.register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin):
    resource_class = IngredientResource
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)

@admin.register(Recipe)
class RecipeAdmin(ImportExportModelAdmin):
    list_display = ('title', 'author', 'tag', 'time_to_cook')
    search_fields = ('title', 'author__username')
    list_filter = ('tag', 'author')
    filter_horizontal = ('ingredient',)

@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', 'color')
    prepopulated_fields = {'slug': ('name',)}