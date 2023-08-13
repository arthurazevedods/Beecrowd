
N = (int(input()))
alunos = input().split()

total = 0
for i in alunos:
	a = int(i)%3
	total += int(i)-a


print(total)