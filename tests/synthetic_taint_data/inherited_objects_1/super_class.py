class SuperClass:
    def set_command(self, command):
        self.command = command
        
    def get_command(self):
        return self.command
    
    def evaluate_command(self):
        raise NotImplementedError('Please implement before use.')
    