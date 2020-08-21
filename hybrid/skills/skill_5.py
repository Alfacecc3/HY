#reply_reask_handlea
import random, time, sys, json
def data_structure():
    return '''
    data è un intent con un array outputs particolare.
    questa è la sua struttura:
    "outputs":[
        #elemento 0:
        [
            #elemento 00:
            "neanche io",
            #elemento 01:
            "uguale",
        ],
        # elemento 1:
        [
            #elemento 10:
            "wow!",
            #elemento 11:
            "che bello"
        ]
    ]
    qui serve un dizionario per ricordare a cosa corrisponde ogni numero
    dimensions={
        "null_reply":0, # se dice che non sta facendo niente o cose simili
        "interesting":1 # se sta facendo qualcosa di figo
    }
    '''

raw_data=json.loads(open('db/dataset.json').read())
data=raw_data['intents']['reply_reask_handlerIntent']['outputs']
dimensions={
    'say_same_thing': 0,
    'interesting': 1,
    'happyness': 2,
    'sadness': 3
}
c=['ok']
x=sys.argv[1]
y=sys.argv[2]
#print('usr replied: '+x)
#print('after reading: '+y)
if x.startswith('nulla') or x.startswith('niente'):
    #avevi chiesto cosa stesse facendo
    c=data[dimensions['say_same_thing']]
elif x.startswith('male') or x.startswith('non bene'):
    c=data[dimensions['sadness']]
elif x.startswith('bene') or x.startswith('non male'):
    c=data[dimensions['happyness']]

out=c[random.randint(0, len(c)-1)]
print(out)
print(data[dimensions['say_same_thing']][random.randint(0, len(data[0])-1)])
f=open('latest_output.log', 'w+')
f.write(out)
f.close()