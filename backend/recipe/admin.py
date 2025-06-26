from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "measurement_unit",
    )
    list_display_links = ("name",)
    list_editable = ("measurement_unit",)
    search_fields = ("name",)


class RecipeAdmin(admin.ModelAdmin):
    search_fields = (
        "name",
        "author__email",
    )
    list_display = (
        "name",
        "author",
    )
    list_display_links = ("name",)
    list_editable = ("author",)

    readonly_fields = ("get_favorite_count",)

    def get_favorite_count(self, obj):
        return obj.in_favorites.count()

    get_favorite_count.short_description = "Добавление(-й) в избранное"


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)
