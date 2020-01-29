import sys

alfa = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

n = int(sys.argv[1])
e = int(sys.argv[2])
file_path = sys.argv[3]

def crypt(read_file, msg, e, n):
    end = len(msg)
    cryptMsg = ""
    for i in range(end):
        m = msg[i]
        #fórmula padrao para criptografrar
        cryptMsg += str(pow((alfa.index(m) + 2), e, n)) # pois estamos indexando do 2 ao 28 (precisamos avançar 2 unidades)
        if(i + 1 < end):
            cryptMsg += ' ' #separador, para saber quem é quem
    try:
        crypt_file = open("EncryptFile.txt", "w")
        crypt_file.write(cryptMsg)
        crypt_file.close()
        return 1
    except FileNotFoundError:
        print("Houve um erro ao criar o arquivo, tente novamente")
        return -1
def correct_file(file_path, alfa):
    try:
        file = open(file_path, "r")
        msg = file.read().upper() #convertendo tudo para maiusculo
        file.close()
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return False
    i = 0
    end = len(msg)
    valid = ""
    while i < end:
        if(msg[i] in alfa):
            valid += msg[i]
        i += 1
    try:
        file = open(file_path, "w")
        file.write(valid)
        file.close()
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return False
    return True
def init():
    if(correct_file(file_path, alfa)):
        try:
            file = open(file_path, "r")
            read_file = open(file_path, "r")
            msg = read_file.read()
        except FileNotFoundError:
            print('Arquivo não encontrado')
        if(crypt(read_file, msg, e, n) == 1):
            print('Arquivo criptografado com sucesso')
        else:
            print('Houve um erro na criptografia do arquivo')
    else:
        print('Houve um erro na validação do arquivo, tente novamente')
init()