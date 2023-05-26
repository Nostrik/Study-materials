from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from advertisements.models import Advertisement


def advertisement_list(request,  *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisement/advertisement.html', {
        'advertisement': advertisements
    })


def categories(request,  *args, **kwargs):
    cats = ['Личные вещи', 'Транспорт', 'Хобби', 'Отдых']
    return render(request, 'categories/categories.html', {'categories': cats})


def regions(request,  *args, **kwargs):
    reg = ['Москва', 'Московская область', 'республика Алтай', 'Вологодская область']
    return render(request, 'regions/regions.html', {'regions': reg})


class Regions(View):
    reg = ['Москва', 'Московская область', 'республика Алтай', 'Вологодская область']

    def get(self, request):
        return render(request, 'regions/regions.html', {'regions': self.reg})

    def post(self, request):
        return HttpResponse(
            '<p>Регион успешно создан</p>'
        )


class About(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'БеСплатные объявления в вашем городе'
        context['title'] = 'БеСплатные объвяления'
        context['description'] = """
        lorem ipsum dolore
        """
        return context


class Contacts(TemplateView):
    template_name = 'contacts/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = 'tel: 8-800-708-19-45\nemail: sales@company.com'
        return context


class Advertisements(View):
    request_count = 0
    adlist_1 = [
        'Личные вещи',
        'Транспорт',
        'Работа'
    ]
    adlist_2 = [
        'Запчасти и аксесуары',
        'Для дома и дачи',
        'Недвижимость'
    ]
    adlist_3 = [
        'Предложение услуг',
        'Хобби и отдых',
        'Электроника'
    ]

    def get(self, request):
        Advertisements.request_count += 1
        return render(request, 'advertisement/advertisement_list.html', {'adlist1': self.adlist_1,
                                                                          'adlist2': self.adlist_2,
                                                                          'adlist3': self.adlist_3,
                                                                          'count': Advertisements.request_count})

    def post(self, request):
        return render(request, 'advertisement/test_post.html', {})


class HomePage(TemplateView):
    template_name = 'home_page/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_1'] = Advertisements.adlist_1[0]
        context['category_2'] = Advertisements.adlist_1[1]
        context['category_3'] = Advertisements.adlist_1[2]
        context['category_4'] = Advertisements.adlist_2[0]
        context['category_5'] = Advertisements.adlist_2[1]
        context['category_6'] = Advertisements.adlist_2[2]
        context['category_7'] = Advertisements.adlist_3[0]
        context['category_8'] = Advertisements.adlist_3[1]
        context['category_9'] = Advertisements.adlist_3[2]
        context['region_1'] = Regions.reg[0]
        context['region_2'] = Regions.reg[1]
        context['region_3'] = Regions.reg[2]
        context['region_4'] = Regions.reg[3]
        return context


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]
