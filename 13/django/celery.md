##Celery

Redis is an open source, BSD licensed, advanced key-value cache and store. 
It is often referred to as a data structure server since keys can contain 
strings, hashes, lists, sets, sorted sets, bitmaps and hyperloglogs.

Celery is an asynchronous task queue/job queue 
based on distributed message passing.

It is focused on real-time operation, 
but supports scheduling as well.

Celery is used in production systems 
to process millions of tasks a day.

    sudo apt-get install redis
    pip install celery
    pip install django-celery
    pip install redis

    INSTALLED_APPS = ( .. 'djcelery' .. )

    import djcelery
    djcelery.setup_loader()
    BROKER_URL = 'redis://localhost:6379/0'
    ./manage.py celeryd


Make migration

tasks.py

    from celery import task
    from celery.utils.log import get_task_logger
    logger = get_task_logger(__name__)
    logger.setLevel('DEBUG')

    @task(name='save_message')
    def save_message(message):
        logger.info('Save message...')
        message.save()
            logger.info('Success!')

    from main.tasks import save_chat_message
    save_chat_message.delay(message)


./manage.py celeryd --queues=mail --concurrency=1


Celery routing

    CELERY_ROUTES = (CeleryRouter(), )

     class CeleryRouter(object):
         def route_for_task(self, task, args=None, kwargs=None):
             if task == "convertor.tasks.hq_image_from_pdf":
                 return {'queue': 'pdf2image'}
             elif task == 'samsung.tasks.export_samsung':
                 return {'queue': 'samsung'}
             else:
                 # по умолчанию, все остальные задачи обслуживаются очередью
                 # с именем "celery" (достаточно просто сказать None)
                 # мы сюда собираем всю "мелочёвку"
                 return None








