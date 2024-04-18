import shamirs

age=20
(a,b,c,d)=shamirs.shares(20,4)
(q,w,e,r)=shamirs.shares(30,4)
aa=shamirs.interpolate([a-b, b-c, c-d, d-a])
print(aa)