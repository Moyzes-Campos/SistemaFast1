from django.db import models
from stdimage.models import StdImageField

# Create your models here.


class Regulamento(models.Model):
    Areas = (
        ('AE', 'Aerodinâmica'),
        ('DS', 'Direção e Suspenção'),
        ('EL', 'Elétrica'),
        ('ES', 'Estrutura'),
        ('FR', 'Freio e Ergonomia'),
        ('PW', 'Powewtrain'),
        ('CM', 'Comercial'),
        ('FN', 'Financeiro'),
        ('GS', 'Gestão de Pessoas'),
        ('MK', 'Marketing'),
    )

    T1_choices = (
        ('GR - General Regulations', 'GR - General Regulations'),
        ('AD - Administrative Regulations', 'AD - Administrative Regulations'),
        ('DR - Document Requirements', 'DR - Document Requirements'),
        ('V - Vehicle Requirements', 'V - Vehicle Requirements'),
        ('F - Chassis and Structural ', 'F - Chassis and Structural'),
        ('T - Technical Aspects ', 'T - Technical Aspects'),
        ('VE - Vehicle and Driver Equipament', 'VE - Vehicle and Driver Equipament'),
        ('IC - Internal Combustion Engine Vehicles', 'IC - Internal Combustion Engine Vehicles'),
        ('IN - Technical Inspection', 'IN - Technical Inspection'),
        ('S - Static Events', 'S - Static Events'),
        ('D - Dynamic Events', 'D - Dynamic Events'),
    )

    t1 = models.CharField('Título 1', max_length=50, choices=T1_choices)
    t2 = models.CharField('Título 2', max_length=50, default='Default')
    t3 = models.CharField('Título 3', max_length=100, default='Default')
    resumo = models.TextField(help_text='Escreva o resumo')
    area = models.CharField(max_length=100, choices=Areas, null=True, blank=True)

    class Meta:
        verbose_name = 'Regulamento'
        verbose_name_plural = 'Regulamento'

    def __str__(self):
        return self.t3


class Event(models.Model):
    day = models.DateField('Data', help_text='Data do evento')
    start_time = models.TimeField('Início', help_text='Início')
    notes = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Calendário Fast'
        verbose_name_plural = 'Calendário Fast'


class AtividadeIndex(models.Model):
    Areas = (
        ('AE', 'Aerodinâmica'),
        ('DS', 'Direção e Suspenção'),
        ('EL', 'Elétrica'),
        ('ES', 'Estrutura'),
        ('FR', 'Freio e Ergonomia'),
        ('PW', 'Powewtrain'),
        ('CM', 'Comercial'),
        ('FN', 'Financeiro'),
        ('GS', 'Gestão de Pessoas'),
        ('MK', 'Marketing'),
    )

    situacao = (
        ('AF', 'A fazer'),
        ('FA', 'Fazendo'),
        ('FE', 'Feito'),
    )

    area = models.CharField(max_length=100, choices=Areas)
    situacao = models.CharField(max_length=100, choices=situacao)
    descricao = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'


class ObjetivosArea(models.Model):
    areas_choices = (
        ('AE', 'Aerodinâmica'),
        ('DS', 'Direção e Suspenção'),
        ('EL', 'Elétrica'),
        ('ES', 'Estrutura'),
        ('FR', 'Freio e Ergonomia'),
        ('PW', 'Powewtrain'),
        ('CM', 'Comercial'),
        ('FN', 'Financeiro'),
        ('GS', 'Gestão de Pessoas'),
        ('MK', 'Marketing'),
        ('NA', 'Nenhuma'),
    )
    titulo = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    area = models.CharField(max_length=50, choices=areas_choices, default='Nenhuma')

    class Meta:
        verbose_name = 'Objetivo'
        verbose_name_plural = 'Objetivos'


class Integrantes(models.Model):
    funcao_choices = (
        ('Cordenador', 'Cordenador'),
        ('Assesor', 'Assesor'),
        ('Conselheiro', 'Conselheiro'),
        ('Capitão', 'Capitão(ã)'),
        ('Vice Capitão', 'Vice Capitão(ã)'),
        ('Diretor de Projetos', 'Diretor(a) de Projetos'),
        ('Diretor Administrativo', 'Diretor(a) Administrativo'),
    )

    areas_choices = (
        ('AE', 'Aerodinâmica'),
        ('DS', 'Direção e Suspenção'),
        ('EL', 'Elétrica'),
        ('ES', 'Estrutura'),
        ('FR', 'Freio e Ergonomia'),
        ('PW', 'Powewtrain'),
        ('CM', 'Comercial'),
        ('FN', 'Financeiro'),
        ('GS', 'Gestão de Pessoas'),
        ('MK', 'Marketing'),
        ('NA', 'Nenhuma'),
    )
    nome = models.CharField(max_length=50)
    funcao = models.CharField(max_length=50, choices=funcao_choices)
    area = models.CharField(max_length=50, choices=areas_choices)
    foto = StdImageField('foto', upload_to='integrantes')

    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'
