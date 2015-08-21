from django.contrib import admin
from .models import hotel,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class hotelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['hotel_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('hotel_text', 'pub_date',"was_published_recently")
    list_filter = ['pub_date']
    search_fields = ['hotel_text']

admin.site.register(hotel, hotelAdmin)
