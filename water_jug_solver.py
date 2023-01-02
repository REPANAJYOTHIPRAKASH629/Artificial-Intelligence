from collections import defaultdict
jug1,jug2,aim = 4,3,1
visited = defaultdict(lambda:False)
def waterjugsolver(amt1,amt2):
    if (amt1==aim and amt2==0) or (amt2==aim and amt1==0):
        print(amt1,amt2)
        return True
    if visited[(amt1,amt2)]==False:
        print(amt1,amt2)
        visited[(amt1,amt2)] = True
        return(waterjugsolver(0,amt2) or
               waterjugsolver(amt1,0) or
               waterjugsolver(jug1,amt2) or
               waterjugsolver(amt1,jug2) or
               waterjugsolver(amt1+min(amt2,(jug1-amt1)),amt2-min(amt2,(jug1-amt1))) or
               waterjugsolver(amt1+min(amt1,(jug2-amt2)),amt1-min(amt1,(jug2-amt2))))
    else:
        return False
print("Steps : ")
waterjugsolver(0,0)
               
