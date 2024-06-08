import csv
import logging
import chardet

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler()])

def detectar_encoding(arquivo_csv):
    encodings = ['utf-8', 'iso-8859-1', 'windows-1252']
    raw_data = arquivo_csv.read()
    
    for encoding in encodings:
        try:
            arquivo_csv.seek(0)
            encoding_detectado = raw_data.decode(encoding)
            logging.info(f"Decodificado com sucesso usando o encoding: {encoding}")
            return encoding_detectado
        except UnicodeDecodeError:
            logging.warning(f"Falha ao decodificar usando o encoding: {encoding}")
            continue

    encoding_detectado = chardet.detect(raw_data)
    encoding = encoding_detectado['encoding']
    
    if encoding:
        logging.info(f"Encoding detectado usando chardet: {encoding}")
        return encoding_detectado.decode(encoding)
    else:
        logging.error("Não foi possível detectar o encoding do arquivo CSV.")
        raise UnicodeDecodeError("Não foi possível detectar o encoding do arquivo CSV.")

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