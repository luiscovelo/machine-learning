import argparse
import joblib
from pathlib import Path

import os

_PATH_COMPLETE_SHEET = "files/urls-complete.csv"
_PATH_BASE_SHEET = "files/urls.csv"
_TEST_SIZE = 0.25  # teste com 25% dos dados
_TRAIN_SIZE = 0.75  # treino com 75% dos dados
_RANDOM_STATE = 20
_DEBUG = 0
_USE_MODEL_SAVE = 1


def get_path_complete_sheet():
    return _PATH_COMPLETE_SHEET


def get_path_base_sheet():
    return _PATH_BASE_SHEET


def get_test_size():
    return _TEST_SIZE


def get_train_size():
    return _TRAIN_SIZE


def get_random_state():
    return _RANDOM_STATE


def get_debug():
    return _DEBUG


def logging(msg):
    if get_debug():
        print("[log]: " + msg)


def print_result(msg):
    if get_debug():
        print("[result]: " + msg)


def list_alg():
    list = {
        "DummyClassifier",
        "LinearSVC",
        "SVC",
        "RandomForestClassifier",
        #"LinearRegression",
        "LogisticRegression",
        "KNeighborsClassifier",
        "MultinomialNB",
        "GaussianNB",
        "DecisionTreeClassifier",
        "MLPClassifier"
    }

    os.system('cls')
    print("Algoritmos suportados:")
    for alg in list:
        print("\t- " + alg)

    exit(0)


def print_how_to_use():

    url_valid = "https://g1.globo.com/educacao/noticia/2021/04/05/ministro-da-educacao-defende-homeschooling-em-audiencia-e-diz-que-socializacao-da-crianca-pode-ser-na-igreja.ghtml"

    os.system('cls')
    print("\nPara utilizar o app de classifição siga as instruções abaixo:\n")
    print("Paramêtro --url: \n\t- deve ser informado a url da notícia a ser classificada.")
    print("Parametro --model:")
    print("\t- caso deseja especificar um algoritmo, digite o comando {py main.py --list alg} para obter o nome os algoritmos disponíveis, ex: py main.py --url {url_noticia} --model LogisticRegression")
    print("\t- informe o valor {all} caso deseje mostrar o resultado com todos algoritmos.")
    print("\t- informe o valor {best} caso deseje mostrar o resultado com o algoritmo de maior acerto.")
    print("\nExemplos de comandos válidos:")
    print("\tComando com alg específico: \n\t\t py main.py --url " + url_valid + " --model LogisticRegression")
    print("\tComando com todos os algs: \n\t\t py main.py --url " + url_valid + " --model all")
    print("\tComando com o melhor alg: \n\t\t py main.py --url " + url_valid + " --model best")
    exit()


def get_and_validate_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--model", help="Algoritmo a ser usado na classificação.")
    parser.add_argument("--url", help="URl da notícia a ser classficada.")
    parser.add_argument("--list", help="Lista de algoritimos de classificação.", required=False, default="")
    parser.add_argument("--how_to_use", help="Auxilia em como utilizar a aplicação.", required=False, default="")

    args = parser.parse_args()

    if args.how_to_use == 'app':
        print_how_to_use()

    if args.model == '':
        logging("Argumento --model invalido.")
        exit(0)

    if args.url == '':
        logging("Argumento --url invalido.")
        exit(0)

    if args.list == "alg":
        list_alg()

    args.model = args.model.replace("'", "")
    args.url = args.url.replace("'", "")

    return args


def load_model(filename):
    if not _USE_MODEL_SAVE:
        return False

    if Path(filename).is_file():
        logging("Utilizando modelo de treino salvo em disco.")
        return joblib.load(filename)
    else:
        return False


def save_model(pipe, filename):

    try:
        joblib.dump(pipe, filename)
    except Exception as err:
        print("Erro ao salvar o modelo.", err)
