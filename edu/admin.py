from django.contrib import admin
from .models import Matricula

# Register your models here.
class AdminMatricula(admin.ModelAdmin):
    list_display = ['id', 'matricula', 'aluno', 'data_matricula']
    list_display_links = ['id', 'matricula']
    search_fields = ['aluno__user__first_name', 'data_matricula']
    list_filter = ['curso']
    list_per_page = 2
admin.site.register(Matricula, AdminMatricula)