##Template language

    {% for story in story_list %}
    <h2>
      <a href="{{ story.get_absolute_url }}">
        {{ story.headline|upper }}
      </a>
    </h2>
    <p>{{ story.tease|truncatewords:"100" }}</p>
    {% endfor %}


    {{ value|default:"nothing" }}


    {% if athlete_list %}
        Number of athletes: {{ athlete_list|length }}
    {% elif athlete_in_locker_room_list %}
        Athletes should be out of the locker room soon!
    {% else %}
        No athletes.
    {% endif %}


    {{ data|safe }}

    {% autoescape off %}
        Hello {{ name }}
    {% endautoescape %}



    {% for comment in task.comment_set.all %}
        {{ comment }}
    {% endfor %}


    class Task(models.Model):
        def foo(self):
            return "bar"

    {{ task.foo }}


    {% load humanize %}

    {{ 45,000|intcomma }}

    {% load humanize i18n %}

{% mytag %}







