import sys
import time
import itertools

done = False

def animate(msg):
    print(msg)
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            raise Exception('Finished')
        sys.stdout.write('\r'+msg+' ' + c)
        sys.stdout.flush()
    sys.stdout.write('\rDone!     ')
