class Character:
    def __init__(self):
        self.character_name = ''
        self.path_to_character_file = ''
        self.path_to_character_file_san = ''

    def set_name(self, name):
        self.character_name = name

    def set_path(self, path):
        self.path_to_character_file = path
    
    def get_path(self):
        return self.path_to_character_file

    def get_name(self):
        return self.character_name

    def set_path_san(self, path):
        self.path_to_character_file_san = path

    def get_path_san(self):
        return self.sanitize(self.path_to_character_file_san)

    def sanitize(self, command: str) -> str:
        valid_commands = { 'list' : 'ls', 'stats': 'stat'}
        return valid_commands[command]