# Them cac thu vien neu can
import time
from math import*
class Store:
    def __init__(self):
        self.a = 0
        self.b = 0

class Order:
    def __init__(self,id,x,y,v,m):
        self.id=id
        self.x=x
        self.y=y
        self.v=v
        self.m=m
class Employee:
    def __init__(self,o):
        self.ListItem = []
        self.count = 0
        self.currentpoint = o
        self.length = 0
        self.wage = 0
        self.cost = 0
def Assign_one_for_eachEmp(ListItem_Undelivered,ListEmployee,M):
    for x in range(M):
        ListEmployee[x].ListItem.append(ListItem_Undelivered[x])
        ListEmployee[x].count+=1
        #print(ListEmployee[x].currentpoint.a,ListEmployee[x].currentpoint.b,ListItem_Undelivered[x].x,ListItem_Undelivered[x].y,'\n')
        ListEmployee[x].length = sqrt((ListEmployee[x].currentpoint.a - ListItem_Undelivered[x].x) ** 2 +(ListEmployee[x].currentpoint.b - ListItem_Undelivered[x].y) ** 2)
        #print(ListEmployee[x].length)
        ListEmployee[x].wage = 5 + ListItem_Undelivered[x].v + ListItem_Undelivered[x].m * 2
        ListEmployee[x].cost =  ListEmployee[x].wage - (ListEmployee[x].length/40*20+10)
        ListEmployee[x].currentpoint = ListItem_Undelivered[x]

    for x in range(M):
        ListItem_Undelivered.pop(0)

def delta_cost(tempListEmployee):
    Delta_cost = 0
    tempListEmployee1 = [] + tempListEmployee
    for x in tempListEmployee1:
        for y in tempListEmployee1:
            Delta_cost+= abs(x.cost-y.cost)
    return Delta_cost


def cost(ListEmployee,Item):
    check = 0
    Delta_curent = 0
    for i in range(len(ListEmployee)):
        x = ListEmployee[i]
        tempwage = x.wage
        templength = x.length
        tempcost = x.cost
        x.wage = x.wage + 5 + Item.v + Item.m * 2
        x.length = x.length + sqrt((x.currentpoint.x - Item.x)**2 + (x.currentpoint.y-Item.x)**2)
        x.cost = x.wage-(x.length/40*20+10)
        Delta = delta_cost(ListEmployee)

        if i == 0 :
            Delta_curent = Delta
            x.wage = tempwage
            x.cost = tempcost
            x.length = templength

        else:
            if Delta<Delta_curent:
                Delta_curent = Delta
                check = i
            x.wage = tempwage
            x.cost = tempcost
            x.length = templength
    ListEmployee[check].ListItem.append(Item)
    ListEmployee[check].wage = ListEmployee[check].wage + 5 + Item.v + Item.m * 2
    ListEmployee[check].length = ListEmployee[check].length + sqrt((ListEmployee[check].currentpoint.x - Item.x)**2 + (ListEmployee[check].currentpoint.y-Item.y)**2)
    ListEmployee[check].cost = ListEmployee[check].wage - (ListEmployee[check].length/40*20+10)
    ListEmployee[check].currentpoint=Item
    ListEmployee[check].count+=1
    return Delta_curent

