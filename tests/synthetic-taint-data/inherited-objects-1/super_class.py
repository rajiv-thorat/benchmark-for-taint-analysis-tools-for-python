from importlib.resources import path


class super_class:
    def set_path(self):
        self.path = path
        
    def get_info(self):
        raise NotImplementedError('Please implement before use.')