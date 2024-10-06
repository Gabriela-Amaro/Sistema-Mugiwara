from django.db import models

class usuario(models.Model):
    class role_opt(models.IntegerChoices):
        ADMIN = 1, "Administrador"
        USUARIO = 2, "Usuário"

    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    senha_hash = models.CharField(max_length=254)
    role = models.IntegerField(
        choices = role_opt,
        default = role_opt.USUARIO,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
class fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email =  models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class cliente(models.Model):
    nome = models.CharField(max_length=100)
    cnpj_cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email =  models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
class fluxo_caixa(models.Model):
    data = models.DateField(auto_now_add=True)
    saldo_inicial = models.DecimalField(decimal_places=2, max_digits=9)
    saldo_final = models.DecimalField(decimal_places=2, max_digits=9)
    projecao_entradas = models.DecimalField(decimal_places=2, max_digits=9)
    projecao_saidas = models.DecimalField(decimal_places=2, max_digits=9)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.data
    
class relatorio(models.Model):
    class relatorio_tipo(models.IntegerChoices):
        RECEITA = 1, "Receita"
        DESPESA  = 2, "Despesa"

    tipo = models.IntegerField(
        choices =  relatorio_tipo
    )
    periodo_inicio = models.DateField(auto_now=False, auto_now_add=False)
    periodo_fim = models.DateField(auto_now=False, auto_now_add=False)
    arquivo_pdf  = models.FileField(upload_to=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Relatório de {self.periodo_inicio} à {self.periodo_fim}"
    
class despesa(models.Model):
    descricao = models.TextField()
    data_vencimento = models.DateField(auto_now=False, auto_now_add=False)
    valor = models.DecimalField(decimal_places=2, max_digits=9)
    categoria = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    fornecedor = models.ForeignKey(
        fornecedor,
        on_delete = models.SET_NULL,
        null = True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"vencimento: {self.data_vencimento}, valor: {self.valor}"
    
class receita(models.Model):
    descricao = models.TextField()
    data_vencimento = models.DateField(auto_now=False, auto_now_add=False)
    valor = models.DecimalField(decimal_places=2, max_digits=9)
    categoria = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(
        cliente,
        on_delete = models.SET_NULL,
        null = True 
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"vencimento: {self.data_vencimento}, valor: {self.valor}"
    
class conta_bancaria(models.Model):
    nome_banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=3)
    numero_conta = models.CharField(max_length=50)
    saldo_atual = models.DecimalField(decimal_places=2, max_digits=9)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome_banco', 'saldo_atual']

    def __str__(self):
        return f"Banco: {self.nome_banco}, agencia: {self.agencia}, conta: {self.numero_conta}"
    
class pagamento(models.Model):
    class  metodos_pagamento(models.IntegerChoices):
        DINHEIRO = 1, "Dinheiro"
        DEBITO  = 2, "Débito em conta"

    valor_pago = models.DecimalField(decimal_places=2, max_digits=9)
    metodo_pagamento = models.IntegerField(
        choices = metodos_pagamento,
        default = metodos_pagamento.DINHEIRO,
    )
    created_at  =  models.DateTimeField(auto_now_add=True)
    despesa = models.ForeignKey(
        despesa,
        on_delete =  models.CASCADE
    )
    conta_bancaria  = models.ForeignKey(
        conta_bancaria,
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"data: {self.created_at}, valor: {self.valor_pago}"
    
class recebimento(models.Model):
    class  metodos_recebimento(models.IntegerChoices):
        DINHEIRO = 1, "Dinheiro"
        PIX = 2, "Pix"

    valor_pago = models.DecimalField(decimal_places=2, max_digits=9)
    metodo_recebimento = models.IntegerField(
        choices = metodos_recebimento,
        default = metodos_recebimento.DINHEIRO,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    receita = models.ForeignKey(
        receita,
        on_delete = models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"data: {self.created_at}, valor: {self.valor_pago}"
    
class extrato_bancario(models.Model):
    arquivo_extrato = models.FileField(upload_to=None)
    created_at = models.DateTimeField(auto_now_add=True)
    conta_bancaria = models.ForeignKey(
        conta_bancaria,
        on_delete = models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"data: {self.created_at}, conta: {self.conta_bancaria.numero_conta}"
