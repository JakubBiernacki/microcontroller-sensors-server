from utils.singleton import singleton


@singleton
class Config:
    def __init__(self, file_path='.env'):
        self.file_path = file_path
        self._env = {}

        self.map_file_to_dict()

    def map_file_to_dict(self):
        with open(self.file_path, 'r') as file:
            for line in file.readlines():
                key, value = line.split('=')
                self._env[key] = value.strip()

    def get(self, key):
        return self._env.get(key)

