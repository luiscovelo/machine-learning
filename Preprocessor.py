import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from goose3 import Goose
import unicodedata
import re

from Util import *


def generate_sheet():
    # Caso não exista a planilha com os textos:
    # é lido a planilha base, obtido os textos e gerado uma nova planilha contendo os textos.
    if not Path(get_path_complete_sheet()).is_file():

        nltk.download("stopwords")
        nltk.download("punkt")

        # Lendo a planilha utilizando separador ;
        dataframe = pd.read_csv(get_path_base_sheet(), sep=";")
        dataframe["texto"] = ""

        for index, row in dataframe.iterrows():

            text = get_text_sanitized_from_url(row["link"])

            # Adicionando o texto da materia no dataframe na coluna 'texto'
            dataframe.at[index, "texto"] = text

            if text == "":
                dataframe = dataframe.drop(index)

            print(str(index) + ': ' + row['link'])

        if dataframe.to_csv(get_path_complete_sheet(), sep=";"):
            generated = True
        else:
            generated = False

        return generated

    else:
        return True


def get_text_sanitized_from_url(url):
    logging("Criando uma lista com as stop words da língua Portuguesa.")
    list_stopwords = set(stopwords.words("portuguese"))

    logging("Abrindo conexão com o Gooose.")
    goose = Goose()

    logging("Buscando a notícia com base na URL.")
    notice = goose.extract(url)

    # Seto o texto da materia
    text = notice.cleaned_text

    logging("Limpando caracteres invalidos.")
    # Remove caracter especial, acentuação, etc
    text = str(unicodedata.normalize("NFKD", text).encode("ASCII", "ignore"))

    logging("Removendo todo caracter na qual não seja LETRA.")
    # Mantem somente letras no conteudo do texto
    text = re.sub(r"[^A-Za-z]+", ' ', text)

    logging("Convertendo o texto em minusculo.")
    # Seto o texto para minusculo
    text = text.lower()

    logging("Transformando o texto em um array de palavras.")
    # Transforma o texto em uma lista separando palavra por palavra
    text_words = word_tokenize(text)

    logging("Removendo do texto todas as stops words.")
    # Remove todas as stops words do texto
    text = [word for word in text_words if not word in list_stopwords and len(word) > 2]

    logging("Convertando o array de palavras higienizados em uma só string separando por espaço.")
    # Transforma a lista de palavras em uma unica string

    text = (" ").join(text)

    logging("Fechando conexão com o Gooose.")
    goose.close()

    return text