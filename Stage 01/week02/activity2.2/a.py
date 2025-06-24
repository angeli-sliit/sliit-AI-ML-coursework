marks = []
for i in range (10):
    mark = int(input(f"Enter mark stusent {i+1}:"))
    marks.append(mark)

tot=sum(marks)
print("min : ",min(marks))
print("max : ",max(marks))
print("avg : ",(tot/10.0))







