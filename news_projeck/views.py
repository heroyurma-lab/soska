from django.shortcuts import render, get_object_or_404
from .models import News, Category


def home_page_view(request):
    categories = Category.objects.all()
    news = News.objects.filter(status=News.Status.Published).order_by('-published_at')
    latest_news = News.objects.filter(status=News.Status.Published).order_by('-published_at')[:5]
    latest_sport = News.objects.filter(status=News.Status.Published).order_by('-published_at')[:5]

    uzb_news = News.objects.filter(category__name="O‘zbekiston", status=News.Status.Published).order_by(
        '-published_at')[1:5]
    last_uzb_new = News.objects.filter(category__name="O‘zbekiston", status=News.Status.Published).order_by(
        '-published_at').first()

    jahon_news = News.objects.filter(category__name="Jahon", status=News.Status.Published).order_by('-published_at')[
        1:5]
    last_jahon_new = News.objects.filter(category__name="Jahon", status=News.Status.Published).order_by(
        '-published_at').first()

    context = {
        'latest_sport': latest_sport,
        'latest_news': latest_news,
        'jahon_news': jahon_news,
        'last_jahon_new': last_jahon_new,
        'last_uzb_new': last_uzb_new,
        'uzb_news': uzb_news,
        'categories': categories,
        'news': news
    }
    return render(request, 'home.html', context)


def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published).order_by('-published_at')
    return render(request, 'news_list.html', {'news_list': news_list})


def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    return render(request, 'news_detail.html', {'news': news})


def contact_us(request):
    return render(request, 'contact.html')


def about_us(request):
    return render(request, 'about.html')


def page_404(request):
    return render(request, '404.html')