#avviadiscorsa
import random
import time
random.seed(time.time())
c=['che fai?', 'come stai?', 'tutto ok?', 'tutto bene?']
out=c[random.randint(0, len(c)-1)]

print(out)
f=open('latest_output.log','w+')
f.write(out)
f.close()
