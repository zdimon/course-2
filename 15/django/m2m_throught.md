##Many to many throught


    class CreateUpdateMixin(models.Model):
        create = models.DateTimeField(auto_now_add=True,
                                      verbose_name=u'Дата создания')
        update = models.DateTimeField(auto_now=True,
                                      verbose_name=u'Дата изменения')

        class Meta:
            abstract = True

    class Issue(BasePaperModel, PublicMixin, CreateUpdateMixin):
        errors = models.CharField(verbose_name=_(u'ошибки'),
                                max_length=100, default=' ',
                                  blank=True, null=True)

        customer = models.ManyToManyField('accounts.Customer',
                                          verbose_name=_(u'пользователь'),
                                          through='PurchasedIssues')
    


    class PurchasedIssues(CreateUpdateMixin, models.Model):
        PURCHASED_TYPES = (
            ('mirror', _(u'Разовая покупка c сайта-зеркала')),
            ('once', _(u'Разовая покупка c личного счета')),
            ('subscribe', _(u'Покупка по подписке')),
            ('promorcode', _(u'Покупка по промокоду')),
            ('giftcode', _(u'Покупка по подарочному коду')),
            ('once_add', _(u'Разовая покупка с пополнением счета')),
            ('collection', _(u'Добавление в коллекцию')),
            ('ipad', _(u'Покупка через iPad-приложение')),
            ('add_by_admin', _(u'Добавление в коллекцию администрацией'))
        )
        customer = models.ForeignKey('accounts.Customer',
                                     verbose_name=_(u'пользователь'))
        journal = models.ForeignKey('journal.Journal',
                                    blank=True, null=True,
                                    verbose_name=_(u'издание'))
        issue = models.ForeignKey('journal.Issue',
                                  verbose_name=_(u'печатное издание'))
        purchased_type = models.CharField(verbose_name=_(u'тип покупки'),
                                          choices=PURCHASED_TYPES,
                                          max_length=15)
