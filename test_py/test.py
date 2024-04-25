import shamirs
import pickle
import os

age1=45
age2=30
party_send=shamirs.shares(age1,4)
party_send2=shamirs.shares(age2,4)
path='../share_received/'


#do share and store in folder
i=0
for shares in party_send:
    name=str(i)+'_send_add.txt'
    f=open(path+name,'wb')
    pickle.dump(shares,f)
    f.close()
    i+=1
  

#get file in folder, and do the add
inDir = os.listdir(path)
share_list=[]
for share_recv in inDir:
    name_list=share_recv.split('_')
    print(name_list)
    if share_recv[2:6]=='send' and share_recv[7:10]=='add':
        f=open(path+share_recv,'rb')
        share_recv=pickle.load(f)
        f.close()
        print(share_recv)
        share_list.append(share_recv)


i=0
for share in party_send:
    party_send[i]+=party_send2[i]
    i+=0

print(shamirs.interpolate(party_send))

