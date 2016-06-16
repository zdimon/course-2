##Delete images

    class ArticleImages(models.Model):
        article = models.ForeignKey('Article')
        image  = models.ImageField(upload_to=get_upload_path, verbose_name=u'Изображение')
        def delete(self, *args, **kwargs):
            self.image.delete()
            super(ArticleImages, self).delete(*args, **kwargs)
