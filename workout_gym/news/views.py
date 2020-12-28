from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-pub_date')
    news_paginator = Paginator(news, 3)
    page_num = request.GET.get('page')
    page = news_paginator.get_page(page_num)
    contex = {
        'count': news_paginator.count,
        'page': page
    }
    return render(request, 'news/news_home.html', contex)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'


def create(request):
    error = " "
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Some ERROR'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
