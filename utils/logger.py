import utime
from utils.singleton import singleton


@singleton
class Logger:
    def log(self, context, message):
        self._write_log("LOG", context, message)

    def warning(self, context, message):
        self._write_log("WARNING", context, message)

    def error(self, context, message):
        self._write_log("ERROR", context, message)

    def info(self, context, message):
        self._write_log("INFO", context, message)

    def _write_log(self, level, context, message):

        log_message = f"[TIME] [{level}] [{context}] : {message}\n"

        print(log_message, end='\n')

