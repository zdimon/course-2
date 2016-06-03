## Parse data

    url_reg = 'https://adminsmssubscriptions.ssl.mts.ru/Users/LogOn?ReturnUrl=%2f'
    l_data = {'Login': 'pressa.ru', 'Password': '***' }
    s = requests.Session()
    r = s.post(url_reg, data=l_data, verify=True)

    url1 = 'https://adminsmssubscriptions.ssl.mts.ru/Contents/EditContent/80149c3a-072f-46f2-b64d-2bc9afeacb98?backurl=%2FContentCategories%2FSearch%2Fb437ceea-b86c-47d4-925a-d5a9e58292c0%3FcontentType%3Dactivecontents%26subscriptionType%3Dcontinuous'
    url2 = 'https://adminsmssubscriptions.ssl.mts.ru/Contents/EditContent/c48fa92e-57c2-4d43-ae0a-d972ae6b915a?backurl=%2FContentCategories%2FSearch%2Fb437ceea-b86c-47d4-925a-d5a9e58292c0%3FcontentType%3Dactivecontents%26subscriptionType%3Dcontinuous'

    q = s.get(url1)
    q2 = s.get(url2)
    y=BeautifulSoup(q.text,"lxml")
    y2=BeautifulSoup(q2.text,"lxml")

    tbl = y.body.findAll("table")[1]
    td = tbl.findAll("td")
    ll = len(td)

    tbl2 = y2.body.findAll("table")[1]
    td2 = tbl2.findAll("td")
    ll2 = len(td)


    cnt1 = td[ll-3].text
    cnt2 = td2[ll2-3].text
