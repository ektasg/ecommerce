from django.contrib import admin
from .models import Book, Author, Cart, BookOrder

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price','stock')


class AuthorAdmin(admin.ModelAdmin):
   list_display = ('last_name', 'first_name')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'active', 'order_date')


class BookOrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'cart' , 'quantity')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(BookOrder, BookOrderAdmin)