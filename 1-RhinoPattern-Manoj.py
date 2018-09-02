import rhinoscriptsyntax as rs

#get 2 curves & store them in list
crvs = rs.GetObjects("select 2 curves")
crv1 = crvs[0]
crv2 = crvs[1]

div = 25 #no of points the curve is divided
rad1 = 0.25 #radius for the internal connections
rad2 = rad1*2 #radius fore the frame

#divide the curves and store the points in a list or 2 lists
pts1 = rs.DivideCurve(crv1,div)
pts2 = rs.DivideCurve(crv2,div)

#makes the line between points and the internal pipe
for i in range(len(pts1)):
    if rs.Distance(pts1[i],pts2[i])>0:
        lines = rs.AddLine(pts1[i],pts2[i])
        pipe = rs.AddPipe(lines, 0,rad1)
    else:
        continue

#add the pipe for outer frame
pipe_frame1 = rs.AddPipe(crv1, 0,rad2)
pipe_frame2 = rs.AddPipe(crv2, 0,rad2)