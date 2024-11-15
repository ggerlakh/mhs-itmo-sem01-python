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

Если на вход скрипту `nl.py ` передается файл, то для сравнения вывода скрипта `python3 nl.py <filename>` с командой `nl -b a <path_to_file>` можно использовать следующую команду в (которая подразумевает наличие установленного `vimdiff`, вместо `README.md` можно подставить путь до другого файла)
```bash
nl -b a README.md > artifacts/t1.txt && python3 nl.py README.md > artifacts/t2.txt && vimdiff artifacts/t1.txt artifacts/t2.txt
```

Пример работы работы скрипта `nl.py`
![nl.py demo](https://github.com/ggerlakh/mhs-itmo-sem01-python/blob/main/hw_1/artifacts/nl_artifact1.png)

## Скрипт tail.py

## Скрипт wc.py