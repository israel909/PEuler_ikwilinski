from shapely.geometry import Point, Polygon

ORIGIN = Point(0, 0)
count = 0
with open('triangle.txt', "r") as f:
    for line in f:
        coords = list(map(int,line.split(",")))
        currentTriangle = Polygon([(coords[0], coords[1]),(coords[2], coords[3]),(coords[4], coords[5])])
        if currentTriangle.contains(ORIGIN): count += 1
print("ANSWER:", count)