def cost1(ListEmployee,Item):
    check = 0
    Delta_curent = delta_cost(ListEmployee)
    ListA = []
    for a in range(len(ListEmployee)):
        temp = ListEmployee[a]
        ListEmployee.pop(a)
        delta = 0
        for b in ListEmployee:
            delta += abs(temp.cost-b.cost)
        ListA.append(Delta_curent-delta*2)
        ListEmployee.insert(a,temp)

    for i in range(len(ListEmployee)):
        x = ListEmployee[i]
        tempwage = x.wage
        templength = x.length
        tempcost = x.cost
        x.wage = x.wage + 5 + Item.v + Item.m * 2
        x.length = x.length + sqrt((x.currentpoint.x - Item.x)**2 + (x.currentpoint.y-Item.x)**2)
        x.cost = x.wage-(x.length/40*20+10)
        Delta = 0
        for y in ListEmployee:
            Delta += abs(x.cost - y.cost)
        Delta = Delta*2+ListA[i]

        if i == 0 :
            Delta_curent = Delta
            x.wage = tempwage
            x.cost = tempcost
            x.length = templength

        else:
            if Delta<Delta_curent:
                Delta_curent = Delta
                check = i
            x.wage = tempwage
            x.cost = tempcost
            x.length = templength
    ListEmployee[check].ListItem.append(Item)
    ListEmployee[check].wage = ListEmployee[check].wage + 5 + Item.v + Item.m * 2
    ListEmployee[check].length = ListEmployee[check].length + sqrt((ListEmployee[check].currentpoint.x - Item.x)**2 + (ListEmployee[check].currentpoint.y-Item.y)**2)
    ListEmployee[check].cost = ListEmployee[check].wage - (ListEmployee[check].length/40*20+10)
    ListEmployee[check].currentpoint=Item
    ListEmployee[check].count+=1
    return Delta_curent

def Maxdef(ListEmployee,Item):
    check = 0
    ListEmployee[check].ListItem.append(Item)
    ListEmployee[check].wage = ListEmployee[check].wage + 5 + Item.v + Item.m * 2
    ListEmployee[check].length = ListEmployee[check].length + sqrt((ListEmployee[check].currentpoint.x - Item.x) ** 2 + (ListEmployee[check].currentpoint.y - Item.y) ** 2)
    ListEmployee[check].cost = ListEmployee[check].wage - (ListEmployee[check].length / 40 * 20 + 10)
    ListEmployee[check].currentpoint = Item
    ListEmployee[check].count += 1
    Delta = delta_cost(ListEmployee)
    return Delta

def Greedy(store,ListItem_Undelivered,N,M):
    ListEmployee = []
    for x in range(0,M):
        ListEmployee.append(Employee(store))
    Assign_one_for_eachEmp(ListItem_Undelivered,ListEmployee,M)
    # for x in ListEmployee:
    #     print(x.cost)
    #     print('\n')
    delta = 0
    for x in ListItem_Undelivered:
        # print(x.id)
        delta = cost1(ListEmployee,x)
        #delta = Maxdef(ListEmployee,x)
    print(delta)
    return ListEmployee
    # for x in ListEmployee:
    #     # print(x.currentpoint.id)
    #     for i in x.ListItem:
    #         print(i.id,' ')
    #     print("cost ís ",x.cost)
    #     print("wage is ",x.wage)
    #     print("length is ",x.length)



def assign(file_input, file_output):
    # read input
    f = open("input.txt", "r")
    count = 0
    N = 0
    M = 0
    id = 0
    ListItem_Undelivered=[]
    a = Store()
    for i in f:
        if count == 0:
            arr = i.split()
            a.a = int(arr[0])
            a.b = int(arr[1])
            count += 1
        elif count == 1:
            arr = i.split()
            N = int(arr[0])
            M = int(arr[1])
            count +=1
        else:
            arr = i.split()
            ListItem_Undelivered+= [Order(int(id) ,int(arr[0]),int(arr[1]),int(arr[2]),int(arr[3]))]
            id +=1
    # print(a.x,a.y,'\n')
    # print(N,M,'\n')
    # for j in ListItem_Undelivered:
    #     print(j.id,' ',j.x,' ',j.y,' ',j.v,' ',j.m,'\n')
    f.close()
    # run algorithm
    start = time.time()
    ListEmployee = Greedy(a,ListItem_Undelivered,N,M)
    end = time.time()
    print(end-start)

    # write output
    f = open("output.txt", "w")
    j = 1
    for x in ListEmployee:
        i = 0
        for y in x.ListItem:
            i += 1
            if(i < x.count):
                f.write("%d "%(y.id))
            else:
                f.write("%d" % (y.id))
        if j < len(ListEmployee):
            f.write("\n")
        j += 1
        print(x.cost)
    f.close


assign('input.txt', 'output.txt')
