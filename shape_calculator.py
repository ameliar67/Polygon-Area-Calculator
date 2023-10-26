import math

class Rectangle():
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

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
    if self.height > 50:
      return("Too big for picture.")
    if self.width > 50:
      return("Too big for picture.")
    
    str = "*" * self.width + '''
'''
    
    i = 1
    while i < self.height:
      str = str + "*" * self.width + '''
'''
      i = i + 1

    return str

  def get_amount_inside(self, shape):
    area_shape = shape.get_area()
    area = self.get_area()

    if area_shape > area:
      return 0
    else:
      num = area / area_shape
      return math.floor(num)


class Square(Rectangle):
  def __init__(self, side_length):
    self.width = side_length
    self.height = side_length

  def __str__(self):
    return 'Square(side=' + str(self.width) + ')'

  def set_side(self, side):
    self.width = side
    self.height = side