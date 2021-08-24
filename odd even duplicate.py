mainlist = []
duplicatelist = []
evenlist = []
oddlist = []

for i in range(5):
    n = int(input(f"enter {i+1}th number: "))
    if n in mainlist:
        duplicatelist.append(n)
    elif n % 2 == 0:
        evenlist.append(n)
    else:
        oddlist.append(n)
    mainlist.append(n)



print(f"main list:\n {mainlist} ")
print("-------------------------------------")
print(f"even:\n {evenlist}\n", f"odd:\n {oddlist}")
print(f"{duplicatelist}")

