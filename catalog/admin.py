from django.contrib import admin

# Register your models here.


from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(BookInstance)
admin.site.register(Genre)
#admin.site.register(Language)





class BooksInstanceInline(admin.StackedInline):
    model = BookInstance
    extra= 0


class BookInline(admin.StackedInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    
    #Play with these modify them

    fieldsets = (
        ('General Info', {
            'fields': ('first_name', 'last_name','genre')
        }),
        ('Dates', {
            'fields': (('date_of_birth', 'date_of_death'))
        }),
    )








 #Compare the view of __bookinstance__ with and without
#> `inlines = [BooksInstanceInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]    



@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
            (None, {
                'fields': ('book','imprint', 'id')
            }),
            ('Availability', {
                'fields': ('status', 'due_back', 'borrower')
            }),
        )

#Added language and inline book
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']

    inlines =[BookInline]
