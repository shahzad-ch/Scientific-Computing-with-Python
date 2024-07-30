class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        output = ''
        for i in range(self.height):
            output += '*' * self.width + '\n'
        return output
    
    def get_amount_inside(self, other):
        h = self.height // other.height
        w = self.width // other.width
        return h*w

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def __str__(self):
        return f'{self.__class__.__name__}(side={self.height})'
    def set_side(self, side):
        self.__init__(side)
    def set_height(self, height):
        self.set_side(height)
    def set_width(self, width):
        self.set_side(width)

rect = Rectangle(16, 8)
rect.get_area()
print(rect)
print(rect.get_picture())

sq = Square(4)
print(sq.get_picture())
print(sq)
sq.set_height(2)
print(sq)
