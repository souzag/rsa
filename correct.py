import os

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
