## Many to many manipulation

    class Category(models.Model):    
        ...

    class Article(models.Model):
        ....
        category = models.ManyToManyField('catalog.Category',
                                          blank=True,
                                          verbose_name=_(u'Категории в Pressa.ru'))


###Retrieving 

    obj.category.all()

    category_obj.article_set.all()

    Category.objects.get(id=4).article_set.all()

Many-to-many relationships can be queried using lookups across relationships:

    Article.objects.filter(category__id=1)
    Article.objects.filter(category__pk=1)
    Article.objects.filter(category=1)
    Article.objects.filter(category=cat1)


The count() function respects distinct() as well:

    Article.objects.filter(category__title__startswith="Science").count()
    Article.objects.filter(category__title__startswith="Science").distinct().count()

    Category.objects.filter(article__in=[1,2]).distinct()

###Deleting

    a.category.through.objects.all().delete()
    for c in b['categories']:
        cat = Category.objects.get(pk=c['id'])
        a.category.add(cat)

    cat2.article_set.clear()

    a4.category.remove(c2)


###Multiply adding

    obj.category.add(p1, p2)


###Filtering

    q = Article.objects.filter(pk>2)
    q.filter(...).filter(...)

