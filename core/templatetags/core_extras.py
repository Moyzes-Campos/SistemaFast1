from django import template
from core import models

register = template.Library()


@register.inclusion_tag('atividades1.html')
def tamanho_model():
    tamanho = models.AtividadeIndex.objects.filter(area='AE').count()
    tam_AF = models.AtividadeIndex.objects.filter(area='AE').filter(situacao='AF').count() /tamanho
    tam_FA = models.AtividadeIndex.objects.filter(area='AE').filter(situacao='FA').count() /tamanho
    tam_FE = models.AtividadeIndex.objects.filter(area='AE').filter(situacao='FE').count() / tamanho

    return {'tam_AF': tam_AF,
            'tam_FA': tam_FA,
            'tam_FE': tam_FE}
