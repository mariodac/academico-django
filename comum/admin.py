from django.contrib import admin
from .models import Aluno

# Register your models here.
class AdminAlunos(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    list_per_page = 10
admin.site.register(Aluno, )