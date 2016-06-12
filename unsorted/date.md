##Date manipulation

    from datetime import datetime
    from dateutil.relativedelta import relativedelta


    _date = datetime.today()+ relativedelta(days=7)

    _date = datetime.today()+ relativedelta(months=1)

    _date.strftime('%Y-%m-%d')

