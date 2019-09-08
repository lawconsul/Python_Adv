print(f"\n2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.")
str1 = b"class"
str2 = b"function"
str3 = b"method"
print(f"str1: {str1}, type={type(str1)}, len={len(str1)}")
print(f"str2: {str2}, type={type(str2)}, len={len(str2)}")
print(f"str3: {str3}, type={type(str3)}, len={len(str3)}")

print(f"\n3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.")
str1 = b"attribute"
# str2 = b"класс"
# str3 = b"функция"
str4 = b"type"
print(f"str1: {str1}, type={type(str1)}, len={len(str1)}")
# print(f"str2: {str2}, type={type(str2)}, len={len(str2)}")
# print(f"str3: {str3}, type={type(str3)}, len={len(str3)}")
print(f"str4: {str4}, type={type(str4)}, len={len(str4)}")

print(f"\n4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).")
str1 = "разработка"
str2 = "администрирование"
str3 = "protocol"
str4 = "standard"
str1 = str1.encode('utf-8')
print(f"str1: {str1}, type={type(str1)}, len={len(str1)}")
str1 = str1.decode('utf-8')
print(f"str1: {str1}, type={type(str1)}, len={len(str1)}")

str2 = str2.encode('utf-8')
print(f"str2: {str2}, type={type(str2)}, len={len(str2)}")
str2 = str2.decode('utf-8')
print(f"str2: {str2}, type={type(str2)}, len={len(str2)}")

str3 = str3.encode('utf-8')
print(f"str3: {str3}, type={type(str3)}, len={len(str3)}")
str3 = str3.decode('utf-8')
print(f"str3: {str3}, type={type(str3)}, len={len(str3)}")

str4 = str4.encode('utf-8')
print(f"str4: {str4}, type={type(str4)}, len={len(str4)}")
str4 = str4.decode('utf-8')
print(f"str4: {str4}, type={type(str4)}, len={len(str4)}")

print(f"\n5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.")
import subprocess
args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
if 0 > 1:
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))

print(f"\n6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.")
import locale
def_coding = locale.getpreferredencoding()
print(f"def_coding: {def_coding}")

file_name = "test_file.txt"
str1 = ["сетевое программирование", "сокет", "декоратор"]

with open(file_name, "w") as f_n:
    for st in str1:
        f_n.write(f"{st}\n")
    f_n.close()
    print(f_n)

# with open(file_name, encoding='cp866') as f_n:
with open(file_name, encoding='utf-8') as f_n:
    for st in f_n:
        print(st, end='')