import chardet
import subprocess

ARGS = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for ping_res in ARGS:
    ping_proc = subprocess.Popen(ping_res, stdout=subprocess.PIPE)
    print(ping_proc.stdout)

    for line in ping_proc.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding'])
        print(line)