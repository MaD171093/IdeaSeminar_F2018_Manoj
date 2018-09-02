import rhinoscriptsyntax as rs

#get 2 curves & store them in list
crvs = rs.GetObjects("select 2 curves")
crv1 = crvs[0]
crv2 = crvs[1]


div = 25 #no of points the curve is divided
rad = 0.25 #radius 



#divide the curves and store the points in a list or 2 lists
pts_crv1 = rs.DivideCurve(crv1,div)
pts_crv2 = rs.DivideCurve(crv2,div)

spts_list1 = [] # list of new points for crv 1 # s = shear
spts_list2 = [] # list of new points for crv 2

#makes list of points
for i in range(len(pts_crv1)):
    d = rs.Distance(pts_crv1[i],pts_crv2[i])
    sf = d*0.3 # shear factor
    
    nz1 = pts_crv1[i][2]#n = new # z = coordinate
    nx1 = pts_crv1[i][0] + sf # x = coordinate
    ny1 = pts_crv1[i][1] # y = coordinate
    
    npts_crv1 = (nx1,ny1,nz1)
    spts_list1.append(npts_crv1)
    
    
    nz2 = pts_crv2[i][2]#n = new # z = coordinate
    nx2 = pts_crv2[i][0] - sf # x = coordinate
    ny2 = pts_crv2[i][1] # y = coordinate
    
    npts_crv2 = (nx2,ny2,nz2)
    spts_list2.append(npts_crv2)

scrv1 = rs.AddInterpCurve(spts_list1)
scrv2 = rs.AddInterpCurve(spts_list2)

pts_scrv1 = rs.DivideCurve(scrv1,div)
pts_scrv2 = rs.DivideCurve(scrv2,div)




rs.AddLoftSrf([crv1,scrv1])
rs.AddLoftSrf([crv2,scrv2])

#add the pipe for outer frame
pipe_frame1 = rs.AddPipe(scrv1, 0,rad)
pipe_frame2 = rs.AddPipe(scrv2, 0,rad)

