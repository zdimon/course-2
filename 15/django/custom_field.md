##Custom field

    import os
    from django.db.models.fields.files import FileField



    class JournalFileField(FileField):

        def __init__(self, *args, **kwargs):
            self.default_name = kwargs.pop('default_name', False)
            self.prefix = kwargs.pop('prefix','')
            kwargs['max_length'] = 255
            super(JournalFileField, self).__init__(*args, **kwargs)

        def generate_filename(self, instance, filename):
            paper_slug = instance.name_slug
            paper_year = "%s" % instance.release_date.year
            journal_slug = instance.journal.name_slug
            publishing_office_slug = instance.journal.publishing_office.name_slug
            if self.default_name and filename != '':
                # filename = '' used for getting files directory
                filename = "{0}-{1}-{2}.pdf".format(journal_slug,
                                                    paper_year,
                                                    paper_slug)
            return os.path.join(self.prefix,
                                journal_slug,
                                paper_year,
                                paper_slug,
                                self.get_directory_name(),
                                self.get_filename(filename))



    class SwfPage(models.Model):
        paper = models.ForeignKey(Issue,
                                  verbose_name=_(u'печатное издание'),
                                  related_name='page_set_swf')
        page = models.PositiveIntegerField(verbose_name=_(u'номер страницы'))
        preview = JournalFileField(
            verbose_name=_(u'файл изображения предпросмотра'),
            upload_to='swf/low',
            prefix='private',
            blank=True, null=True)
        image = JournalFileField(
            verbose_name=_(u'файл страницы'),
            upload_to='swf',
            prefix='private')




    class Tier(models.Model):
        name = models.CharField(verbose_name=_(u'наименование tier-а (код цены) в App Store'),
                                max_length=20)
        cost_from = AmountField()
        cost_to = AmountField()


    class AmountField(models.DecimalField):
        def __init__(self, *args, **kwargs):
            kwargs['max_digits'] = 12
            kwargs['decimal_places'] = 2
            super(AmountField, self).__init__(*args, **kwargs)


