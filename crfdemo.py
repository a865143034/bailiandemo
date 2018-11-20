#coding:utf-8
ab=[[10,70],[1,60]]
ac=[[300,1],[5,25]]
bd=[[10,70],[1,60]]
cd=[[20,70],[1,150]]
'''
z=0
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                energy=ab[a][b]*ac[a][c]*bd[b][d]*cd[c][d]
                print('Energy(a={},b={},c={},d={})={}'.format(a,b,c,d,energy))
                z+=energy
#z是所有联合概率的和
print('Z={}'.format(z))
'''
for a in range(2):
    for b in range(2):
        energy=0
        for c in range(2):
            for d in range(2):
                energy+=ab[a][b]*ac[a][c]*bd[b][d]*cd[c][d]
        print('Energy(a={},b={})={}'.format(a,b,energy))
#边际概率不必归一化
