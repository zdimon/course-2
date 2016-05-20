##What's in an HTTP request?

HTTP is a request/response protocol, which means your computer sends a request for some file (e.g. "Get me the file 'home.html'"), and the web server sends back a response


##Two HTTP Request Methods: GET and POST


    GET - Requests data from a specified resource
    POST - Submits data to be processed to a specified resource

###The GET Method

    http://mysite.com?name1=value1&name2=value

Note that the query string (name/value pairs) is sent in the URL of a GET request.


Some other notes on GET requests:

-GET requests can be cached
-GET requests remain in the browser history
-GET requests can be bookmarked
-GET requests should never be used when dealing with sensitive data
-GET requests have length restrictions
-GET requests should be used only to retrieve data

##The POST Method

    POST /test/demo_form.asp HTTP/1.1
    Host: w3schools.com
    name1=value1&name2=value2

Note that the query string (name/value pairs) is sent in the HTTP message body of a POST request:

    POST requests are never cached
    POST requests do not remain in the browser history
    POST requests cannot be bookmarked
    POST requests have no restrictions on data length



##Requests library

Requests is the only Non-GMO HTTP library for Python, safe for human consumption.

    import requests
    r = requests.get('http://yandex.ru')
    #Now, we have a Response object called r.
    print r.status_code

###Outputs

    200


    r = requests.get('http://yandex.ru')
    print r.text

###Outputs

    <!DOCTYPE html><html class="i-ua_js_no i-ua_css_standart i-ua_browser_unknown i-ua_browser_desktop i-ua_platform_other" lang="uk"><head xmlns:og="http://ogp.me/ns#"><meta http-equiv="X-UA-Compatible" content="IE=edge"><title>Яндекс.....


    r = requests.post('http://httpbin.org/post', data = {'key':'value'})


    r = requests.put('http://httpbin.org/put', data = {'key':'value'})
    r = requests.delete('http://httpbin.org/delete')
    r = requests.head('http://httpbin.org/get')
    r = requests.options('http://httpbin.org/get')


##Passing Parameters In URLs

Requests allows you to provide your arguments as a dictionary, using the params keyword argument.

    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('http://httpbin.org/get', params=payload)
    # http://httpbin.org/get?key1=value1&key2=value2
    

## POST request

    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://httpbin.org/post", data=payload)


##POST a Multipart-Encoded File

Requests makes it simple to upload files.

    url = 'http://httpbin.org/post'
    files = {'file': open('report.xls', 'rb')}
    r = requests.post(url, files=files)


##Timeouts

    import requests
    from subprocess import call
    import time

    while True:
        time.sleep(30) 
        try:
            rez = requests.get('http://mysite.com',timeout=5)
        except:
            call('reload_server.sh')




http://docs.python-requests.org/en/master/



