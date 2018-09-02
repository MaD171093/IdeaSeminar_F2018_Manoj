import rhinoscriptsyntax as rs


#get 2 curves & store them in list
crvs = rs.GetObjects("select 2 curves")

div = 25 #no of points the curve is divided
gravity = 10 #amout by which the points will come down


#divide the curves and store the points in a 2 lists
pts_crv1=rs.DivideCurve(crvs[0],div, False)
pts_crv2=rs.DivideCurve(crvs[1],div, False)


rad1 = 0.15 #radius for the downward structure
rad2 = rad1*2 #radius fore the frame 

gpts_list1 = [] # list of new points for crv 1
gpts_list2 = [] # list of new points for crv 2

#makes the line between points 
for i in range(len(pts_crv1)):
    nz1 = pts_crv1[i][2] - gravity #n = new # z = coordinate
    nx1 = pts_crv1[i][0] # x = coordinate
    ny1 = pts_crv1[i][1] # y = coordinate
    
    npts_crv1 = (nx1,ny1,nz1)
    gpts_list1.append(npts_crv1)
    gline1 = rs.AddLine(pts_crv1[i],npts_crv1)#gravity line
    pipe_crv1 = rs.AddPipe(gline1, 0,rad1)
    
    nz2 = pts_crv2[i][2] - gravity #n = new # z = coordinate
    nx2 = pts_crv2[i][0] # x = coordinate
    ny2 = pts_crv2[i][1] # y = coordinate
    
    npts_crv2 = (nx2,ny2,nz2)
    gpts_list2.append(npts_crv2)
    gline2 = rs.AddLine(pts_crv2[i],npts_crv2)#gravity line
    pipe_crv2 = rs.AddPipe(gline2, 0,rad1)

gcrv1 = rs.AddInterpCurve(gpts_list1)
gcrv2 = rs.AddInterpCurve(gpts_list2)

rs.AddPipe(gcrv1, 0,rad2)
rs.AddPipe(gcrv2, 0,rad2)