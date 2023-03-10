# Generated by Django 3.2.16 on 2023-01-25 11:42

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='integrantes',
            options={'verbose_name': 'Integrante', 'verbose_name_plural': 'Integrantes'},
        ),
        migrations.AlterModelOptions(
            name='objetivosarea',
            options={'verbose_name': 'Objetivo', 'verbose_name_plural': 'Objetivos'},
        ),
        migrations.AddField(
            model_name='regulamento',
            name='area',
            field=models.CharField(blank=True, choices=[('AE', 'Aerodinâmica'), ('DS', 'Direção e Suspenção'), ('EL', 'Elétrica'), ('ES', 'Estrutura'), ('FR', 'Freio e Ergonomia'), ('PW', 'Powewtrain'), ('CM', 'Comercial'), ('FN', 'Financeiro'), ('GS', 'Gestão de Pessoas'), ('MK', 'Marketing')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='integrantes',
            name='foto',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='integrantes', variations={}, verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='integrantes',
            name='funcao',
            field=models.CharField(choices=[('Cordenador', 'Cordenador'), ('Assesor', 'Assesor'), ('Conselheiro', 'Conselheiro'), ('Capitão', 'Capitão(ã)'), ('Vice Capitão', 'Vice Capitão(ã)'), ('Diretor de Projetos', 'Diretor(a) de Projetos'), ('Diretor Administrativo', 'Diretor(a) Administrativo')], max_length=50),
        ),
        migrations.AlterField(
            model_name='regulamento',
            name='t1',
            field=models.CharField(choices=[('GR - General Regulations', 'General Regulations'), ('AD - Administrative Regulations', 'Administrative Regulations'), ('DR - Document Requirements', 'DR - Document Requirements')], max_length=50, verbose_name='T1'),
        ),
    ]
