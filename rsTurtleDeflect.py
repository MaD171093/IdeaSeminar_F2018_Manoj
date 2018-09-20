import rhinoscriptsyntax as rs
import math

allObjs = rs.AllObjects()
rs.DeleteObjects(allObjs)



class Turtle:
    def __init__(self, pos = [0,0,0], heading = [1,0,0]):
        self.heading = heading
        self.point = rs.AddPoint(pos)
        pointPos = rs.PointCoordinates(self.point)
        self.direction = rs.VectorCreate(heading,pointPos)
        self.lines = []
    
    def forward(self,magnitude):
        print self.direction
        movement = rs.VectorScale(self.direction,magnitude)
        prevPos = rs.PointCoordinates(self.point)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        rs.AddLine(prevPos,currentPos)
        
    def left(self,angle):
        self.direction = rs.VectorRotate(self.direction, angle, [0,0,1])
        print(self.direction)
        
    def right(self,angle):
        self.direction = rs.VectorRotate(self.direction, -angle, [0,0,1])
        print(self.direction)
    
    def goto(self, x, y):
        prevPos = rs.PointCoordinates(self.point)
        movement = rs.VectorCreate([x,y,0],prevPos)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        rs.AddLine(prevPos,currentPos)
    
    def deflect(self,deflectPoint):
        """
        Takes a Point as an input.
        Point creates a force field.
        The turtle deflects around the point
        """
        
        defPtPos=rs.PointCoordinates(deflectPoint)
        prevPos = rs.PointCoordinates(self.point)
        deflectVector1 = rs.VectorScale(rs.VectorCreate(prevPos, defPtPos),0.33)
        deflectVector2 = -deflectVector1
        deflectVector90_1 = rs.VectorScale(rs.VectorRotate(deflectVector1,90,[0,0,1]),0.33)
        deflectVector90_2 = -deflectVector90_1
        
        deflectVectorList = [deflectVector1,deflectVector2,deflectVector90_1,deflectVector90_2]
        
        forcePts =[]
        for i in deflectVectorList:
            newPt = rs.CopyObject(deflectPoint)
            rs.MoveObject(newPt,i)
            forcePts.append(newPt)
        
        gotoPt = rs.PointCoordinates(forcePts[0])
        
        self.goto(gotoPt[0],gotoPt[1])
        rs.AddArc3Pt(forcePts[0],forcePts[1],forcePts[2])
        rs.AddArc3Pt(forcePts[1],forcePts[0],forcePts[3])
        rs.DeleteObjects(forcePts)


mad = Turtle()


"""for i in range(100):
    j = i+1
    x = 10*j*math.cos(j) 
    y = 10*j*math.sin(j)
    pt = rs.AddPoint(x,y,0)
    mad.deflect(pt)"""

x = 5
y = 25
z = 0

pt = rs.AddPoint(x,y,z)
mad.deflect(pt)