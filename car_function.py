import random
#car_map is the map of the problem
def create_map(x):
    car_map=[0,1,2,3,4,5,6,7,8,9,10,11]
    n=0
    li=[1,10]
    while n<x:
        index=random.randint(0,11)
        if index in li:
            continue  
        car_map[index]='x'
        n+=1
    return car_map



def print_map(car_map):
    s=[]
    for cell in car_map:
        s.append(str(cell))
    print(
        '_'*13 +'\n'+
        "| "+s[0]+' | '+s[1]+' | '+s[2]+' |'+'\n'+
        "| "+s[3]+' | '+s[4]+' | '+s[5]+' |'+'\n'+
        "| "+s[6]+' | '+s[7]+' | '+s[8]+' |'+'\n'+
        "| "+s[9]+' |'+s[10]+' | '+s[11]+'|'+'\n'+
        '_'*13 +'\n'
    )



def generate_start(car_map):
    state=False
    s=0
    while state==False:
        s=random.randint(0,11)
        if car_map[s]!='x':
            state=True
    return s


def apply_action(car,action):
    if action==">":
        car+=1
    if action=="<":
        car-=1
    if action=="^":
        car-=3
    if action=="v":
        car+=3
    return car
def generate_action(car,car_map):
    available_action=[]
    if car not in [0,1,2] and car_map[apply_action(car,"^")]!='x':available_action.append("^");
    if car not in [9,10,11]and car_map[apply_action(car,"v")]!='x':available_action.append("v");
    if car not in [2,5,8,11]and car_map[apply_action(car,">")]!='x':available_action.append(">");
    if car not in [0,3,6,9]and car_map[apply_action(car,"<")]!='x':available_action.append("<");
    #print("avail_action befor modification",available_action)
    return available_action
#print(generate_action(1,create_map(2)))
def print_car(car,Csymbol,car_map,Gsymbol,goal):
    s=[]
    for cell in car_map:
        s.append(str(cell))
    s[car]=Csymbol
    s[goal]=Gsymbol
    print(
        '_'*14 +'\n'+
        "| "+s[0]+' | '+s[1] +'  | '+s[2] +'  |'+'\n'+
        "| "+s[3]+' | '+s[4] +'  | '+s[5] +'  |'+'\n'+
        "| "+s[6]+' | '+s[7] +'  | '+s[8] +'  |'+'\n'+
        "| "+s[9]+' | '+s[10]+' | '+s[11]+' |'+'\n'+
        '_'*14 +'\n'
    )


def isgoal(car,goal):
    if car==goal:
        return True
    return False
    

def compute_cost(new_action,previous_action):
    cost=0
    if previous_action=="start" or new_action==previous_action:
        cost=1
    else:
        cost=2
    return cost




def h(car,goal):
    count=0
    count+= + abs( int(goal%3) - int(car%3) )
    return count
