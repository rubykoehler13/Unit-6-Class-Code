import math
# Slope: (y2-y1)/(x2-x1) --> (x1, y1), (x2, y2)
def slope(point1,point2):
   slope_formula = (point2[1]-point1[1])/(point2[0]-point1[0])
   return slope_formula

# Distance: sqrt((x2-x1)^2+(y2-y1)^2) --> (x1, y1), (x2, y2)
def distance(point1, point2):
   delta_x = (point2[0]-point1[0]) ** 2
   delta_y = (point2[1]-point1[1]) ** 2
   distance_formula = math.sqrt(delta_x+delta_y)
   return distance_formula

def main():
   pass

if __name__ == "__main__":
   main()

print(slope((1, 2), (3, 4)))
print(distance((1, 2), (3, 4)))