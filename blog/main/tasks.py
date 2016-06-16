from celery import task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)
logger.setLevel('DEBUG')
import time


@task(name='save_message')
def save_message():
    logger.info('Save message...')
    for i in range(5):
        logger.info('Success! %s' % i)
        print 'Success! %s' % i
        time.sleep(5)


@task(name='send_message')
def send_message():
    logger.info('send_message message...')
    for i in range(5):
        logger.info('send_message! %s' % i)
        print 'send_message! %s' % i
        time.sleep(5)
