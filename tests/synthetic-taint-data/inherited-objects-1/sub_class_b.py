from super_class import super_class

class sub_class_b(super_class):
    def __init__(self):
        super().__init__()
    
    def get_info(self):
        return self.path