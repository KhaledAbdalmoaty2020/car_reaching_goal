#state is the car position which change with action 
#get state is the apply_action function
def get_min(fringe, key):
	Min= 0
	for i in range(1,len(fringe)):
		if fringe[i][key] < fringe[Min][key] :
			Min=i
	return Min

def init_node(strategy,intial_state):
    initial_node = {}
    initial_node['state']=intial_state
    initial_node['path']=["start"]
    #init_node["action"]="start"
    if strategy in ('UCS','Astar'): initial_node['cost']=0
    if strategy == 'Greedy': initial_node['h']=0
    if strategy =='Astar': initial_node['f']=0	
    return initial_node

def select_node(strategy,fringe):
	if strategy == 'DFS': return -1
	if strategy == 'BFS': return 0
	if strategy == 'UCS': return get_min(fringe,'cost')
	if strategy == 'Greedy': return get_min(fringe,'h')
	if strategy == 'Astar': return get_min(fringe,'f')

def add_node(strategy,next_state,action,current_node,compute_cost,heuristic,goal=None):
	next_node = {}
	next_node['state']=next_state
	#next_node['path']=[current_node['path'],action] #[[[[],'>'],'^'],'<']
	if strategy in ('UCS','Astar'):
		next_node['cost']=current_node['cost']+compute_cost(action,current_node['path'][-1])
	next_node['path']=current_node['path'][:]; next_node['path'].append(action)
	if strategy=='Greedy':
		next_node['h']=heuristic(next_node['state'],goal)
	if strategy=='Astar':
		next_node['f']=next_node['cost']+heuristic(next_node['state'],goal)
	return next_node

def solve(strategy,intial_state,get_actions,get_state,isgoal,compute_cost=None,heuristic=None,car_map=None,goal=None):
	fringe=[]; visited=[];car_map=car_map	
	fringe.append(init_node(strategy,intial_state))
	while len(fringe)>0:
		current_node=fringe.pop(select_node(strategy,fringe))
		if current_node['state'] in visited : continue
		visited.append(current_node['state'])
		if isgoal(current_node['state'],goal):
			Solution = {}
			Solution['solution']=current_node['path']
			if strategy in ('UCS','Astar'): Solution['cost']=current_node['cost'];
			Solution['expanded_nodes']=len(visited)
			return Solution
		possible_actions=get_actions(current_node['state'],car_map)
		for action in possible_actions :
			next_state=get_state(current_node['state'],action)
			next_node=add_node(strategy,next_state,action,current_node,compute_cost,heuristic,goal=goal)
			fringe.append(next_node)
	return 'failure'
