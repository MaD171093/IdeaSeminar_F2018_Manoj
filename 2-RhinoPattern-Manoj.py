import rhinoscriptsyntax as rs
#function for middle point

# gmp = get middle point
def gmp(p1,p2):
    x=(p1[0]+p2[0])/2
    y=(p1[1]+p2[1])/2
    z=(p1[2]+p2[2])/2
    return[x,y,z]


#get 2 curves & store them in list
crvs = rs.GetObjects("select 2 curves")

div = 25 #no of points the curve is divided


#divide the curves and store the points in a 2 lists
pts_crv1=rs.DivideCurve(crvs[0],div, False)
pts_crv2=rs.DivideCurve(crvs[1],div, False)


#measure the distance between the points
for  i in range (len(pts_crv1)):
    d=rs.Distance(pts_crv1[i],pts_crv2[i])
    
    #for making surface
    mid=gmp(pts_crv1[i],pts_crv2[i])
    pf=d/4 #pf=proportionate factor
    
    mx=mid[0]
    my=mid[1]
    mz=mid[2]+pf # only z co-ordinate is changing
    top=(mx,my,mz)
    
    #for making a curved roof 
    list_crv1=rs.AddInterpCurve([pts_crv1[i],top,pts_crv2[i]])#list of curves are stored here 
    if(i<len(pts_crv1)-1):
        npt1=pts_crv1[i+1]# n=new; i.e points are selected on the suceeding line
        npt2=pts_crv2[i+1]
        nmid=gmp(npt1,npt2)
        
        r=rs.Distance(pts_crv1[i+1],pts_crv2[i+1])
        npf=r/4 #pf=proportionate factor
        
        upf=npf*1.6 # upper proportionate factor
        
        nmx=nmid[0]
        nmy=nmid[1]
        nmz=nmid[2]+upf
        
        ntop=(nmx,nmy,nmz)
        
        rail=rs.AddLine(pts_crv1[i],npt1) 
        
    list_crv2=rs.AddInterpCurve([npt1,ntop,npt2])
    
    srf=rs.AddSweep1(rail,[list_crv1,list_crv2])
    
