from pathlib import Path

print('Path: ', Path(__file__).resolve())


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
           # pathlib Objekt mit überladenem OPerator

# Datenpipeline bauen
# ETL Datapipeline: Extract, Transform, Load


def read_data(file_name):
    """große Datei einlesen"""
    with open(DATA_DIR / file_name) as f:
     #   content = f.read()     #Alles anzeigen
    #   print(content)
        for line in f:
            print(line)     # Alles als Zeilen


if __name__ == '__main__':
    read_data('techcrunch.csv')



