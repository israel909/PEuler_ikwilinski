import copy

found = set()

def solver(remaining, currentState, endState,path=""):
    if len(remaining) == 0 and currentState[1:] == endState[:-1]:
        found.add(endState + path[:-(len(endState)-1)])
        return

    for r in remaining:
        if currentState[1:] == r[:-1]:
            newSet = copy.copy(remaining)
            newSet.remove(r)
            solver(newSet, r, endState, path + r[-1])

LENGTH = 5
DATA = ['{0:b}'.format(i).zfill(LENGTH) for i in range(0, 2**LENGTH)]
solver(DATA[1:], DATA[0], DATA[0])
print("ANSWER:",sum([int(i,2) for i in found]))
