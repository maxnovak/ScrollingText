import os, time
top = "/"
i = 1
#for root, dirs, files in os.walk(top, topdown=True):
    #print root #the path im starting at
    #print "--------------"
    #print dirs #should randomly choose which to go into
    #print "*****************"
    #print files #Don't care about files right now
    #i += 1
    #if i > 10:
         #break

#will make recursive just doing forloop for basic setup
for i in range(10):
    files = os.listdir(top)
    for f in files:
        path = os.path.join(top,f)
        if os.path.isdir(path):
            print path 
            top = path
            #recursive call here
        else:
            print path
    
    time.sleep(0.05)



