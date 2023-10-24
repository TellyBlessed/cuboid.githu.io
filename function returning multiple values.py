Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> [DEBUG ON]
>>> #Calculating volume, surface_area, and perimeter of a Cuboid
def Cuboid(length, width, height):
...   surface_area = 2 *length * 2 * width * 2 * height
...   perimeter = 2 * length + 2 * width + 2 * height
...   volume = length * width * height
...   return surface_area, perimeter, volume
... 
... l, w, h = Cuboid(50, 100, 60)
... print(l, w, h)
... 
