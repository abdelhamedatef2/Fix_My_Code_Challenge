#!/usr/bin/python3

class Square:
    """
    class represent square shape.
    
    Attrs:
    - width: width of square.
    - height: height of square.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes square with given width and height.
        
        Args:
        - width: width of square.
        - height: height of square.
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """
        Calculate area of square.
        
        Returns:
        area of square.
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Calculate perimeter of square.
        
        Returns:
        perimeter of square.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returns str represent square.
        
        Returns:
        str represent square in format 'width/height'.
        """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
