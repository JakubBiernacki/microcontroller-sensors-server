from utils.logger import Logger

logger = Logger()


class EventEmitter:

    def __init__(self):
        self._callbacks = {}

    def on(self, event_name, function):
        self._callbacks[event_name] = function
        logger.info(self, f'listen {event_name} event')
        return function

    def emit(self, event_name, *args, **kwargs):
        function = self._callbacks.get(event_name)

        if function:
            logger.info(self, f'emit {event_name} event')
            function(*args, **kwargs)

    def off(self, event_name):
        self._callbacks[event_name] = None
