def media(a, b, c):
    m=(a+b+c)/3
    return m

def mensagem(msg):
    print(msg)

def main():
    a = float(input())
    b = float(input())
    c = float(input())
    m = media(a, b, c)
    mensagem(f'{m:.2f}')


if __name__=='__main__':
    main()