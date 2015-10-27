from django.views.generic import ListView, DetailView
from .models import Produto


class HomeView(ListView):
    template_name = 'home.html'
    paginate_by = 9

    def get_queryset(self):
        return Produto.objects.filter(destaque=True)


class ProdutoView(DetailView):
    template_name = 'product_detail.html'
    model = Produto
    context_object_name = 'produto'
