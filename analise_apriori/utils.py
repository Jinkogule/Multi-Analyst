import csv
import chardet

def detectar_encoding(csv_file):
    try:
        return csv_file.read().decode('utf-8')
    except UnicodeDecodeError:
        rawdata = csv_file.read()
        resultado = chardet.detect(rawdata)
        encoding = resultado['encoding'] if resultado['encoding'] else 'iso-8859-1'
        return rawdata.decode(encoding)

def remover_todos_zeros_da_lista(lista):
    return [x for x in lista if x != 0]

def detectar_delimitador(csv_string_io):
    amostra = ''.join([csv_string_io.readline() for _ in range(5)])
    csv_string_io.seek(0)
    delimitadores = [";", ",", "\t"]
    delimitador_detectado = max(delimitadores, key=amostra.count)
    return delimitador_detectado

def detectar_header(csv_string_io, delimiter):
    csv_string_io.seek(0)
    sample = csv_string_io.read(2048)
    sniffer = csv.Sniffer()
    has_header = sniffer.has_header(sample)
    csv_string_io.seek(0)
    return has_header