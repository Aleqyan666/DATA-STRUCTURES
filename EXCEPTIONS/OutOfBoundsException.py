class OutOfBoundsException(Exception):
    """Custom exception when an index or value is out of bounds."""
    
    def __init__(self, index):
        self.message = f"Index '{index}' is out of bounds." 
        super().__init__(self.message) 