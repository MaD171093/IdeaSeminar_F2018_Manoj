import rhinoscriptsyntax as rs


#get 2 curves & store them in list
crvs = rs.GetObjects("select 2 curves")

div = 25 #no of points the curve is divided
gravity = 10 #amout by which the points will come down


#divide the curves and store the points in a 2 lists
pts_crv1=rs.DivideCurve(crvs[0],div, False)
pts_crv2=rs.DivideCurve(crvs[1],div, False)


rad = 0.25 #radius for the downward wing


gpts_list1 = [] # list of new points for crv 1
gpts_list2 = [] # list of new points for crv 2

#makes the line between points 
for i in range(len(pts_crv1)):
    nz1 = pts_crv1[i][2] - gravity #n = new # z = coordinate
    nx1 = pts_crv1[i][0] # x = coordinate
    ny1 = pts_crv1[i][1] # y = coordinate
    
    npts_crv1 = (nx1,ny1,nz1)
    gpts_list1.append(npts_crv1)

    
    nz2 = pts_crv2[i][2] - gravity #n = new # z = coordinate
    nx2 = pts_crv2[i][0] # x = coordinate
    ny2 = pts_crv2[i][1] # y = coordinate
    
    npts_crv2 = (nx2,ny2,nz2)
    gpts_list2.append(npts_crv2)


gcrv1 = rs.AddInterpCurve(gpts_list1)
gcrv2 = rs.AddInterpCurve(gpts_list2)


#divide the curves and store the points in a list or 2 lists
pts_gcrv1 = rs.DivideCurve(gcrv1,div,False)
pts_gcrv2 = rs.DivideCurve(gcrv2,div,False)

spts_list1 = [] # list of new points for gcrv 1 # s = shear
spts_list2 = [] # list of new points for gcrv 2

#makes list of points
for i in range(len(pts_gcrv1)):
    d = rs.Distance(pts_gcrv1[i],pts_gcrv2[i])
    sf = -d*0.3 # shear factor
    
    nz1 = pts_gcrv1[i][2]#n = new # z = coordinate
    nx1 = pts_gcrv1[i][0] + sf # x = coordinate
    ny1 = pts_gcrv1[i][1] # y = coordinate
    
    npts_gcrv1 = (nx1,ny1,nz1)
    spts_list1.append(npts_gcrv1)
    
    
    nz2 = pts_gcrv2[i][2]#n = new # z = coordinate
    nx2 = pts_gcrv2[i][0] - sf # x = coordinate
    ny2 = pts_gcrv2[i][1] # y = coordinate
    
    npts_gcrv2 = (nx2,ny2,nz2)
    spts_list2.append(npts_gcrv2)
    print("TEST","Point added")

scrv1 = rs.AddInterpCurve(spts_list1)
scrv2 = rs.AddInterpCurve(spts_list2)

pts_scrv1 = rs.DivideCurve(scrv1,div)
pts_scrv2 = rs.DivideCurve(scrv2,div)




rs.AddLoftSrf([gcrv1,scrv1])
rs.AddLoftSrf([gcrv2,scrv2])

#add the pipe for outer frame
pipe_frame1 = rs.AddPipe(scrv1, 0,rad)
pipe_frame2 = rs.AddPipe(scrv2, 0,rad)
