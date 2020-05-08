from django.shortcuts import render, HttpResponseRedirect, reverse

from .models import Article
from datetime import datetime
import locale


# Create your views here.


def details(request):
    try:
        all_articles = Article.objects.all()[::-1][1:]
        last_article = Article.objects.all().order_by('-id')[0]
    except:
        return render(request, 'articles.html')

    return render(request, 'articles.html', {'all_articles': all_articles, 'last_article': last_article})


def add_article(request):
    locale.setlocale(locale.LC_ALL, "ru")
    try:
        Article.objects.create(article_meta=request.POST['article-meta'],
                               article_title=request.POST['article-title'],
                               article_text=request.POST['article-text'],
                               pub_date=datetime.today().strftime("%d %B %Y %H:%M"),
                               article_image=request.FILES['article-image'])
    except:
        return render(request, 'new_article.html')
    return HttpResponseRedirect(reverse('articles:details'))
