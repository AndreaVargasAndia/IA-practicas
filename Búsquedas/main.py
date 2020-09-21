import sys, pygame
import random
import math

class myPoint:
    def __init__(self, xcord, ycord):
        self.x = xcord
        self.y = ycord
    def getPairCoords(self):
        return (self.x, self.y)
    def euclidDistance(self, destination):
        return math.sqrt((self.x-destination.x)*(self.x-destination.x)+(self.y-destination.y)*(self.y-destination.y))
class myGraph:
    points = []
    links = []
    def __init__(self, numPoints, conectivity):
        self.numPoints = numPoints
        self.conectivity = conectivity
        for i in range(numPoints):
            self.points.append(myPoint(random.randint(0, 100)*5+10, random.randint(0, 100)*5+10))
    def generateLinks(self):
        self.links.clear()
        tempLinks=[]
        for p1 in self.points:
            for p2 in self.points:
                #store distance, index point1, index point2
                tempLinks.append((p1.euclidDistance(p2), self.points.index(p1), self.points.index(p2)))
            def sortRule(list):
                return list[0]
            tempLinks.sort(key=sortRule)
            #skip first element to avoid self liking
            for i in range(1,self.conectivity+1):
                if not ((tempLinks[i][1], tempLinks[i][2]) in self.links or (tempLinks[i][2], tempLinks[i][1]) in self.links):
                    self.links.append((tempLinks[i][1], tempLinks[i][2]))
            tempLinks.clear()
    def getLinkCoords(self, linkIndex):
        return (self.points[self.links[linkIndex][0]].getPairCoords(), self.points[self.links[linkIndex][1]].getPairCoords())
    def checkPos(self, pos):
        for p in self.points:
            if (p.x <= pos[0]+5 and p.x >= pos[0]-5) and (p.y <= pos[1]+5 and p.y >= pos[1]-5):
                return p
        return 0
    def DFS(self, startPoint, endPoint):
        stack = []
        path = []
        bannedPoints = []
        stack.append(startPoint)
        maxMem = 1
        steps = 1
        while len(stack) != 0 and stack[len(stack)-1] != endPoint:
            evalPoint = stack.pop()
            path.append(evalPoint)
            bannedPoints.append(evalPoint)
            evalPointIndex = self.points.index(evalPoint)
            addedPoints = 0
            for l in self.links:
                if l[0] == evalPointIndex and not self.points[l[1]] in bannedPoints:
                    stack.append(self.points[l[1]])
                    addedPoints+=1
                elif l[1] == evalPointIndex and not self.points[l[0]] in bannedPoints:
                    stack.append(self.points[l[0]])
                    addedPoints+=1
            if addedPoints == 0: bannedPoints.pop()
            steps+=1
            if len(stack)>maxMem: maxMem = len(stack)
        path.append(endPoint)
        print("Using DFS method")
        print("Max memory usage: ", maxMem)
        print("Steps till find a solution path: ", steps)
        return path
    def hillClimbing(self, startPoint, endPoint):
        stack = []
        path = []
        bannedPoints = []
        stack.append(startPoint)
        maxMem = 1
        steps = 1
        while len(stack) != 0 and stack[len(stack)-1] != endPoint:
            evalPoint = stack.pop()
            path.append(evalPoint)
            bannedPoints.append(evalPoint)
            evalPointIndex = self.points.index(evalPoint)
            addedPoints = 0
            for l in self.links:
                if l[0] == evalPointIndex and not self.points[l[1]] in bannedPoints:
                    stack.append(self.points[l[1]])
                    addedPoints+=1
                elif l[1] == evalPointIndex and not self.points[l[0]] in bannedPoints:
                    stack.append(self.points[l[0]])
                    addedPoints+=1
            def sortRule(point):
                return point.euclidDistance(endPoint)
            stack.sort(reverse=True, key=sortRule)
            if addedPoints == 0: bannedPoints.pop()
            steps+=1
            if len(stack)>maxMem: maxMem = len(stack)
        path.append(endPoint)
        print("Using Hill climbing method")
        print("Max memory usage: ", maxMem)
        print("Steps till find a solution path: ", steps)
        return path

#utility funcs
def pointListToCoordList(pointList):
    coordList = []
    for i in pointList:
        coordList.append((i.x, i.y))
    return coordList

def animatedDraw(screen, points):
    selectedPointColor = (86,156,214)
    visitedPointColor = (255,0,0)
    tmpPoint = points[0]
    for i in points:
        pygame.draw.circle(screen, selectedPointColor, (tmpPoint.x,tmpPoint.y), 3, 2)
        pygame.draw.circle(screen, visitedPointColor, (i.x,i.y), 3, 2)
        tmpPoint = i
        #pygame.draw.lines(screen, selectedPointColor, False, pointListToCoordList(searchPath), 1)
        pygame.time.wait(100)
        pygame.display.update()
#end of utility funcs

pygame.init()
size= 520, 520
screen = pygame.display.set_mode(size)
pygame.display.set_caption("IA tarea")

#colores
background = (30,30,30)
frameColor = (197,134,192)
pointColor = (212, 212, 212)
selectedPointColor = (86,156,214)
pointSize = 3

screen.fill(background)
pygame.draw.rect(screen, frameColor, (5,5,510,510), 2)
numPoints = 200
conectivity = 4
grafo=myGraph(numPoints, conectivity)
grafo.generateLinks()
selectedPoints = [None] * 2

for i in range(len(grafo.links)):
    pygame.draw.lines(screen, frameColor, False, grafo.getLinkCoords(i), 1)
for i in myGraph.points:
    pygame.draw.circle(screen, pointColor, (i.x,i.y), pointSize, 2)
#for i in selectedPoints:
#    pygame.draw.circle(screen, frameColor, (i.x,i.y), 3, 1)
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            tmpPoint = grafo.checkPos(pos)
            if tmpPoint != 0:
                if event.button == 1:
                    if selectedPoints[0] != None:
                        pygame.draw.circle(screen, pointColor, (selectedPoints[0].x,selectedPoints[0].y), pointSize, 2)
                    selectedPoints[0] = tmpPoint
                    pygame.draw.circle(screen, selectedPointColor, (tmpPoint.x,tmpPoint.y), pointSize, 2)
                if event.button == 3:
                    if selectedPoints[1] != None:
                        pygame.draw.circle(screen, pointColor, (selectedPoints[1].x,selectedPoints[1].y), pointSize, 2)
                    selectedPoints[1] = tmpPoint
                    pygame.draw.circle(screen, selectedPointColor, (tmpPoint.x,tmpPoint.y), pointSize, 2)
                    
            pygame.display.update()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                searchPath = grafo.DFS(selectedPoints[0], selectedPoints[1])
                animatedDraw(screen, searchPath)
            elif event.key == pygame.K_w:
                searchPath = grafo.hillClimbing(selectedPoints[0], selectedPoints[1])
                animatedDraw(screen, searchPath)
            elif event.key == pygame.K_r:
                screen.fill(background)
                pygame.draw.rect(screen, frameColor, (5,5,510,510), 2)
                for i in range(len(grafo.links)):
                    pygame.draw.lines(screen, frameColor, False, grafo.getLinkCoords(i), 1)
                for i in myGraph.points:
                    pygame.draw.circle(screen, pointColor, (i.x,i.y), pointSize, 2)
                pygame.display.update()

pygame.quit()
