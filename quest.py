sc=0
print("Earth diameter?")
ans1 = float(input())
if ans1 == 44000:
    sc=sc+1
print("Earth position starting from the sun?")
ans2 = float(input())
if ans2 == 3:
    sc=sc+1
print("Y?")
ans4 = input()
if ans4 == "Y":
    sc=sc+1
print("Your score is:",sc)
exit()