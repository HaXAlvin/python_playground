# UVA 10154 Weights and Measures


# test data
# [(weight, strength, (id))]
# turtles = [(100,101,0), (1,100,1)]
# turtles = [(300,1000,0), (1000,1200,1),(200,600,2),(100,101,3)]
# turtles = [(20,20,0), (20,40,1),(10,60,2),(140,150,3)]
# turtles = [(10,40,0), (20,100,1),(30,40,2)]
# turtles = [(3,5,0), (2,4,1),(1,2,2),(1,1,3)]
turtles = [(101,101,0), (100,201,1),(99,300,2),(98,301,3),(5,302,4)]


def find_turtle_bottom_up(mini_carry:int, left_turtle:list,path=""):
    end = True
    # print("test",path)
    for index,turtle in enumerate(left_turtle):
        if mini_carry >= turtle[0]:
            end = False
            carry = min(mini_carry-turtle[0],turtle[1]-turtle[0])
            find_turtle_bottom_up(carry, left_turtle[:index]+left_turtle[index+1:],path+f"{turtle[2]}")
    if end:
        print(path)


find_turtle_bottom_up(999999, turtles)
print()


def find_turtle_top_down(total_weight:int,left_turtle:list,path=""):
    end = True
    for index,turtle in enumerate(left_turtle):
        if turtle[1]-turtle[0]>=total_weight:
            end = False
            find_turtle_top_down(total_weight+turtle[0], left_turtle[:index]+left_turtle[index+1:],path+f"{turtle[2]}")
    if end:
        print(path)

find_turtle_top_down(0,turtles)
print()


def find_turtle_top_down_look_after(left_turtle:list):
    left_turtle.sort(key=lambda x:x[1])
    for i in range(len(left_turtle)):
        weight = left_turtle[i][0]
        path = f"{left_turtle[i][2]}"
        for turtle in left_turtle[:i]+left_turtle[i+1:]:
            if turtle[1]-turtle[0]>=weight:
                weight += turtle[0]
                path += f"{turtle[2]}"
        print(path)

find_turtle_top_down_look_after(turtles)
print()


def find_turtle_top_down_look_after(left_turtle:list):
    left_turtle.sort(key=lambda x:x[0])
    left_turtle.sort(key=lambda x:x[1])
    weights = []
    path = []
    for turtle in left_turtle:
        weights += [turtle[0]]
        path += [turtle[2]]
        if turtle[1]<sum(weights):
            fat = weights.index(max(weights))
            weights.pop(fat)
            path = path[:fat]+path[fat+1:]
    print("".join(map(str,path)))

find_turtle_top_down_look_after(turtles)
print()
