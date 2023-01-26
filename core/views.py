# Create your views here.
from django.views.generic import TemplateView
from .models import Regulamento, AtividadeIndex, ObjetivosArea, Event, Integrantes
from django.views.generic.detail import DetailView


class IndexViewAE(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexViewAE, self).get_context_data(**kwargs)
        context['titulo3'] = Regulamento.objects.all()
        context['atividades'] = AtividadeIndex.objects.all().filter(area="AE")
        context['objetivos'] = ObjetivosArea.objects.all().filter(area="AE")
        context['integrantes'] = Integrantes.objects.all().filter(area="AE")
        context['pagina'] = ('Home')

        tamanho = AtividadeIndex.objects.filter(area='AE').count()
        if tamanho > 0:
            tam_AF = AtividadeIndex.objects.filter(area='AE').filter(situacao='AF').count() / tamanho
            tam_AF = int(tam_AF * 100)
            tam_FA = AtividadeIndex.objects.filter(area='AE').filter(situacao='FA').count() / tamanho
            tam_FA = int(tam_FA * 100)
            tam_FE = AtividadeIndex.objects.filter(area='AE').filter(situacao='FE').count() / tamanho
            tam_FE = int(tam_FE * 100)
            context['tamanhos'] = (tam_AF, tam_FA, tam_FE)

        return context


class IndexViewEL(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexViewEL, self).get_context_data(**kwargs)
        context['titulo3'] = Regulamento.objects.all()
        context['atividades'] = AtividadeIndex.objects.all().filter(area="EL")
        context['objetivos'] = ObjetivosArea.objects.all().filter(area="EL")
        context['integrantes'] = Integrantes.objects.all().filter(area="EL")
        context['pagina'] = ('Home')

        tamanho = AtividadeIndex.objects.filter(area='EL').count()
        if tamanho > 0:
            tam_AF = AtividadeIndex.objects.filter(area='EL').filter(situacao='AF').count() / tamanho
            tam_AF = int(tam_AF * 100)
            tam_FA = AtividadeIndex.objects.filter(area='EL').filter(situacao='FA').count() / tamanho
            tam_FA = int(tam_FA * 100)
            tam_FE = AtividadeIndex.objects.filter(area='EL').filter(situacao='FE').count() / tamanho
            tam_FE = int(tam_FE * 100)
            context['tamanhos'] = (tam_AF, tam_FA, tam_FE)

        return context


class IndexViewFR(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexViewFR, self).get_context_data(**kwargs)
        context['titulo3'] = Regulamento.objects.all()
        context['atividades'] = AtividadeIndex.objects.all().filter(area="FR")
        context['objetivos'] = ObjetivosArea.objects.all().filter(area="FR")
        context['integrantes'] = Integrantes.objects.all().filter(area="FR")
        context['pagina'] = ('Home')
        tamanho = AtividadeIndex.objects.filter(area='FR').count()
        if tamanho > 0:
            tam_AF = AtividadeIndex.objects.filter(area='FR').filter(situacao='AF').count() / tamanho
            tam_AF = int(tam_AF * 100)
            tam_FA = AtividadeIndex.objects.filter(area='FR').filter(situacao='FA').count() / tamanho
            tam_FA = int(tam_FA * 100)
            tam_FE = AtividadeIndex.objects.filter(area='FR').filter(situacao='FE').count() / tamanho
            tam_FE = int(tam_FE * 100)
            context['tamanhos'] = (tam_AF, tam_FA, tam_FE)

        return context


class IndexViewDS(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexViewDS, self).get_context_data(**kwargs)
        context['titulo3'] = Regulamento.objects.all()
        context['atividades'] = AtividadeIndex.objects.all().filter(area="DS")
        context['objetivos'] = ObjetivosArea.objects.all().filter(area="DS")
        context['integrantes'] = Integrantes.objects.all().filter(area="DS")
        context['pagina'] = ('Home')

        tamanho = AtividadeIndex.objects.filter(area='DS').count()
        if tamanho > 0:
            tam_AF = AtividadeIndex.objects.filter(area='DS').filter(situacao='AF').count() / tamanho
            tam_AF = int(tam_AF * 100)
            tam_FA = AtividadeIndex.objects.filter(area='DS').filter(situacao='FA').count() / tamanho
            tam_FA = int(tam_FA * 100)
            tam_FE = AtividadeIndex.objects.filter(area='DS').filter(situacao='FE').count() / tamanho
            tam_FE = int(tam_FE * 100)
            context['tamanhos'] = (tam_AF, tam_FA, tam_FE)
        return context


