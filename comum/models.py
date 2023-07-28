from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Aluno(models.Model):
    sexo_opcoes = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro')
    )
    # nome = models.CharField(verbose_name='Nome', max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(verbose_name='E-mail', max_length=100)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', null=True)
    sexo = models.CharField(choices=sexo_opcoes, max_length=30, null=True)
    telefone = models.CharField(verbose_name='Telefone', max_length=15, null=True)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ('user__first_name',)

    def __str__(self) -> str:
        return '{} {}'.format(self.user.first_name, self.user.last_name)