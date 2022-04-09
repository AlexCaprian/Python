def meia_noite(h, m, s):
    ts=((h*60)*60)+(m*60)+s
    r=ts-0
    return r


h=int(input())
m=int(input())
s=int(input())
t=meia_noite(h, m,s)


def mensagem(msg):
    print(msg)


def main():
    mensagem(t)


if __name__=='__main__':
    main()