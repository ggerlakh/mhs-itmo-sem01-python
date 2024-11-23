# HW_2

Выполнение второго ДЗ

## latex_gen_ggerlakh

Библиотека для генерации .tex кода. (https://test.pypi.org/project/latex-gen-ggerlakh/)  

Основная функциональность описана в модуле `src/latex_gen_ggerlakh/convert_to_tex.py`:

- `def generate_tex_doc(tex_content: str) -> str` - функция которая обрамлет входную строку (предполагаемую с содержанием tex контента), стандартыми директивами для описания .tex файла

- `def generate_table(inp_list: List[List[any]]) -> str` - функция которая генерирует таблицу в .tex формате на основе переданного двумерного списка для вставки в документ

- `def generate_picture(pic_png_path: str) -> str:` - функция которая генерирует .tex код для вставки картинки `pic_png_path` в документ

- `def convert_tex_to_pdf(path_to_tex: str) -> None:` - функция которая конвертирует .tex файл в .pdf файл (требуется наличие программы `pdflatex` для конвертации .tex в .pdf)


## Пример использования

Пример использования библиотеки описан в файле `src/latex_gen_ggerlakh/example.py`

```bash
cd src/latex_gen_ggerlakh
python3 example.py 
```

## Инструкция по установке

Для установки библиотеки можно использовать следующую команду:
```bash
pip install -i https://test.pypi.org/simple/ latex-gen-ggerlakh
```

## Docker

Также для тестирования библиотеки можно собрать docker образ из `Dockerfile`
```bash
docker build . -t latex-gen-ggerlakh-image 
```
и запустить его
```bash
docker run -it latex-gen-ggerlakh-image bash
```