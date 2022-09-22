from importlib.resources import path


class SuperClass:
    def set_path(self):
        self.path = path
        
    def get_info(self):
        raise NotImplementedError('Please implement before use.')