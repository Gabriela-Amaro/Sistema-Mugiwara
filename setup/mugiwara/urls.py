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
    path('despesa/<int:c_id>', views.updateDespesaView, name='despesa'),
    path('delete_despesa/<int:c_id>', views.deleteDespesaView, name='delete_despesa'),
    path('show_despesa/', views.showDespesaView, name='show_despesa'),
]