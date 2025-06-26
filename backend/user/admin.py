from django.contrib import admin
from .models import User, Follow, Favorite, ShoppingCart


class UserAdmin(admin.ModelAdmin):
    search_fields = ("email", "username")
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "avatar",
        "is_subscribed",
    )
    list_editable = (
        "username",
        "first_name",
        "last_name",
        "avatar",
        "is_subscribed",
    )
    list_display_links = ("email",)


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "following",
    )
    list_display_links = ("user",)
    list_editable = ("following",)


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "recipe",
    )
    list_display_links = ("user",)
    list_editable = ("recipe",)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "recipe",
    )
    list_display_links = ("user",)
    list_editable = ("recipe",)


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Favorite, FavoriteAdmin)
