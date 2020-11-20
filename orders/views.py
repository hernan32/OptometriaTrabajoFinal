from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from orders.models import Order, Product


class OrderList(ListView):
    model = Order


class OrderDetail(DetailView):
    model = Order


class OrderCreation(CreateView):
    model = Order
    success_url = reverse_lazy('orders:list')
    fields = ['patient', 'seller', 'products', 'payment_method']


class OrderUpdate(UpdateView):
    model = Order
    success_url = reverse_lazy('orders:list')
    fields = ['patient', 'seller', 'products', 'payment_method', 'status']

    def get_form(self, form_class=None):
        form = super(OrderUpdate, self).get_form()
        form.fields['patient'].disabled = True
        form.fields['seller'].disabled = True
        form.fields['products'].disabled = True
        form.fields['payment_method'].disabled = True
        return form


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:list')


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class ProductCreation(CreateView):
    model = Product
    success_url = reverse_lazy('orders:catalog')
    fields = ['name', 'price', 'is_glass', 'position', 'type', 'frame']


class ProductUpdate(UpdateView):
    model = Product
    success_url = reverse_lazy('orders:catalog')
    fields = ['name', 'price', 'is_glass', 'position', 'type', 'frame']


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('orders:catalog')

