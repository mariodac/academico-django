# Generated by Django 3.2.7 on 2023-07-15 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matricula',
            options={'ordering': ['nome_aluno'], 'verbose_name': 'Matricula de Aluno', 'verbose_name_plural': 'Matricula de Alunos'},
        ),
    ]
