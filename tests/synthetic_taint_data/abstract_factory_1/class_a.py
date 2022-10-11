class ClassA:
    def __init__(self):
        self.command = ''

    def get_command(self):
        return self.command

    def set_command(self, command):
        self.command = command

    def get_command_sanitized(self):
        return self.sanitize(self.command)

    def sanitize(self, command: str) -> str:
        valid_commands = { 'list' : 'ls', 'stats': 'stat'}
        return valid_commands[command]