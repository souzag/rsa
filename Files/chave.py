import sys

p = int(sys.argv[1])
q = int(sys.argv[2])
e = int(sys.argv[3])

def create_public_key_file(n, e, p, q):
    
    try:
        file = open("PublicKey.txt", "w")
        file.write(str(n))
        file.write(' ')
        file.write(str(e))
        file.write(' ')
        file.write('p = ')
        file.write(str(p))
        file.write(' ')
        file.write('q = ')
        file.write(str(q))
        file.close()

    except FileNotFoundError:
        print("Houve um erro ao criar o arquivo, tente novamente")
def check_prime(k):
    if k == 0 or k == 1:
        return False
    elif k == 2:
        return True
    elif k % 2 == 0:
        return False
    i = 3
    r = k ** 0.5
    while(i <= r):
        if k % i == 0:
            return False
        i += 2
    return True
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)
def init():
    n = p * q 
    FiN = int((p - 1) * (q - 1))
    if not check_prime(p):
        print('p não é um numero primo')
    elif not check_prime(q):
        print('q não é um numero primo')
    elif n <= 26:
        print('O produto p.q deve ser maior que 26')
    elif gcd(e, FiN) != 1 :
        print('não é co-primo com o produto (p-1).(q-1)')
    else :
        create_public_key_file(n, e , p , q)
        print('Chave publica gerada com sucesso!')
init()