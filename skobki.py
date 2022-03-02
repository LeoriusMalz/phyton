kvad = 0
krug = 0
figure = 0

a = list(str(input().split()))[2:-2]

for i in a:
    if i == "(":
        krug += 1;
    elif i == "[":
        kvad += 1;
    elif i == "{":
        figure += 1;
    if i == ")":
        krug -= 1;
    elif i == "]":
        kvad -= 1;
    elif i == "}":
        figure -= 1;
        
if (kvad == 0) and (krug == 0) and (figure == 0):
    print("YES")
else:
    print("NO")
