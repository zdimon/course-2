## Queries

issue_ids = Model.objects.filter(customer=user).values_list('issue', flat=True)

Issue.objects.filter(id__in=issue_ids).filter(**self.kwargs)


