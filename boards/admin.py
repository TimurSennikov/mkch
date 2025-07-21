from django.contrib import admin
from .models import Board, Thread, Comment

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('code',)

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'creation')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'creation')
