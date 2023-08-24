from django.contrib import admin
from .models import Room, RoomImage, Event, EventImage, AboutUsContent
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)

@admin.register(RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    list_display = ('room', 'image')
    list_filter = ('room',)
    search_fields = ('room__title',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'date')
    list_filter = ('date',)

@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ('event', 'image')
    list_filter = ('event',)
    search_fields = ('event__title',)  # Searching using related field's title

@admin.register(AboutUsContent)
class AboutUsContentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    