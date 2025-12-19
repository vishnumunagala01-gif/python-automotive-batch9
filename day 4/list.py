food=["dal","sambar","rice"]
print(food[0])

food.append("curd")
print(food)

food.remove("dal")
print(food)

food.insert(1,"idly")
print(food)
print(food.sort())

for i in food:
    print(i)