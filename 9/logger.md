##Python logger

    import logging

Best practice when instantiating loggers in a library is to only 
create them using the __name__ global variable.

    loger = logging.getLogger(__name__)

There are different importance levels you can use, debug, info, warning, error and critical.


DEBUG: Low level system information for debugging purposes
INFO: General system information
WARNING: Information describing a minor problem that has occurred.
ERROR: Information describing a major problem that has occurred.
CRITICAL: Information describing a critical problem that has occurred.

    logging.basicConfig(level=logging.DEBUG)
    logger.info('Start reading database')

We can use a FileHandler to write records to a file.

    handler = logging.FileHandler('hello.log')
    logger.addHandler(handler)

We can format the records this way using formatter:


    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)



There are different handlers, you can also send records to you mailbox or even a to a 
remote server. You can also write your own custom logging handler. 


    try:
        open('/path/to/does/not/exist', 'rb')
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception, e:
        logger.error('Failed to open file', exc_info=True)




http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python




