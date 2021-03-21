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


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=45)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)  # chave estrangueira de Cargo
    bio = models.TextField('Biografia', max_length=300)
    imagem = StdImageField('Imagem', upload_to='equipe', variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instragram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'funcionário'
        verbose_plural = 'funcionários'

    def __str__(self):
        return self.nome