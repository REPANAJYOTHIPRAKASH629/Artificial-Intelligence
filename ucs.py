
def ucs(start_state,goal_state):
    frontier = PriorityQueue()
    node = Node(start_state,None,None,0)
    frontier.push(node,0)
    reached = dict()
    reached[start_state] = node
    num_generated = 0
    while not frontier.is_empty():
        node = frontier.pop()
        if node.state == goal_state:
            return solution(node),num_generated
        for successor,action,step_cost in node.state.successors():
            num_generated+=1
            path_cost = node.cost+step_cost
            if successor not in reached or path_cost < reached[successor].cost:
                child_node= Node(successor,node,action,path_cost)
                reached[successor]=child_node
                frointer.push(child_node,path_cost)
    return None,num_generated
solution_path,N = ucs(start_state,goal_state)
print(f'number of generated node : {N}')
show_solution(start_state,solution_path,ncols=6)

'''
import csv
from queue import PriorityQueue

# CSE 362 - Artificial Intelligence 
# Program for calculating distance between two cities & best route 
# using Uniform Cost Search algorithm 
# Ayşe Nida Dinç - 20160808047

class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)


def build_graph(path):

    file = open(path,'r')
    routes = {}
    next(file)
    for row in file:
        
        row = row.split(',')
        routes.setdefault(row[0], []).append((row[1],row[2]))
        routes.setdefault(row[1], []).append((row[0],row[2]))
        
    file.close()
    
   # print(routes)
    return routes


def uniform_cost_search(graph, start_city, destination_city):

    visited = set() 
    route = [] 
    priority_queue = PriorityQueue() 
    priority_queue.put((0, [start_city])) 
    
    while priority_queue:

        if priority_queue.empty(): 
            print ('distance: infinity \nroute: \nnone')
            break

        distance, route = priority_queue.get() 
        city = route[len(route)-1]

        if city not in visited:
            visited.add(city) 

            if city == destination_city: 
                route.append(distance)
                display_route(graph,route)
                return route

        childs = graph[city]
        neighbor=[i[0] for i in childs] 

        for i in neighbor:
            if i not in visited: 
            
                totaldistance = distance + int(city_to_neighbor(graph, city, i))
                temp = route[:]
                temp.append(i)
                priority_queue.put((totaldistance, temp)) 

    return priority_queue


def city_to_neighbor(graph, current, neighbor):
    index = [i[0] for i in graph[current]].index(neighbor)
    return graph[current][index][1]


def display_route(graph,route):
    length = len(route)
    distance = route[-1]
    print()
    print('Distance between cities: %s km'%(distance))
    print()
    print('Best route: ')
    count = 0
    while count < (length-2):
        km = city_to_neighbor(graph, route[count], route[count+1]) 
        print('%s -> %s %s' %(route[count],route[count+1],km))
        count+=1
    return




if __name__ == "__main__":
    
    while True:
        try:
            inputFile = input("Enter road map path: ")
            test = open(inputFile, 'r').readlines()
        except FileNotFoundError:
            print("Wrong file or file path, please try again!")
        else:
            break
       
    graph = build_graph(inputFile)

    while True:
        try:
            start_city = input("Enter the start city: ")
            if start_city not in graph: 
                raise CityNotFoundError(start_city)
            break
        except CityNotFoundError:
            print("City not found on map, try again!")
    
    while True:
        try:
            destination_city = input("Enter the destination city: ")
            if destination_city not in graph: 
                raise CityNotFoundError(destination_city)
            break
        except CityNotFoundError:
            print("City not found on map, try again!")

   
    uniform_cost_search(graph, start_city, destination_city) 
         
    pass
'''
'''
import Queue

# main function: accept user inputs
def main():

    # test case
    # gird size n = 5
    # start location = (1, 1)
    # goal location = (5, 3)
    # grid values = [[100, 99, 120, 30, 70], [3, 1, 110, 97, 68], [103, 2, 105, 89, 92], [87, 4, 2, 201, 73],
    # [110, 90, 5, 80, 81]]
    # -----------------------------------------
    # the grid:
    # 110  90  5    80  81
    # 87   4   2    201 73
    # 103  2   105  89  92
    # 3    1   110  97  68
    # 100  99  120  30  70
    # ------------------------------------------
    # the least cost path = [(1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (5, 3)]
    # the least cost = 23
    least_cost_path = path_find(5, (1,1), (5,3), [[100,99,120,30,70], [3,1,110,97,68], [103,2,105,89,92], [87,4,2,201,73], [110,90,5,80,81]])
    print ("the least-cost path is: ", least_cost_path)

# find the least_cost_path
def path_find(size, start, goal, values):
    # queue holds all the frontier in the form: (sum_cost, [path])
    frontiers = PriorityQueue()
    # the list holds all the cells that have been visited
    cell_visited = []
    path = []
    sum_cost = 0
    # put the root into queue
    frontiers.put((sum_cost, [start]))

    # check if frontiers is empty
    while frontiers.empty() == False:

        # dequeue the frontier with the least cost
        frontier_expand = tuple(frontiers.get(-1))
        sum_cost = frontier_expand[0]
        # a list of tuples
        path = list(frontier_expand[1])
        # print "the path is: ", path
        # get the frontier on the path (a tuple)
        frontier_loc = path[-1]
        cell_visited.append(frontier_loc)
        # print "frontier to be expanded is: ", frontier_expand

        # if reaches to the goal location, print the path and exit
        if frontier_loc == goal:
            print ("the least cost is: ", frontier_expand[0])
            return path
        # else we expand the frontier and get its neighbors
        else:
            row_index = frontier_loc[0]
            col_index = frontier_loc[1]
            # print "the row index is: ", row_index
            # print "the column index is: ", col_index
            # add its neighbors into frontiers
            # if cell is NOT on bottom edge
            if row_index != 1 and (row_index - 1, col_index) not in cell_visited:
                cost = sum_cost + values[row_index - 2][col_index - 1] + 1
                frontier_path = list(path)
                frontier_path.append((row_index - 1, col_index))
                frontier = (cost, frontier_path)
                frontiers.put(frontier)
            # if cell is NOT on left edge
            if col_index != 1 and (row_index, col_index - 1) not in cell_visited:
                cost = sum_cost + values[row_index - 1][col_index - 2] + 1
                frontier_path = list(path)
                frontier_path.append((row_index, col_index - 1))
                frontier = (cost, frontier_path)
                frontiers.put(frontier)
            # if cell is NOT on top edge
            if row_index != size and (row_index + 1, col_index) not in cell_visited:
                cost = sum_cost + values[row_index][col_index - 1] + 1
                frontier_path = list(path)
                frontier_path.append((row_index + 1, col_index))
                frontier = (cost, frontier_path)
                frontiers.put(frontier)
            # if cell is NOT on right edge
            if col_index != size and (row_index, col_index + 1) not in cell_visited:
                cost = sum_cost + values[row_index - 1][col_index] + 1
                frontier_path = list(path)
                frontier_path.append((row_index, col_index + 1))
                frontier = (cost, frontier_path)
                frontiers.put(frontier)

main()
'''