class IndexViewES(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexViewES, self).get_context_data(**kwargs)
        context['titulo3'] = Regulamento.objects.all()
        context['atividades'] = AtividadeIndex.objects.all().filter(area="ES")
        context['objetivos'] = ObjetivosArea.objects.all().filter(area="ES")
        context['integrantes'] = Integrantes.objects.all().filter(area="ES")
        context['pagina'] = ('Home')

        tamanho = AtividadeIndex.objects.filter(area='ES').count()
        if tamanho > 0:
            tam_AF = AtividadeIndex.objects.filter(area='ES').filter(situacao='AF').count() / tamanho
            tam_AF = int(tam_AF * 100)
            tam_FA = AtividadeIndex.objects.filter(area='ES').filter(situacao='FA').count() / tamanho
            tam_FA = int(tam_FA * 100)
            tam_FE = AtividadeIndex.objects.filter(area='ES').filter(situacao='FE').count() / tamanho
            tam_FE = int(tam_FE * 100)
            context['tamanhos'] = (tam_AF, tam_FA, tam_FE)
        return context


class IndexViewPW(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexViewPW, self).get_context_data(**kwargs)
        context['titulo3'] = Regulamento.objects.all()
        context['atividades'] = AtividadeIndex.objects.all().filter(area="PW")
        context['objetivos'] = ObjetivosArea.objects.all().filter(area="PW")
        context['integrantes'] = Integrantes.objects.all().filter(area="PW")
        context['pagina'] = ('Home')

        tamanho = AtividadeIndex.objects.filter(area='PW').count()
        if tamanho > 0:
            tam_AF = AtividadeIndex.objects.filter(area='PW').filter(situacao='AF').count() / tamanho
            tam_AF = int(tam_AF * 100)
            tam_FA = AtividadeIndex.objects.filter(area='PW').filter(situacao='FA').count() / tamanho
            tam_FA = int(tam_FA * 100)
            tam_FE = AtividadeIndex.objects.filter(area='PW').filter(situacao='FE').count() / tamanho
            tam_FE = int(tam_FE * 100)
            context['tamanhos'] = (tam_AF, tam_FA, tam_FE)
        return context


class IndexViewCM(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexViewCM, self).get_context_data(**kwargs)
        context['titulo3'] = Regulamento.objects.all()
        context['atividades'] = AtividadeIndex.objects.all().filter(area="CM")
        context['objetivos'] = ObjetivosArea.objects.all().filter(area="CM")
        context['integrantes'] = Integrantes.objects.all().filter(area="CM")
        context['pagina'] = ('Home')

        tamanho = AtividadeIndex.objects.filter(area='CM').count()
        if tamanho > 0:
            tam_AF = AtividadeIndex.objects.filter(area='CM').filter(situacao='AF').count() / tamanho
            tam_AF = int(tam_AF * 100)
            tam_FA = AtividadeIndex.objects.filter(area='CM').filter(situacao='FA').count() / tamanho
            tam_FA = int(tam_FA * 100)
            tam_FE = AtividadeIndex.objects.filter(area='CM').filter(situacao='FE').count() / tamanho
            tam_FE = int(tam_FE * 100)
            context['tamanhos'] = (tam_AF, tam_FA, tam_FE)
        return context


class IndexViewFN(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexViewFN, self).get_context_data(**kwargs)
        context['titulo3'] = Regulamento.objects.all()
        context['atividades'] = AtividadeIndex.objects.all().filter(area="FN")
        context['objetivos'] = ObjetivosArea.objects.all().filter(area="FN")
        context['integrantes'] = Integrantes.objects.all().filter(area="FN")
        context['pagina'] = ('Home')

        tamanho = AtividadeIndex.objects.filter(area='FN').count()
        if tamanho > 0:
            tam_AF = AtividadeIndex.objects.filter(area='FN').filter(situacao='AF').count() / tamanho
            tam_AF = int(tam_AF * 100)
            tam_FA = AtividadeIndex.objects.filter(area='FN').filter(situacao='FA').count() / tamanho
            tam_FA = int(tam_FA * 100)
            tam_FE = AtividadeIndex.objects.filter(area='FN').filter(situacao='FE').count() / tamanho
            tam_FE = int(tam_FE * 100)
            context['tamanhos'] = (tam_AF, tam_FA, tam_FE)
        return context


class IndexViewGS(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexViewGS, self).get_context_data(**kwargs)
        context['titulo3'] = Regulamento.objects.all()
        context['atividades'] = AtividadeIndex.objects.all().filter(area="GS")
        context['objetivos'] = ObjetivosArea.objects.all().filter(area="GS")
        context['integrantes'] = Integrantes.objects.all().filter(area="GS")
        context['pagina'] = ('Home')

        tamanho = AtividadeIndex.objects.filter(area='GS').count()
        if tamanho > 0:
            tam_AF = AtividadeIndex.objects.filter(area='GS').filter(situacao='AF').count() / tamanho
            tam_AF = int(tam_AF * 100)
            tam_FA = AtividadeIndex.objects.filter(area='GS').filter(situacao='FA').count() / tamanho
            tam_FA = int(tam_FA * 100)
            tam_FE = AtividadeIndex.objects.filter(area='GS').filter(situacao='FE').count() / tamanho
            tam_FE = int(tam_FE * 100)
            context['tamanhos'] = (tam_AF, tam_FA, tam_FE)
        return context


