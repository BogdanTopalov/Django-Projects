from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView

from ProjectSoftUni.main_app.forms import EditProductForm, AddProductForm
from ProjectSoftUni.main_app.models import Product

from ProjectSoftUni.common.custom_mixins import StaffRequiredMixin

from django.urls import reverse_lazy


class ProductsDashboardView(ListView):
    model = Product
    template_name = 'main/product/products_dashboard.html'
    context_object_name = 'products'


class ShowProductView(DetailView):
    model = Product
    template_name = 'main/product/show_product.html'
    context_object_name = 'product'


class CreateProductView(StaffRequiredMixin, CreateView):
    model = Product
    form_class = AddProductForm
    template_name = 'main/product/add_product.html'
    permission_required = 'main_app.add_product'

    # Go to the created product page.
    def get_success_url(self):
        return reverse_lazy('show product page', kwargs={'pk': self.object.pk})


class EditProductView(StaffRequiredMixin, UpdateView):
    model = Product
    form_class = EditProductForm
    template_name = 'main/product/edit_product.html'
    permission_required = 'main_app.change_product'

    # Return to the same product page.
    def get_success_url(self):
        return reverse_lazy('show product page', kwargs={'pk': self.object.pk})


class DeleteProductView(StaffRequiredMixin, DeleteView):
    model = Product
    template_name = 'main/product/delete_product.html'
    permission_required = 'main_app.delete_product'

    # Return to product dashboard page after deletion.
    def get_success_url(self):
        return reverse_lazy('product dashboard page')
