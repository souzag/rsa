from correct import correct_file

alfa = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

def header():
    print("|------------------------------------------------------------------------------------------------|")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                             ********      ********        ***                                  |")
    print("|                             **     **     **             ** **                                 |")
    print("|                             **     **     **            **   **                                |")
    print("|                             ********      ********     *********                               |")
    print("|                             **     **           **    **       **                              |")
    print("|                             **     **           **   **         **                             |")
    print("|                             **     **     ********  **           **                            |")
    print("|                                                                                                |")
    print("|                             Alunos: Ascânio Sávio de Araujo Neves                              |") 
    print("|                                     Gabriel Luiz Leite Souza                                   |")
    print("|                                     Danilo Vasconcelos Freire                                  |")
    print("|                                     Jorge Firmo Soares Neto                                    |")
    print("|                                     João Victor de Alarcão Ayalla Alcântara                    |")
    print("|------------------------------------------------------------------------------------------------|")
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

# Euclides Algorithm
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def create_public_key_file(n, e):
    
    try:
        file = open("PublicKey.txt", "w")
        file.write(str(n))
        file.write(' ')
        file.write(str(e))
        file.close()

    except FileNotFoundError:
        print("Houve um erro ao criar o arquivo, tente novamente")

def crypt(read_file, msg, e, n):
    end = len(msg)
    cryptMsg = ""
    for i in range(end):
        m = msg[i]
        #fórmula padrao para criptografrar
        cryptMsg += str((alfa.index(m) ** e) % n)
        if(i + 1 < end):
            cryptMsg += ',' #separador, para saber quem é quem
    try:
        crypt_file = open("EncryptFile.txt", "w")
        crypt_file.write(cryptMsg)
        crypt_file.close()
        return 1
    except FileNotFoundError:
        print("Houve um erro ao criar o arquivo, tente novamente")
        return -1

def findInverse(e, fiN) :
	d = 0
	while(int((d * e) % fiN) != 1):
		d += 1
	return d

def decrypt(cryptMsg, d, n):
    decryptMsg = ""
    i = 0
    end = len(cryptMsg)
    while i < end:
        current = ""
        while i < end and cryptMsg[i] != ',':
            current += cryptMsg[i]
            i += 1
        i += 1
        current = int (current)
        decryptMsg += alfa[(current ** d) % n]
    try:
        file = open("DecryptFile.txt", "w")
        file.write(decryptMsg)
        file.close()
    except FileNotFoundError:
        print("Não foi possivel criar o arquivo descriptografado, tente novamente")
def init():
    p = 0
    q = 0
    e = 0
    FiN = 0
    while(True):
        print("Digite uma das seguintes operações: ")
        print("[ 1 ] Gerar chave pública")
        print("[ 2 ] Criptografar")
        print("[ 3 ] Descriptografrar")
        print("[ 4 ] Sair")
        operation = int(input())
        if operation == 1:
            p = int(input("Informe um número primo p: "))
            while(not check_prime(p)):
                print(p, "não é um numero primo.")
                p = int(input("Informe um número primo p: "))
            q = int(input("Informe um número primo q: "))
            while(not check_prime(q)):
                print(q, "não é um numero primo.")
                q = int(input("Informe um número primo q: "))
            n = p * q # produto dos primos
            while(n <= 26):
                print("O produto p.q deve ser maior que 26")
                p = int(input("Informe um número primo p: "))
                q = int(input("Informe um número primo q: "))
                n = p * q
            e = int(input("Informe um número [e], tal que, [e] seja co-primo com o produto (p-1).(q-1): "))
            FiN = int((p - 1) * (q - 1))
            while(gcd(e, FiN) != 1):
                print(e, "não é co-primo com o produto (p-1).(q-1)")
                e = int(input("Informe um número [e], tal que, [e] seja co-primo com o produto (p-1).(q-1): "))
            create_public_key_file(n, e)
            print("Chave publica gerada com sucesso!")

        elif operation == 2:
            n = p * q
            FiN = int((p - 1) * (q - 1))
            file_path = input("Informe o diretório do arquivo a ser criptografado: ")
            if(correct_file(file_path, alfa)):
                try:
                    file = open(file_path, "r")
                    read_file = open(file_path, "r")
                    msg = read_file.read()
                except FileNotFoundError:
                    print("Arquivo não encontrado")

                if(crypt(read_file, msg, e, n) == 1):
                    print("Arquivo criptografado com sucesso")
                else:
                    print("Houve um erro na criptografia do arquivo")
        elif operation == 3:
            n = p * q
            d = findInverse(e, FiN)
            file_path = input("Informe o diretório do arquivo a ser descriptografado:")
            try:
                file = open(file_path, "r")
                cryptMsg = file.read()
                file.close()
                decrypt(cryptMsg, d, n)
            except FileNotFoundError:
                print("Arquivo não encontrado")
        elif operation == 4:
            break
        else:
            print("Operação inválida")
header()
init()