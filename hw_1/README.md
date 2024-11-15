# HW_1

Выполнение первого ДЗ

## Создание виртуального окружения

1. Окружение создается через `conda`  

   ```bash
   conda create -n hw_1 -c conda-forge python=3.12 click
   ```
2. Для активации окружения используется следующая команда:
   
   ```bash
   conda activate hw_1
   ```
3. Для деактивации:

   ```bash
   conda deactivate
   ```

## Скрипт nl.py

```bash
Usage: nl.py [OPTIONS] [FILENAME]

  Simple line numbering filter that works like `nl -b a`

Options:
  --help  Show this message and exit.
```

- Если на вход скрипту `nl.py ` передается файл, то для сравнения вывода скрипта `python3 nl.py <filename>` с командой `nl -b a <path_to_file>` можно использовать следующую команду в (которая подразумевает наличие установленного `vimdiff`, вместо `README.md` можно подставить путь до другого файла)

  ```bash
  nl -b a README.md > artifacts/nl_t1.txt && python3 nl.py README.md > artifacts/nl_t2.txt && vimdiff artifacts/nl_t1.txt artifacts/nl_t2.txt
  ```
- Для сравнение вывода данных которые берутся из `stdin` можно использовать следующую команду в (которая подразумевает наличие установленного `vimdiff`, вместо `README.md` можно подставить путь до другого файла или другой `stdin`)  
  ```bash
  cat nl.py | nl -b a > artifacts/nl_t3.txt && cat nl.py | python3 nl.py > artifacts/nl_t4.txt && vimdiff artifacts/nl_t3.txt artifacts/nl_t4.txt
  ```

Пример работы работы скрипта `nl.py`
![nl.py demo](https://github.com/ggerlakh/mhs-itmo-sem01-python/blob/main/hw_1/artifacts/nl_artifact1.png)

## Скрипт tail.py

```bash
Usage: tail.py [OPTIONS] [FILENAMES]...

  Simple display the last part of a file that works like `tail` command
  without options.

Options:
  --help  Show this message and exit.
ggerlakh@MacBook-Air-Gleb hw_1 % 
```

- Если на вход скрипту `tail.py ` передается файл (файлы), то для сравнения вывода скрипта `python3 tail.py <filenames>` с командой `tail <path_to_files>` можно использовать следующую команду в (которая подразумевает наличие установленного `vimdiff`, вместо `README.md` и `tail.py` можно подставить путь до другого файла)  

  ```bash
  tail nl.py README.md > artifacts/tail_t1.txt && python3 tail.py nl.py README.md > artifacts/tail_t2.txt && vimdiff artifacts/tail_t1.txt artifacts/tail_t2.txt
  ```
- Для сравнения вывода данных которые берутся из `stdin` можно использовать следующую команду в (которая подразумевает наличие установленного `vimdiff`, вместо `README.md` можно подставить путь до другого файла или другой `stdin`)

  ```bash
  cat README.md | tail -17 > artifacts/tail_t3.txt && cat README.md | python3 tail.py > artifacts/tail_t4.txt && vimdiff artifacts/tail_t3.txt artifacts/tail_t4.txt
  ```

Пример работы работы скрипта `tail.py`
![tail.py demo](https://github.com/ggerlakh/mhs-itmo-sem01-python/blob/main/hw_1/artifacts/tail_artifact1.png)

## Скрипт wc.py
