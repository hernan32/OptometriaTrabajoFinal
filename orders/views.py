from django.db.models import Q, Count
from django.forms import DateInput
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, MonthArchiveView, \
    WeekArchiveView

from orders.models import Order, Product


class OrderList(ListView):
    model = Order


class OrderDetail(DetailView):
    model = Order


class OrderCreation(CreateView):
    model = Order
    success_url = reverse_lazy('orders:list')
    fields = ['patient', 'products', 'date', 'payment_method']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        """add date picker in forms"""
        form = super(OrderCreation, self).get_form()
        form.fields['date'].widget = DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        return form


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


class WorkShopList(ListView):
    model = Order
    template_name_suffix = '_workshop_list'

    def get_queryset(self):
        new_context = Order.objects.filter(Q(status='FIN') | Q(status='TAL')).order_by('status')
        return new_context


class WorkShopDetail(DetailView):
    model = Order
    template_name_suffix = '_workshop_detail'


class WorkShopUpdate(UpdateView):
    model = Order
    success_url = reverse_lazy('orders:workshop_list')
    template_name_suffix = '_workshop_form'
    fields = ['patient', 'seller', 'status']

    def get_form(self, form_class=None):
        form = super(WorkShopUpdate, self).get_form()
        form.fields['patient'].disabled = True
        form.fields['seller'].disabled = True
        return form


class OverviewProductList(ListView):
    model = Product
    template_name_suffix = "_overview"


class OverviewOrderList(ListView):
    model = Order
    template_name_suffix = "_overview"


class PatientsWithOrdersByMonth(MonthArchiveView):
    queryset = Order.objects.all()
    date_field = "date"
    allow_future = True
    allow_empty = True
    template_name_suffix = '_report_by_month'

    def get_queryset(self):
        return self.queryset.values('patient').annotate(Count('patient'))


class PatientsWithOrdersByWeek(WeekArchiveView):
    queryset = Order.objects.all()
    date_field = "date"
    week_format = "%W"
    allow_future = True
    allow_empty = True
    template_name_suffix = '_report_by_week'

    def get_queryset(self):
        return self.queryset.values('patient').annotate(Count('patient'))


class BestSellerByMonth(MonthArchiveView):
    queryset = Order.objects.all()
    date_field = "date"
    allow_future = True
    allow_empty = True

    def get_template_names(self):
        return ['orders/product_report_by_month.html']

    def get_queryset(self):
        return self.queryset.values('products__name') \
            .annotate(Count('products__name')).order_by('-products__name__count')


class BestSalesByMonth(MonthArchiveView):
    queryset = Order.objects.all()
    date_field = "date"
    allow_future = True
    allow_empty = True

    def get_template_names(self):
        return ['orders/product_sales_report_by_month.html']

    def get_queryset(self):
        return self.queryset.values('seller__first_name')\
            .annotate(Count('seller__first_name')).order_by('-seller__first_name__count')
