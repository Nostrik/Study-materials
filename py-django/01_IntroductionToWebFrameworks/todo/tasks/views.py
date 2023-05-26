from django.http import HttpResponse

from django.views import View
import random

class ToDoView(View):
    
    def get(self, request, *args, **kwargs):
        list_deals = ['Установить python', 'Установить django', 'Запустить сервер', 'Порадоваться результату', 'Добавить 5й элемент']
        random.shuffle(list_deals)
        list_2 = []
        for element in list_deals:
            elem = f'<li>{element}</li>'
            list_2.append(elem)
        list_deals = ''.join(list_2)
        final_list = f'<ul>{list_deals}</ul>'
        return HttpResponse(final_list)
