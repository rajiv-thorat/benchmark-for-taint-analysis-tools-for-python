from super_class import SuperClass


class SubClassA(SuperClass):
    def __init__(self):
        super().__init__()

    def get_info(self):
        return 'test'