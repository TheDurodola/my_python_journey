class InvalidNameError(ValueError):


    def __init__(self, message="Name cannot be empty or contain only whitespace."):
        self.message = message
        super().__init__(self.message)