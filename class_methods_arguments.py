class Circle:
    pi = 3.14
    def area(self, radius):
        area = Circle.pi * radius ** 2
        return area
circle = Circle()
pizza_area = circle.area(12 / 2)
print("pizza area is ",pizza_area)
teaching_table_area = circle.area(36 / 2)
print("teaching table area is ",teaching_table_area)
round_room_area = circle.area(11460 / 2)
print("round room area is ",round_room_area)
# Path: class_methods_arguments.py
print(pizza_area, teaching_table_area, round_room_area)