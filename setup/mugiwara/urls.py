from django.urls import path
from mugiwara import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login.as_view(), name="login"),
    path("signup/", views.signup.as_view(), name="signup"),
    path("logout/", views.userLogout, name="logout"),

    path('conta_bancaria/', views.createContaBancariaView, name='conta_bancaria'),
    path('conta_bancaria/<int:c_id>', views.updateContaBancariaView, name='conta_bancaria'),
    path('delete_conta_bancaria/<int:c_id>', views.deleteContaBancariaView, name='delete_conta_bancaria'),
    path('show_conta_bancaria/', views.showContaBancariaView, name='show_conta_bancaria'),

    path('despesa/', views.createDespesaView, name='despesa'),
    path('delete_despesa/<int:c_id>', views.deleteDespesaView, name='delete_despesa'),
    path('show_despesa/', views.showDespesaView, name='show_despesa'),

    path('fluxo_caixa/', views.createFluxoCaixaView, name='fluxo_caixa'),
    path('delete_fluxo_caixa/<int:f_id>', views.deleteFluxoCaixaView, name='delete_fluxo_caixa'),
    path('show_fluxo_caixa/', views.showFluxoCaixaView, name='show_fluxo_caixa'),
    path('show_fluxo_caixa_one/<int:f_id>', views.showFluxoCaixaOneView, name='show_fluxo_caixa_one'),

    path('show_pagamentos', views.showPagamentoView, name='show_pagamentos'),
    path('pagamento/<int:d_id>', views.pagamentoView, name='pagamento'),

    path('receita/', views.createReceitaView, name='receita'),
    path('delete_receita/<int:r_id>', views.deleteReceitaView, name='delete_receita'),
    path('show_receita/', views.showReceitaView, name='show_receita'),    

    path('recebimento/<int:r_id>', views.recebimentoView, name='recebimento'),
    path('show_recebimentos/', views.showRecebimentoView, name='show_recebimentos'),

]