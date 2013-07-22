import os, time
top = "/"
i = 1
for root, dirs, files in os.walk(top, topdown=True):
    print root #the path im starting at
    #print "--------------"
    #print dirs #should randomly choose which to go into
    #print "*****************"
    #print files #Don't care about files right now
    time.sleep(0.05)
    i += 1
    if i > 10:
        break



