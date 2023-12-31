from django.db import models

# Create your models here.

class Matricula(models.Model):
    matricula = models.IntegerField()
    # nome_aluno = models.CharField(max_length=200)
    aluno = models.ForeignKey('comum.Aluno', verbose_name='Aluno', related_name='comum_aluno', on_delete=models.CASCADE)
    curso = models.CharField(max_length=100)
    observacao = models.TextField()
    data_matricula = models.DateTimeField(verbose_name="Data da matrícula", blank=True, auto_now_add=True)

    class Meta:
        verbose_name = "Matricula de Aluno"
        verbose_name_plural = "Matricula de Alunos"
        ordering = ["aluno__user__first_name"]

