def sala(l, c, a):
    api=l*c
    vs=l*c*a
    apa=2*a*l+2*a*c
    print(api, vs, apa, sep='\n')
    return api, vs, apa

a = int(input())
c = int(input())
l = int(input())
r = sala(l, c, a)


def mens(msg):
    print(msg)


def main():
    mens(r)
