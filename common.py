"""
Common objects used throughout.
"""

class FGItemDescriptor:
    def __init__(self,
                 class_name: str,
                 display_name: str,
                 description: str):
        self.class_name = class_name
        self.display_name = display_name
        self.description = description

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'ff{self.__class__}'

