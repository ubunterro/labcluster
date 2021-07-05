import matplotlib.pyplot as plt
from random import randint

from Point import Point

POINTS_NUM = 70
T = 40
SIZE = 100
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

plt.gca().set_aspect('equal')

points = []
clusters = []

medianX = 0
medianY = 0

for i in range(0, POINTS_NUM):
    p = Point(randint(0, SIZE), randint(0, SIZE))
    medianX += p.x
    medianY += p.y
    points.append(p)

# найдем среднюю точку

medianX = medianX / POINTS_NUM
medianY = medianY / POINTS_NUM
medianPoint = Point(medianX, medianY)
print("med", medianPoint)

centerPoint = None # индекс средней точки в массиве
centerPointIndex = 0
minDistance = float("inf")

for i in range(0, POINTS_NUM):
    distance = points[i].distance(medianPoint)
    #print (distance)
    if distance < minDistance:
        centerPoint = points[i]
        centerPointIndex = i
        minDistance = distance

centerPoint.cluster = 1
print(centerPointIndex)
print(centerPoint)
print(points)
points.insert(0, points.pop(centerPointIndex))
print(points)


lastCluster = 0;
centers = [centerPoint]; # центр первого кластера

for i in range (0, POINTS_NUM):
    minDistance = float("inf")
    closestCluster = -1
    for ci in range(0, len(centers)):
        distance = points[i].distance(centers[ci])
        print(distance)
        if distance < minDistance:
            minDistance = distance
            closestCluster = ci
    if minDistance > T: # не нашли куда вступать
        lastCluster += 1
        points[i].cluster = lastCluster
        centers.append(points[i])
    else:
        points[i].cluster = closestCluster



print(centers)



print(points)

clusterIndex = 0
for p in points:
    plt.plot(p.x, p.y, COLORS[p.cluster]+'o')

for i in range(0, lastCluster+1):
    print("Z" + str(i))
    for pi, p in enumerate(points):
        if p.cluster == i:
            print("X" + str(pi) + "(" + str(p.x) + "," + str(p.y) + ")")


for i, center in enumerate(centers):
    #plt.gca().add_patch(plt.Circle((center.x, center.y), T, color=COLORS[i], fill=False))
    plt.text(center.x, center.y, 'Z' + str(i) + '(' + str(center.x) + ', ' + str(center.y) + ')', fontsize=10)

plt.plot(medianX, medianY, 'r*')
#plt.plot(centerPoint.x, centerPoint.y, 'go')

plt.axis([-2, SIZE + SIZE * 0.2 , -2, SIZE + SIZE * 0.2])
plt.show()

print(points)
