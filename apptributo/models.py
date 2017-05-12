from django.db import models

# Create your models here.


class Pessoa(models.Model):
	pessoa_cpf = models.CharField(max_length=15)
	pessoa_nome = models.CharField(max_length=60)

	#def __str__(self):
		#return self.pessoa_nome


class Veiculo(models.Model):
	fk_pessoa = models.ForeignKey(Pessoa)
	veiculo_placa = models.CharField(max_length=7)
	veiculo_preco_fipe = models.CharField(max_length=10)


class Tributos(models.Model):
	fk_veiculo = models.ForeignKey(Veiculo)
	is_pago = models.BooleanField("Pago?")
	taxas_impostos= models.DecimalField(max_digits=5, decimal_places= 2)