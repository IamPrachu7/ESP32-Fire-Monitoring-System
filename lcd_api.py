class LcdApi:
    def __init__(self, num_lines, num_columns):
        self.num_lines = num_lines
        self.num_columns = num_columns
    def clear(self): pass
    def move_to(self, col, row): pass
    def putstr(self, string): pass
