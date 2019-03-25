import os

def acceptCommand():  # проверка на ввод номера
    kk = '1234567'
    while True:
        s = input('Выберите пункт меню: ')
        if s in kk:
            return s
        else:
            continue

def runCommand(command, path):
    if command == 1:
        return moveUp()
    elif command == 2:
        return up()
    elif command == 3:
        return down()
    elif command == 4:
        return countFiles(path)
    elif command == 5:
        return countBytes(path)
    elif command == 6:
        return findFiles(path)
    elif command == 7:
        return 'Выход выполнен.'



def countFiles(path, a=0):
    for root, dirs, files in os.walk(path):
        if len(dirs) == 0:
            a += len(files)
            return a
        a += len(files)
    return countFiles(path, a)


def countBytes(path, a=0):
    for root, dirs, files in os.walk(path):
        if '.idea' not in dirs:
            if len(dirs) == 0:
                for i in files:
                    a += os.path.getsize(i)
                return a

            else:
                for i in files:
                    a += os.path.getsize(i)
                return countBytes(path, a)
        else:
            continue


def up():  # переход вверх из папки
    os.chdir('..')
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        print('root:', root, 'dirs:', dirs, 'files:', files)

def down():
    papka = input('Введите имя папки, в которую хотите перейти: ')
    while True:
        try:
            a = os.getcwd()
            os.chdir(r'%s\%s'%(a, papka))
            j = os.getcwd()
            print(j)
            break
        except:
            papka = input('Такой папки не существует, введите еще раз: ')


def moveUp():  # вывод каталога
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        print('root:', root, 'dirs:', dirs, 'files:', files)

def findFiles(path):
    target = input('Введите имя файла: ')
    lst = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if target in i:
                lst.append(os.path.abspath(i))
                return lst
            else:
                continue


def main():
    MENU = 'C:\Python34\n' \
           '1. Просмотр каталога\n' \
           '2. На уровень вверх \n' \
           '3  На уровень вниз\n' \
           '4  Количество файлов и каталогов\n' \
           '5  Размер текущего каталога (в байтах)\n' \
           '6  Поиск файла\n' \
           '7  Выход из программы\n'
    print(MENU)
    a = int(input('Выберите пункт меню: '))
    path = os.getcwd()
    if a  == 7:
        print(runCommand(a, path))
    while a != 7:
        print(runCommand(a, path))

        MENU = 'C:\Python34\n' \
               '1. Просмотр каталога\n' \
               '2. На уровень вверх \n' \
               '3  На уровень вниз\n' \
               '4  Количество файлов и каталогов\n' \
               '5  Размер текущего каталога (в байтах)\n' \
               '6  Поиск файла\n' \
               '7  Выход из программы\n'
        print(MENU)
        a = int(input('Выберите пункт меню: '))
        path = os.getcwd()



if __name__ == '__main__':
    main()