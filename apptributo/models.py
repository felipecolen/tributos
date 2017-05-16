from django.db import models


class Pessoa(models.Model):
    pessoa_cpf = models.CharField(max_length=15)
    pessoa_nome = models.CharField(max_length=60)

    # aqui vc sobrescreve o método de salvamento, incluindo opções adicionais...
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.pessoa_nome = self.pessoa_nome.upper()  # coloca ASSIM ao salvar
        super(Pessoa, self).save()

    def __str__(self):
        return '{} {}'.format(self.pessoa_nome, self.pessoa_cpf)

    class Meta:
        ordering = ['pessoa_nome', ]
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class Veiculo(models.Model):
    fk_pessoa = models.ForeignKey(Pessoa)
    veiculo_placa = models.CharField(max_length=7)
    veiculo_preco_fipe = models.DecimalField(max_digits=9, decimal_places=2)


class Tributos(models.Model):
    fk_veiculo = models.ForeignKey(Veiculo)
    is_pago = models.BooleanField("Pago?", default=False)
    taxas_impostos = models.DecimalField(max_digits=8, decimal_places=2)
