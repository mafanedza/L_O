def triangle_area(side1,side2,side3):
    semi_parameter = (side1 + side2 + side3) / 2
    area = (semi_parameter*(semi_parameter-side1)*(semi_parameter-side2)*(semi_parameter-side3)) ** 0.5
    return area
print(triangle_area(12,16,20))
