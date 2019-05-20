import numpy as np
# Program by Joshua Banda 911908802004
goal_state = np.array([[1,2,3],
             [8,0,4],
             [7,6,5]])
"""
intial_state = np.array([[8,1,3],
                [7,2,4],
                [0,6,5]])
"""
intial_state = np.array([[0,1,3],
                [8,6,4],
                [2,7,5]])
"""
intial_state = np.array([[8,6,1],
                [2,0,3],
                [7,5,4]])"""
#intial_state = np.array([[1,2,3],[4,7,5],[0,6,8]])

def is_goal(goal,intial):
    """Check if the item matches the goal item and the game is done"""
    return np.array_equal(goal,intial)
"""
def reconstruct_path(node, n):
    Reonstucts the path from intial_node to goal_state using recurssion

    if node[3]== None:
        return node

    else:
        n.append(reconstruct_path(node[3], n))"""

def find_num(intial,num) :
    """Checks for the location of the zero to determine possible neighbors"""
    x=0
    for row in intial[0:len(intial)]:
        y=0
        for i in row[0:len(row)]:
            if i == num:
                return x,y
            y+=1
        x+=1

def create_neighbors(intial_node):
    """Used to create all the possible children nodes of the parent nodes
    by first locating the zero in the node then generating all the possible moves of the zero
    based on the rules of the game"""
    intial = intial_node[0]
    x, y = find_num(intial,0)
    neighbors = []
    distance_travelled = intial_node[2] +1
    a = np.array(intial)
    b = np.array(intial)
    c = np.array(intial)
    d = np.array(intial)

    if(x==0 and y==0):
        a[x][y], a[x][y+1] = a[x][y+1], a[x][y]
        c[x][y], c[x+1][y] = c[x+1][y], c[x][y]
        neighbors.append(a)
        neighbors.append(c)
        return neighbors, distance_travelled

    if(x==0 and y==1):
        a[x][y], a[x][y+1] = a[x][y+1], a[x][y]
        b[x][y], b[x][y-1] = b[x][y-1], b[x][y]
        c[x][y], c[x+1][y] = c[x+1][y], c[x][y]
        neighbors.append(a)
        neighbors.append(b)
        neighbors.append(c)
        return neighbors, distance_travelled

    if(x==0 and y==2):
        b[x][y], b[x][y-1] = b[x][y-1], b[x][y]
        c[x][y], c[x+1][y] = c[x+1][y], c[x][y]
        neighbors.append(b)
        neighbors.append(c)
        return neighbors, distance_travelled

    if(x==1 and y==0):
        a[x][y], a[x][y+1] = a[x][y+1], a[x][y]
        c[x][y], c[x+1][y] = c[x+1][y], c[x][y]
        d[x][y], d[x-1][y] = d[x-1][y], d[x][y]
        neighbors.append(a)
        neighbors.append(c)
        neighbors.append(d)
        return neighbors, distance_travelled

    if(x==1 and y==1):
        a[x][y], a[x][y+1] = a[x][y+1], a[x][y]
        b[x][y], b[x][y-1] = b[x][y-1], b[x][y]
        c[x][y], c[x+1][y] = c[x+1][y], c[x][y]
        d[x][y], d[x-1][y] = d[x-1][y], d[x][y]
        neighbors.append(a)
        neighbors.append(b)
        neighbors.append(c)
        neighbors.append(d)
        return neighbors, distance_travelled

    if(x==1 and y==2):
        b[x][y], b[x][y-1] = b[x][y-1], b[x][y]
        c[x][y], c[x+1][y] = c[x+1][y], c[x][y]
        d[x][y], d[x-1][y] = d[x-1][y], d[x][y]
        neighbors.append(b)
        neighbors.append(c)
        neighbors.append(d)
        return neighbors, distance_travelled

    if(x==2 and y==0):
        a[x][y], a[x][y+1] = a[x][y+1], a[x][y]
        d[x][y], d[x-1][y] = d[x-1][y], d[x][y]
        neighbors.append(a)
        neighbors.append(b)
        neighbors.append(d)
        return neighbors, distance_travelled

    if(x==2 and y==1):
         a[x][y], a[x][y+1] = a[x][y+1], a[x][y]
         b[x][y], b[x][y-1] = b[x][y-1], b[x][y]
         d[x][y], d[x-1][y] = d[x-1][y], d[x][y]
         neighbors.append(a)
         neighbors.append(b)
         neighbors.append(d)
         return neighbors, distance_travelled

    if(x==2 and y==2):
        b[x][y], b[x][y-1] = b[x][y-1], b[x][y]
        d[x][y], d[x-1][y] = d[x-1][y], d[x][y]
        neighbors.append(b)
        neighbors.append(d)
        return neighbors, distance_travelled



