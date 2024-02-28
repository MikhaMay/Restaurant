from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, string):
        pass
    
class ConsoleLogger(Logger):
    def log(self, string):
        print(string)

class FileLogger(Logger):
    def __init__(self, filename = 'output.txt'):
        self._filename = filename

    def log(self, string):
        with open(self._filename, 'a') as f:
            f.write(string)

class LogManager:
    _instance = None
    _logger = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def set_logger(self, new_logger):
        self._logger = new_logger
    
    def log(self, string):
        if not self._logger:
            return
        self._logger.log(string)

    @staticmethod
    def log_message(string):
        if not LogManager._instance:
            LogManager._instance = LogManager()
        LogManager._instance.log(string)