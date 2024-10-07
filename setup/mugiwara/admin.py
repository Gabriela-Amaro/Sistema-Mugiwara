from django.contrib import admin

from .models import conta_bancaria, despesa, receita

admin.site.register(conta_bancaria)
admin.site.register(despesa)
admin.site.register(receita)
