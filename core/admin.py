from django.contrib import admin
from .models import *


# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome')


class Alunodmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'data_nascimento', 'email')


class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano_publicacao')


class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'data_retirado', 'data_devolucao', 'devolvido')


admin.site.register(Autor, AutorAdmin)
admin.site.register(Aluno, Alunodmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
