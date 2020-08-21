#saluta
#<0>
import random
import time
random.seed(time.time())
c=['ciao', 'ei', 'bella']
out=c[random.randint(0, len(c)-1)]

print(out)
f=open('latest_output.log', 'w+')
f.write(out)
f.close()