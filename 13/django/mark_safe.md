##Mark safe

    from django.utils.safestring import mark_safe
    @property
    def get_cover(self):
        try:
            return mark_safe('<img src="%s" />' % self.cover.url)
        except:
            return mark_safe('<img src="%s" />' % '/media/journal_cover/plug.jpg')