class IndexViewMK(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexViewMK, self).get_context_data(**kwargs)
        context['titulo3'] = Regulamento.objects.all()
        context['atividades'] = AtividadeIndex.objects.all().filter(area="MK")
        context['objetivos'] = ObjetivosArea.objects.all().filter(area="MK")
        context['integrantes'] = Integrantes.objects.all().filter(area="MK")
        context['pagina'] = ('Home')

        tamanho = AtividadeIndex.objects.filter(area='MK').count()
        if tamanho > 0:
            tam_AF = AtividadeIndex.objects.filter(area='MK').filter(situacao='AF').count() / tamanho
            tam_AF = int(tam_AF * 100)
            tam_FA = AtividadeIndex.objects.filter(area='MK').filter(situacao='FA').count() / tamanho
            tam_FA = int(tam_FA * 100)
            tam_FE = AtividadeIndex.objects.filter(area='MK').filter(situacao='FE').count() / tamanho
            tam_FE = int(tam_FE * 100)
            context['tamanhos'] = (tam_AF, tam_FA, tam_FE)
        return context


class CalendarioView(TemplateView):
    template_name = 'calendario.html'

    def get_context_data(self, **kwargs):
        context = super(CalendarioView, self).get_context_data(**kwargs)
        context['evento'] = Event.objects.all()
        return context


class RegulamentoViewAE(TemplateView):
    template_name = 'regulamento.html'

    def get_context_data(self, **kwargs):
        context = super(RegulamentoViewAE, self).get_context_data(**kwargs)
        context['regulamento'] = Regulamento.objects.all().filter(area='AE')
        context['pagina'] = ('Regulamento')
        return context


class RegulamentoViewDS(TemplateView):
    template_name = 'regulamento.html'

    def get_context_data(self, **kwargs):
        context = super(RegulamentoViewDS, self).get_context_data(**kwargs)
        context['regulamento'] = Regulamento.objects.all().filter(area='DS')
        context['pagina'] = ('Regulamento')
        return context


class RegulamentoViewEL(TemplateView):
    template_name = 'regulamento.html'

    def get_context_data(self, **kwargs):
        context = super(RegulamentoViewEL, self).get_context_data(**kwargs)
        context['regulamento'] = Regulamento.objects.all().filter(area='EL')
        context['pagina'] = ('Regulamento')
        return context


class RegulamentoViewES(TemplateView):
    template_name = 'regulamento.html'

    def get_context_data(self, **kwargs):
        context = super(RegulamentoViewES, self).get_context_data(**kwargs)
        context['regulamento'] = Regulamento.objects.all().filter(area='ES')
        context['pagina'] = ('Regulamento')
        return context


class RegulamentoViewFR(TemplateView):
    template_name = 'regulamento.html'

    def get_context_data(self, **kwargs):
        context = super(RegulamentoViewFR, self).get_context_data(**kwargs)
        context['regulamento'] = Regulamento.objects.all().filter(area='FR')
        context['pagina'] = ('Regulamento')
        return context


class RegulamentoViewPW(TemplateView):
    template_name = 'regulamento.html'

    def get_context_data(self, **kwargs):
        context = super(RegulamentoViewPW, self).get_context_data(**kwargs)
        context['regulamento'] = Regulamento.objects.all().filter(area='PW')
        context['pagina'] = ('Regulamento')
        return context


class RegulamentoViewCM(TemplateView):
    template_name = 'regulamento.html'

    def get_context_data(self, **kwargs):
        context = super(RegulamentoViewCM, self).get_context_data(**kwargs)
        context['regulamento'] = Regulamento.objects.all().filter(area='CM')
        context['pagina'] = ('Regulamento')
        return context


class RegulamentoViewGS(TemplateView):
    template_name = 'regulamento.html'

    def get_context_data(self, **kwargs):
        context = super(RegulamentoViewGS, self).get_context_data(**kwargs)
        context['regulamento'] = Regulamento.objects.all().filter(area='GS')
        context['pagina'] = ('Regulamento')
        return context


class RegulamentoViewFN(TemplateView):
    template_name = 'regulamento.html'

    def get_context_data(self, **kwargs):
        context = super(RegulamentoViewFN, self).get_context_data(**kwargs)
        context['regulamento'] = Regulamento.objects.all().filter(area='FN')
        context['pagina'] = ('Regulamento')
        return context


class RegulamentoViewMK(TemplateView):
    template_name = 'regulamento.html'

    def get_context_data(self, **kwargs):
        context = super(RegulamentoViewMK, self).get_context_data(**kwargs)
        context['regulamento'] = Regulamento.objects.all().filter(area='MK')
        context['pagina'] = ('Regulamento')
        return context


class BrainstormView(TemplateView):
    template_name = 'brainstorm.html'


class AnaliseView(TemplateView):
    template_name = 'analise.html'


class LicoesView(TemplateView):
    template_name = 'licoes.html'
