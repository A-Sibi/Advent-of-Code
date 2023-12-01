with open('data/day20.txt') as f:
    data1= [] 
    for i in f.read().strip().split('\n'):
        data1.append(i)#naredimo list in appendamo vrednosti 
data = []
for i in data1:
    data.append(int(i))
# data = [1,2,-3,3,-2,0,4]

class Stevilka:
    def __init__(self,val, index):
        self.value = val
        self.org_index = index
        self.wasMoved = False
        self.targetindex = None

dataclass = []

for i in range(len(data)):
    dataclass.append(Stevilka(data[i],i))


for _ in range(len(dataclass)):
    i = 0
    while dataclass[i].wasMoved:
        i += 1
    dataclass[i].target_index = i + dataclass[i].value
    # if dataclass[i].target_index < 0:
    #     dataclass[i].target_index += len(dataclass)
    if dataclass[i].target_index >= len(dataclass):
        dataclass[i].target_index -= len(dataclass)
    if dataclass[i].target_index == 0:
        dataclass[i].target_index = -1
    x = dataclass.pop(i)
    x.wasMoved = True
    # dataclass.insert(x.org_index,None)
    dataclass.insert(x.target_index,x)
    # dataclass.remove(None)


# for stev in dataclass:
    # print(stev.value, end=" ")
# print()
coords = 0

start = 0
for i in range(len(dataclass)):
    if dataclass[i].value == 0:
       start = i 
       break
print('start =', start)

for k in range(1,4):
    novi_i = (k * 1000 + start)
    while novi_i >= len(dataclass):
        novi_i -= len(dataclass)

    coords += dataclass[novi_i].value
    print(dataclass[novi_i].value)
print('seštevek = ',coords)

# print(dataclass)
with open('output20.txt','w') as fp:
    for i in range(len(dataclass)):
        fp.write(str(dataclass[i].value) + '\n')

# odg je više od 10997