import csv
import logging
import chardet

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler()])

def detectar_encoding(csv_file):
    encodings = ['utf-8', 'iso-8859-1', 'windows-1252']
    raw_data = csv_file.read()
    
    for encoding in encodings:
        try:
            csv_file.seek(0)
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

def detectar_delimitador(csv_data_string_io):
    try:
        amostra = ''.join([csv_data_string_io.readline() for _ in range(5)])
        csv_data_string_io.seek(0)
        delimitadores = [";", ",", "\t"]
        delimitador_detectado = max(delimitadores, key=amostra.count)
        logging.info(f"Delimitador detectado: {delimitador_detectado}")
        return delimitador_detectado
    except UnicodeDecodeError as e:
        logging.error(f"Erro de decodificação ao detectar o delimitador: {e}")
        raise
    except Exception as e:
        logging.error(f"Erro inesperado ao detectar o delimitador: {e}")
        raise

def detectar_header(csv_data_string_io):
    try:
        csv_data_string_io.seek(0)
        sample = csv_data_string_io.read(2048)
        sniffer = csv.Sniffer()
        has_header = sniffer.has_header(sample)
        csv_data_string_io.seek(0)
        logging.info(f"Possui header: {has_header}")
        return has_header
    except csv.Error as e:
        logging.error(f"Erro do CSV ao detectar header: {e}")
        raise
    except Exception as e:
        logging.error(f"Ocorreu um erro inesperado ao detectar se possui header: {e}")
        raise