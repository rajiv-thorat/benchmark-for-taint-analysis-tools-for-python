class Character:
    def __init__(self):
        self.character_name = ''
        self.path_to_character_file = ''
        pass

    def set_name(self, name):
        self.character_name = name

    def set_path(self, path):
        self.path_to_character_file = path
    
    def get_path(self):
        return self.path_to_character_file

    def get_name(self):
        return self.character_name