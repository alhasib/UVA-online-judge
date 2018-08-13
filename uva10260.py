one = ['B','F','P','V']
two = ['C','G','J','K','Q','S','X','Z']
three = ['D','T']
four = ['L']
five = ['M','N']
six = ['R']

while True:
    try:
        kr = ''
        ll = ''
        jl = ''
        zz = input()
        p = []
        for i in zz:
            if i in one and i != kr and jl != 'one':
                p.append('1')
                ll = 'one'
            elif i in two and i != kr and jl != 'two':
                p.append('2')
                ll = 'two'
            elif i in three and i != kr and jl != 'three':
                p.append('3')
                ll = 'three'
            elif i in four and i != kr and jl != 'four':
                p.append('4')
                ll = 'four'
            elif i in five and i != kr and jl != 'five':
                p.append('5')
                ll = 'five'
            elif i in six and i != kr and jl != 'six':
                p.append('6')
                ll = 'six'
            else:
                ll = ''
            kr = i
            jl = ll
        pp = (''.join(p))
        print(pp)
    except EOFError:
        break