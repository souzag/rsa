import sys

alfa = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

p = int(sys.argv[1])
q = int(sys.argv[2])
e = int(sys.argv[3])
file_path = sys.argv[4]

def findInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1

    if (m == 1) : 
        return 0

    while (a > 1) : 

        # q is quotient 
        q = a // m 

        t = m 

        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 

        # Update x and y 
        y = x - q * y 
        x = t 


    # Make x positive 
    if (x < 0) : 
        x = x + m0 

    return x 
def decrypt(cryptMsg, d, n):
    decryptMsg = ""
    i = 0
    end = len(cryptMsg)
    while i < end:
        current = ""
        while i < end and cryptMsg[i] != ' ':
            current += cryptMsg[i]
            i += 1
        i += 1
        current = int (current)
        decryptMsg += alfa[pow(current, d, n) - 2] # pois estavamos indexando do 2 ao 28 (precisamos voltar 2 indices)
    try:
        file = open("DecryptFile.txt", "w")
        file.write(decryptMsg)
        file.close()
    except FileNotFoundError:
        print("Não foi possivel criar o arquivo descriptografado, tente novamente")
def init():
    FiN = (p - 1) * (q - 1)
    n = p * q
    d = findInverse(e, FiN)
    try:
        file = open(file_path, "r")
        cryptMsg = file.read()
        file.close()
        decrypt(cryptMsg, d, n)
        print('Arquivo descriptografado com sucesso')
    except FileNotFoundError:
        print("Arquivo não encontrado")
init()