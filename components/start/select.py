class Select:
    def __init__(self, options):
        self.options = options
        self.current_index = 0
        
    def get_current_option(self):
        return self.options[self.current_index]
    
    def left(self):
        self.current_index = (self.current_index - 1) % len(self.options)
    
    def right(self):
        self.current_index = (self.current_index + 1) % len(self.options)