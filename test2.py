import subprocess
import os
import io
import pyautogui as pg



def user_read(a): # Чтение папки на наличие файлов с правилами для ключей
    if os.path.exists(f'c:\DKCL\\{a}.txt'):
        read_file(a)
    else:
        a = input('Введите имя пользователя: ')
        # b = input('Введите пароль: ')
        user_read(a)


def open_file_address(word): # Открытие файла заполненого адресами ключей
    with io.open(f"c:\DKCL\\address.txt", encoding="utf8") as address:
        for line in address:
            if word in line:
                f = line.split('(')
                f = f[1]
                f = f.replace(")", '')
                f = f.replace("\n", '')
                f = f.replace(" ", '')
    return f


def read_file(a): # Чтение построчно файла
    with open(f"c:\DKCL\\{a}.txt", encoding="utf8") as file:  # Разбираем файл с ключами построчно
        for line in file:
            word = line.strip()
            f = open_file_address(word)
            start_dk(f)

def start_dk(f): # Запуск клиента
    subprocess.check_output(f"C:\DKCL\dkcl64.exe -t \"USE,{f}\"")
    pg.typewrite(["12345678"])
    returned_output = subprocess.check_output(f'C:\Program Files\Crypto Pro\CSP\csptest.exe -keyset -enum_cont -verifycontext -fqcn -machinekeys')
    c = returned_output.decode("utf-8")
    print(c)
    subprocess.check_output(f"C:\DKCL\dkcl64.exe -t \"STOP USING,{f}\"")
    # pg.typewrite(["enter"])




if __name__ == '__main__':
    a = input('Введите имя пользователя: ')
    # b = input('Введите пароль: ')
    # cmd = "C:\DKCL\dkcl64.exe"
    # subprocess.check_output(cmd)
    subprocess.check_output(f"C:\DKCL\dkcl64.exe -t \"STOP USING ALL\"")
    # pg.typewrite(["enter"])
    user_read(a)