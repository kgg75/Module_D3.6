from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post, Comment


class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    #ordering = 'rating'
    ordering = '-datetime'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        #context['next_sale'] = None
        return context


class PostDetail(DetailView):
    model = Post    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    template_name = 'one_post.html'    # Используем другой шаблон
    context_object_name = 'one_post'    # Название объекта, в котором будет выбранная пользователем новость
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object.id)
        return context