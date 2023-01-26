from django.urls import path
from .views import IndexViewAE, IndexViewEL, CalendarioView, IndexViewCM, \
    IndexViewDS, IndexViewES, IndexViewFN, IndexViewGS, IndexViewMK, IndexViewPW, IndexViewFR,\
    RegulamentoViewAE, BrainstormView, AnaliseView, LicoesView, RegulamentoViewCM, RegulamentoViewDS, RegulamentoViewEL,\
    RegulamentoViewES, RegulamentoViewFN, RegulamentoViewFR, RegulamentoViewGS, RegulamentoViewMK, RegulamentoViewPW

urlpatterns = [
    path('', IndexViewAE.as_view(), name='indexAE'),
    path('EL', IndexViewEL.as_view(), name='indexEL'),
    path('DS', IndexViewDS.as_view(), name='indexDS'),
    path('ES', IndexViewES.as_view(), name='indexES'),
    path('FR', IndexViewFR.as_view(), name='indexFR'),
    path('PW', IndexViewPW.as_view(), name='indexPW'),
    path('CM', IndexViewCM.as_view(), name='indexCM'),
    path('FN', IndexViewFN.as_view(), name='indexFN'),
    path('GS', IndexViewGS.as_view(), name='indexGS'),
    path('MK', IndexViewMK.as_view(), name='indexMK'),
    path('calendario', CalendarioView.as_view(), name='calendario'),
    path('regulamento/AE', RegulamentoViewAE.as_view(), name='regulamentoAE'),
    path('regulamento/DS', RegulamentoViewDS.as_view(), name='regulamentoDS'),
    path('regulamento/EL', RegulamentoViewEL.as_view(), name='regulamentoEL'),
    path('regulamento/ES', RegulamentoViewES.as_view(), name='regulamentoES'),
    path('regulamento/FR', RegulamentoViewFR.as_view(), name='regulamentoFR'),
    path('regulamento/PW', RegulamentoViewPW.as_view(), name='regulamentoPW'),
    path('regulamento/CM', RegulamentoViewCM.as_view(), name='regulamentoCM'),
    path('regulamento/MK', RegulamentoViewMK.as_view(), name='regulamentoMK'),
    path('regulamento/GS', RegulamentoViewGS.as_view(), name='regulamentoGS'),
    path('regulamento/FN', RegulamentoViewFN.as_view(), name='regulamentoFN'),
    path('brainstorm', BrainstormView.as_view(), name='brainstorm'),
    path('analise', AnaliseView.as_view(), name='analise'),
    path('licoes', LicoesView.as_view(), name='licoes'),
]
