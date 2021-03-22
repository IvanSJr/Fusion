from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Servico, Funcionario, Recurso
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    # Context Manager
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        recursos = Recurso.objects.order_by('?').all()  # retorna objetos em ordem aleatoria e armazena na variável
        c = recursos.count()  # retorna a quantidade de objetos
        context["recursos1"] = recursos[:c//2]  # lado esquerdo do layout
        context["recursos2"] = recursos[c//2:c]  # lado direito do layout
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Ocorreu um erro ao enviar o email!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)