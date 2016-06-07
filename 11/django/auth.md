##Authentication

                {% if user.is_authenticated %}
                    hello {{ user.username }}
                {% else %}
        
                {% if form.non_field_errors %}
                <ul class='errorlist'>
                    {% for error in form.non_field_errors %}
                        <li>{{ error }}</li>
                    {% endfor %}
                </ul>
                {% endif %}        

                <form method="post" action="{% url 'django.contrib.auth.views.login' %}">
                        {% csrf_token %}
                        <h2> {% trans 'Enter' %} </h2>
      
                        <input name="username" type="text"  placeholder="{% trans 'Login' %}">
                   
                        <input type="password" name="password"   placeholder="{% trans "Password" %}">
                    
                        <button type="submit" >{% trans "Enter" %}</button>
                                                                            
                </form>
                   
         
               {% endif %}

###Routing

     url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}, name='logout'),
     url(r'^login/$', 'django.contrib.auth.views.login', name='login'),



