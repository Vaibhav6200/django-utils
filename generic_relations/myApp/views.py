from django.shortcuts import render
from .models import *


def index(request):
    p1 = Publication.objects.get(id=1)
    p2 = Publication.objects.get(id=2)
    p3 = Publication.objects.get(id=3)

    a1 = Article.objects.get(id=1)

    # Quering ManyToMany in individual Instance
    # all_publications_of_a1 = a1.publications.all()
    # all_articles_in_p1 = p1.article_set.all()
    # print(all_articles_in_p1)
    # print(all_publications_of_a1)

    # Quering ManyToMany in whole Model
    # Filtering all articles belonging to publication id = 1
    # req_articles = Article.objects.filter(publications__id=1)
    # req_articles = Article.objects.filter(publications__pk=1)
    # req_articles = Article.objects.filter(publications=1)
    # req_articles = Article.objects.filter(publications=p1)
    # req_publications = Publication.objects.filter(article=2)

    # print(req_articles)
    # print(req_publications)


    # Adding via another end of an m2m
    # a4 = Article(headline="NASA finds intelligent life on Earth")
    # a4.save()
    # p3.article_set.add(a4)
    # print(a4.publications.all() )

    # a4 = Article.objects.get(id=6)
    # a4.publications.remove(p3)
    # print(a4.publications.all())

    # p3.article_set.remove(a4)
    # print(p3.article_set.all())

    # set Article to another publication
    # print(a4.publications.all())
    # a4.publications.set([p2])
    # print(a4.publications.all())


    # Clear complete relation set
    # a4.publications.clear()


    # Bulk Delete
    # Publication.objects.filter(title__startswith="Science").delete()


    # p4 = Publication.objects.create(title="Aaj Tak News")
    # a5 = Article(headline="shootout at lucknow")
    # a5.save()
    # a5.publications.add(p4)



    return render(request, 'index.html')