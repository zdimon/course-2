## Optional url

    url(r'^(?P<journal_type>magazines|newspapers|books|abonement)/new$',
        CategoryByCriterionView.as_view(),


    url(r'^(?P<name_slug>[-\w]+)/subscribe/(?P<pk>\d+)/buy$',
        JournalBuySubscribeView.as_view(), name="journal-buy-subscribe"),
