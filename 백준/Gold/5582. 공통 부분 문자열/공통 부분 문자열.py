string1 = input()
string2 = input()

dp = [0]*(len(string1)+1)
Max = 0

for x in range(len(string2)):
    temp = [0]*(len(string1)+1)
    for y in range(len(string1)):
        if string2[x] == string1[y]:
            temp[y+1] = dp[y]+1
            if temp[y+1] > Max:
                Max = temp[y+1]
    dp = temp

print(Max)