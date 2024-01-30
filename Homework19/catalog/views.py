from PIL import Image
from django.forms import formset_factory, inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View

from catalog.forms import ProductForm, VersionForm
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from catalog.models import Product, Contact, Version
from catalog.services import get_categories


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = "main/index.html"
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = get_categories()
        products = [product for product in Product.objects.all() if product.is_published][:6]

        for product in products:
            product.active_versions = product.versions.filter(is_active=True).first()

        context['products'] = products
        context['categories'] = categories
        return context


class ContactListView(ListView):
    model = Contact
    template_name = "main/contacts.html"
    context_object_name = "adress_info"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context

    def post(self, request, *args, **kwargs):
        country = request.POST.get('country')
        inn = request.POST.get('inn')
        address = request.POST.get('address')
        print(f'{country}\n{inn}\n{address}')
        contact_obj = Contact(country=country, inn=inn, address=address)
        contact_obj.save()
        return self.get(request, *args, **kwargs)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_card.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О товаре'
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

class VersionListView(ListView):
    model = Version
    form_class = VersionForm


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self, *args, **kwargs):
        product_pk = Product.objects.get(pk=self.kwargs.get('pk'))
        return reverse('catalog:version_list', args=[product_pk.pk])