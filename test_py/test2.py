import shamirs
import pickle
import os

age1=14
age2=30
(a,b,c)=shamirs.shares(age1,3)
(d,e,f)=shamirs.shares(age2,3)
q=a+d-2
w=b+e-2
r=c+f-2
print(q,w,r)
#qwr is merged share
print(shamirs.interpolate([q,w,r]))