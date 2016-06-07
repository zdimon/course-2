##Forms

At the heart of this system of components is Django’s Form class.
In much the same way that a Django model.
A form field is represented to a user in the browser as an HTML “widget”.
Each field type has an appropriate default 
Widget class, but these can be overridden as required.



    <form action="/your-name/" method="post">
        <label for="your_name">Your name: </label>
        <input id="your_name" type="text" name="your_name" value="{{ current_name }}">
        <input type="submit" value="OK">
    </form>


###Building a form in Django

    from django import forms

    class NameForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)


###The view

    form = NameForm()
    context = {.....'form': form}


### The template

    <h2> My form </h2>

    {{ form }}

Resulting code.

    <tr>
        <th><label for="id_your_name">Your name:</label></th>
        <td><input id="id_your_name" maxlength="100" name="your_name" type="text" /></td>
    </tr>

Compleate template.


    <h2> My form </h2>

    <form action="/" method="POST">
        {% csrf_token %}
        <table border=1>
            {{ form }}
            <tr>
                <td> <input type="submit" name="Go"> </td>
            </tr>
        </table>
    </form>

More field

    class NameForm(forms.Form):
        ...
        sender = forms.EmailField()

Handle the request


    def home_page(request):
        ...
        
        message = ''
        if request.method == 'POST':
            form = NameForm(request.POST)
            if form.is_valid():
                message = 'Well'
            else:
                message = 'Some error!!!'
        else:        
            form = NameForm()
        context = {'name': 'Dima', 'm': m, 'form': form, 'message': message}
        return render_to_response('main/home.html', context, RequestContext(request))


Change template to show message and manage language.

    {% extends 'base.html' %}
    {% load i18n %}
    {% get_current_language as LANGUAGE_CODE %} 

    
    {% block content %}

  
        <h2> My form </h2>
        <h3>{{ message }}</h3>
        <form action="/{{ LANGUAGE_CODE }}/" method="POST">
            {% csrf_token %}
            <table border=1>
                {{ form }}
                <tr>
                    <td> <input type="submit" name="Go"> </td>
                </tr>
            </table>

        </form>

Get values from view.

        ....
        if form.is_valid():
            print 'I got %s' % form.cleaned_data['your_name']    
        ...

Redirect after submiting.

        if form.is_valid():
            .....
            return HttpResponseRedirect('/'+request.LANGUAGE_CODE+'/')

###Save method

    class NameForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)
        sender = forms.EmailField()
        def save(self):
           data = self.cleaned_data
           print data  

###Model form

    class User(models.Model):
        surname = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Surname')
        name = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Name')
        phone = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'Phone')
        email = models.EmailField(verbose_name=u'Email')


    from django.forms import ModelForm
    from main.models import User

    class NameForm(ModelForm):
        class Meta:
            model = User
            fields = '__all__'


Creating a form to change an existing article.

    article = Article.objects.get(pk=1)
    form = ArticleForm(instance=article)

Customizing

    class BookForm(forms.Form):
        .....
        authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())