def calc_distance(node,goal,distance_travelled):
    """Calculation of huristic that is using manhantan distance to find
        distance of misplaced tiles from there goal state location"""
    h = 0
    f = 0
    x = 0
    intial = node
    for i in intial[0:len(intial)]:
        y = 0
        for j in i[0:len(i)]:
            if(intial[x][y] != goal[x][y]):
               loc1,loc2 = find_num(goal, intial[x][y])
               if(loc1 == x):
                   h += abs(loc2-y)

               elif(loc2 == y):
                   h += abs(loc1-x)

               else:
                   h += abs(loc1-x)+abs(loc2-y)

            y+=1
        x+=1
    return h+distance_travelled

class Node():
    def __init__(self):
        self.items = []

    def view(self):
        return len(self.items)

    def pop(self): #deletes the last element added to queue
        return self.items.pop()

    def peek(self): #displays the last element added
        if self:
            return self.items[-1]

    def push(self, item):
        """Add new node to list buy first checking """
        if(len(self.items)>=1):
            if(item[1]<=self.items[-1][1]):
                self.items.append(item)
            else:
                temp = self.items[:]
                self.items[:] = []
                for i in range(len(temp)):
                    if(item[1]>temp[i][1]):
                        self.items.append(item)
                        for j in range(i,len(temp)):
                            self.items.append(temp[j])
                        break
                    self.items.append(temp[i])

        else:
            self.items.append(item)

    def get_stack(self): #gets the whole queue listed from first in first out
        return self.items

    def is_empty(self): #checks if the queue is empty
        return self.items == []

class Element():
    def __init__(self):
        self.items = []
#print(is_goal(goal_state, goal_state))

#create_neighbors(intial_state)

#calc_distance(intial_state,goal_state,distance_travelled)
open_list = Node()
closed_list = Node()
open_list.push([intial_state,0,0, None])
#open_list.push([goal_state,19,90,'Jake'])
#open_list.push([goal_state,12,13,'Jax'])
#open_list.push([goal_state,4,90,'Joseph'])
#open_list.push([goal_state,5,90,'max'])
print("Start Positions::")
print(intial_state)

while not open_list.is_empty():
    intial_node = open_list.peek()
    closed_list.push( open_list.pop())
    if is_goal(goal_state, intial_node[0]):
        print("Goal Found Hurray!!!\n\n")
        print("Moves to win game = %d" % intial_node[2])
        #n = []
        #print(reconstruct_path(intial_node, n))
        break
    neighbors = []
    neighbors,distance_travelled = create_neighbors(intial_node)
    for i in range(len(neighbors)):
        cost=calc_distance(neighbors[i],goal_state,distance_travelled)
        chechnode = closed_list.get_stack()
        w = True
        for check in range(len(closed_list.get_stack())):
            if(np.array_equal(chechnode[check][0],neighbors[i])):
                w = False
        if w:
            open_list.push([neighbors[i],cost,distance_travelled,intial_node])
    print(len(closed_list.get_stack()))


"""
#print("br\n\n\n")
print("Open List")
print("br\n\n")
print(open_list.get_stack())
print("br\n\n")
print("Closed List")
print("br\n\n")
print(closed_list.get_stack())"""
#open_list.pop()
