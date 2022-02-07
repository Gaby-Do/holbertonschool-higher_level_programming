#!/usr/bin/python3
"""
10. And now, the Square!
Write the class Square that inherits from Rectangle
"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size: (int > 0) side of the rectangle
            x and y: int >= 0
            id: id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {super().width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        list_args = ['id', 'size', 'x', 'y']
        if args:
            if len(args) < 5:
                for i in range(len(args)):
                    setattr(self, list_args[i], args[i])
        elif kwargs:
            for key in kwargs:
                if key in list_args:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        sq_dict = {
                    'id': self.id,
                    'x': self.x,
                    'size': self.size,
                    'y': self.y
                    }
        return sq_dict
