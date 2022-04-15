from itertools import chain

from django.views.generic import TemplateView, ListView

from ProjectSoftUni.main_app.models import Recipe, Product, Course


class HomePageView(TemplateView):
    template_name = 'main/general/home.html'


class AboutPageView(TemplateView):
    template_name = 'main/general/about.html'


class SearchView(ListView):
    template_name = 'main/general/search.html'
    model = (Recipe, Product, Course)
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('searched').lower()

        # When user submits empty search.
        if query == '':
            return None

        recipes = Recipe.objects.filter(title__contains=query)
        products = Product.objects.filter(name__contains=query)
        courses = Course.objects.filter(name__contains=query)

        # When there is no result.
        if len(recipes) == 0\
            and len(products) == 0\
                and len(courses) == 0:
            return None

        object_list = chain(recipes, products, courses)
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['searched'] = self.request.GET.get('searched')
        return context
