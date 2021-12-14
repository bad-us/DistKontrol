import subprocess

a = None
b = None

def write_file():
    # cmd = "C:\DKCL\dkcl64.exe -t \"LIST\" -r=c:\DKCL\\1.txt" # Поставил пока в комент Для работы с файлом нужно разкоментировать
    # subprocess.check_output(cmd)  # returned_output содержит вывод в виде строки байтов
    # print('Сохранение в файл:', returned_output.decode("utf-8"))  # Преобразуем байты в строку
    read_file()

def read_file():
    word = "-->"
    d = []
    f = []
    i = 0
    with open("c:\DKCL\\1.txt", encoding="utf8") as file: # Разбираем файл с ключами построчно
        for line in file:
            if word in line:
                f = line.split('   -->')
                f = f[1]
                f = f.split('(')
                a = f[0]
                print(a)
                f = f[1]
                f = f.replace(")", '')
                f = f.replace("\n", '')
                f = f.replace(" ", ',')
                # up_and_write(f)
                b = up_and_write(f)
                write_final_file(a, b)
    return

def up_and_write(f):
    # word_2_file = "JaCarta"
    p = []
    cmd = f"C:\DKCL\dkcl64.exe -t \"USE,{f}12345678\"" #12345678 пароль пользователя
    subprocess.check_output(cmd)

    # cmd = "C:\Program Files\Crypto Pro\CSP\csptest.exe -keyset -enum_cont -verifycontext -fqcn -machinekeys"
    # returned_output = subprocess.check_output(cmd)
    # b = returned_output.decode("utf-8")
    # b = b.split(' ')
    # b = b[14]
    # b = b.replace('\r\nOK.\r\nTotal:', '') #Вытаскиваем ид ключа
    cmd = "C:\Program Files\Crypto Pro\CSP\csptest -keyset -uniq"
    returned_output = subprocess.check_output(cmd)
    b = returned_output.decode("utf-8")
    b = b.split(' ')
    b = b[20]
    b = b.replace('\nSignature', '') #Вытаскиваем уникальное имя ключа
    cmd = f"C:\DKCL\dkcl64.exe -t \"STOP USING,{f}\""
    subprocess.check_output(cmd)
    return b

def write_final_file(a,b):
    final = open("c:\DKCL\\Final_file.txt", "a", encoding="utf8")
    # b = b.split('\')
    # a = f'{a} - {b}\n'
    b = b.split('\\')
    b = b[1]
    b = b.replace('JACARTA_', '')
    a = f'{a} - {b}\n' # Выделение только адреса ключа
    final.write(a)
    final.close()
    return


if __name__ == '__main__':
    cmd = f"C:\DKCL\dkcl64.exe -t \"STOP USING ALL\""
    subprocess.check_output(cmd)
    write_file()