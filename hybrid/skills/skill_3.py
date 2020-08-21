#affermazioni handlea
import random
import time
random.seed(time.time())
c=['ah va bene', 'ook']
out=c[random.randint(0, len(c)-1)]

print(out)
f=open('latest_output.log','w+')
f.write(out)
f.close()
