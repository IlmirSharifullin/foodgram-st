from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


MIN_VALUE = 1
MAX_VALUE = 32000


class Ingredient(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    measurement_unit = models.CharField(
        max_length=16,
        verbose_name="Единица измерения",
    )
    name = models.CharField(
        max_length=128,
        verbose_name="Название",
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    class Meta:
        ordering = ["-created_at"]

        verbose_name = "рецепт"
        verbose_name_plural = "Рецепты"

    name = models.CharField(
        max_length=256,
        verbose_name="Название",
    )
    text = models.TextField(
        verbose_name="Описание",
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(MIN_VALUE),
                    MaxValueValidator(MAX_VALUE)],
        verbose_name="Время приготовления",
    )
    image = models.ImageField(
        verbose_name="Картинка",
        upload_to="recipes/",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время публикации",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipe",
        verbose_name="Автор",
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        through="RecipeIngredient",
        verbose_name="Ингредиенты",
    )

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    class Meta:
        verbose_name = "рецепт и ингредиент"
        verbose_name_plural = "Рецепты и ингредиенты"
        ordering = ["-recipe__created_at", "ingredient__name"]


    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name="Рецепт",
        related_name="recipe_ingredients",
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name="Ингредиент",
    )
    amount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(MIN_VALUE),
                    MaxValueValidator(MAX_VALUE)],
    )

    def __str__(self):
        return f'{self.ingredient.name} for {self.recipe.name}'
