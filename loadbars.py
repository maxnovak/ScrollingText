import sys
import time
import random

from progressbar import Bar, ETA,  ProgressBar, ReverseBar, FileTransferSpeed, Percentage, RotatingMarker, SimpleProgress
def loadbars():
    bars = [loadbar0,loadbar1,loadbar2,loadbar3,loadbar4,loadbar5,loadbar6]
    bars[random.randint(0,6)]()

def loadbar0():
    pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=300).start()
    for i in range(300):
        time.sleep(0.01)
        pbar.update(i+1)
    pbar.finish()

def loadbar1():
    widgets = [Bar('>'), ' ', ETA()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        # do something
        pbar.update(10*i+1)
    pbar.finish()

def loadbar2():
    class CrazyFileTransferSpeed(FileTransferSpeed):
        """It's bigger between 45 and 80 percent."""
        def update(self, pbar):
            if 45 < pbar.percentage() < 80:
                return 'Bigger Now ' + FileTransferSpeed.update(self,pbar)
            else:
                return FileTransferSpeed.update(self,pbar)

    widgets = [CrazyFileTransferSpeed(),' <<<', Bar(), '>>> ',
               Percentage(),' ', ETA()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000)
    # maybe do something
    pbar.start()
    for i in range(2000000):
        # do something
        pbar.update(5*i+1)
    pbar.finish()


def loadbar3():
    widgets= ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        # do something
        pbar.update(10*i+1)
    pbar.finish()


def loadbar4():
    widgets = ['Test: ', Percentage(), ' ',
               Bar(marker='0',left='[',right=']'),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=500)
    pbar.start()
    for i in range(100,500+1,50):
        time.sleep(0.2)
        pbar.update(i)
    pbar.finish()


def loadbar5():
    pbar = ProgressBar(widgets=[SimpleProgress()], maxval=17).start()
    for i in range(17):
        time.sleep(0.2)
        pbar.update(i + 1)
    pbar.finish()


def loadbar6():
    pbar = ProgressBar().start()
    for i in range(100):
        time.sleep(0.01)
        pbar.update(i + 1)
    pbar.finish()

if __name__ == "__main__":
    loadbars()
