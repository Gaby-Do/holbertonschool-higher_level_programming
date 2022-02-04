#!/usr/bin/python3
"""
2. First Rectangle
Write the class Rectangle that inherits from Base
"""


from models.base import Base
"""importing class base"""


class Rectangle(Base):
    """
    class Rectangle inherits from Base
    """

    err_type_msg = "must be an integer"
    err_val_msg = "must be > 0"

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Args:
                width and height: int, sides of rectangle
                x and y: has no function yet
                id: id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        

    @property
    def width(self):
        """retrieve width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width
            Arg:
                value: must be int >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        area = self.__width * self.__height
        return area

    """
    def display(self):
        for h in range(self.__height):
            for w in range(self.__width):
                print('#', end='')
            print()
    """    
    def __str__(self):
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    def display(self):
        for x in range(self.__x):
            print()
        for h in range(self.__height):
            for y in range(self.__y):
                print(' ', end='')
            for w in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        list_args = ['id', 'width', 'height', 'x', 'y']
        if args:
            if len(args) < 6:
                for i in range(len(args)):
                    setattr(self, list_args[i], args[i])
        else:
            if kwargs:
                for key in kwargs:
                    if key in list_args:
                        setattr(self, key, kwargs[key])

