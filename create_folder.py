#Saba's First Task

#K Sabarathinam
#101114012

import os

i=1;

while i<=100:
    if not os.path.exists('C:/Users/Ammu/Desktop/'+'folder'+str(i)):
        os.mkdir('C:/Users/Ammu/Desktop/'+'folder'+str(i),0o755)
    f=open('C:/Users/Ammu/Desktop/'+'folder'+str(i)+'/folder'+str(i)+'.txt','a')
    f.close()
    i+=1



    
