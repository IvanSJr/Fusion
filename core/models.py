from django.db import models
from stdimage.models import StdImageField


# Create your models here.


class Base(models.Model):
    criados = models.DateTimeField('Criação', auto_now_add=True)
    modificado = models.DataTimeField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    # Opções de icones
    icone_choices = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )

    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=300)
    icone = models.CharField('Icone', max_length=12, choices=icone_choices)

    class Meta:
        verbose_name = 'Serviço'
        verbose_plural = 'Serviços'

    def __str__(self):
        return self.servico
