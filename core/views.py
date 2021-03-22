from django.views.generic import TemplateView
from .models import Servico, Funcionario, Recurso


class IndexView(TemplateView):
    template_name = 'index.html'

    # Context Manager
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        recursos = Recurso.objects.order_by('?').all()  # retorna objetos em ordem aleatoria e armazena na variável
        c = recursos.count()  # retorna a quantidade views
        context["recursos1"] = recursos[:c//2]  # lado esquerdo do layout
        context["recursos2"] = recursos[c//2:c]  # lado direito do layout
        return context
