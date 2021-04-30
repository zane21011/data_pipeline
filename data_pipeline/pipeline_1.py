from pathlib import Path
from typing import Generator

print('Path: ', Path(__file__).resolve())


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
           # pathlib Objekt mit überladenem OPerator

# Datenpipeline bauen
# ETL Datapipeline: Extract, Transform, Load

# Zeilenweise darstellen
# Zeilen ernten
# Kategorien einbauen
# Aus den Zeilen (strings) soll eine Liste werden)

def read_data(file_name: str) -> Generator:
    """große Datei einlesen"""
    with open(DATA_DIR / file_name) as f:
     #   content = f.read()     #Alles anzeigen
    #   print(content)
        for line in f:
            yield line          # erntet die Zeilen

# zu viele Daten!
# def split_line(g: Generator):
  #  result = []
   # for el in g:
    #    result.append(el.split())
    #return result

def split_line(g: Generator):
    result = (line.strip().split(",") for line in g)
    return result


def dictify(g: Generator):
    # print("Dict: ", g)
    header = next(g)        # die Zeiel mit den keys
    # print(next(g))
    return (dict(zip(header, line)) for line in g)




def load_data(file_name: str) -> Generator:
    file_generator = read_data(file_name)
    # print(next(file_generator))
    split_lines = split_line(file_generator)
    # print(split_lines)
    # print(next(split_lines))
    # print(next(split_lines))
    # print(next(split_lines))
    # result = dictify(split_lines)
    return dictify(split_lines)



if __name__ == '__main__':
    load_data('techcrunch.csv')



