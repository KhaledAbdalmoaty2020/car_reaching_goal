import Ai_search
from car_function import*
# ----------------------- implementation of the problem ---------------------- #
def computer_solve(strategy,initial_state,car_map,goal,h=None,flag=False,):
    print_car(initial_state,"C",car_map,"G",goal)
    S=Ai_search.solve(strategy,initial_state,generate_action,apply_action,isgoal,compute_cost=compute_cost,heuristic=h
    ,car_map=car_map,goal=goal)
    print(strategy)
    for i in S:
        try:
            print(i,": ",S[i])
        except:
            print("there is Noway to reach the goal->",S)
    if flag:
        print("show solution step->")
        car=initial_state
        print("Action:","start")
        print_car(initial_state,"C",car_map,"G",goal)
        for action in S['solution']:
            if action=="start":
                continue
            car=apply_action(car,action)
            print("Action:",action)
            symbol="CC"
            gsymbol="G"
            if isgoal(car,goal):
                symbol= gsymbol="You win!"

            print_car(car, symbol, car_map, gsymbol, goal)
        print("end solution steps")
car_map=create_map(2)
initial_state=generate_start(car_map)
#goal=generate_start(car_map)
goal=11
# ------------------------- try different alogrithms ------------------------- #
computer_solve("Greedy",initial_state,car_map,goal,h=h,flag=True)
#computer_solve('UCS',initial_state,car_map,goal,h=h)
#computer_solve('Astar',initial_state,car_map,goal,h=h)
#computer_solve('BFS',initial_state,car_map,goal,h=h)
#computer_solve('DFS',initial_state,car_map,goal,h=h)

