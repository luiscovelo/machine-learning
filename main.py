from Util import get_and_validate_args, clean_screen
from Preprocessor import generate_sheet

import ClassifierLogisticRegression
import ClassifierDummyClassifier
import ClassifierLinearSVC
import ClassifierRandomForestClassifier
import ClassifierLinearRegression
import ClassifierKNeighborsClassifier
import ClassifierMultinomialNB
import ClassifierGaussianNB
import ClassifierDecisionTreeClassifier
import ClassifierMLPClassifier
import ClassifierSVC

import os


def main():

    args = get_and_validate_args()
    results = []

    if generate_sheet():

        clean_screen()
        print("\nPara a URL informada: " + args.url + "\n")

        if args.model == "LogisticRegression":
            response = ClassifierLogisticRegression.ClassifierLogisticRegression(args.url).classifier()

        if args.model == "DummyClassifier":
            response = ClassifierDummyClassifier.ClassifierDummyClassifier(args.url).classifier()

        if args.model == "LinearSVC":
            response = ClassifierLinearSVC.ClassifierLinearSVC(args.url).classifier()

        if args.model == "RandomForestClassifier":
            response = ClassifierRandomForestClassifier.ClassifierRandomForestClassifier(args.url).classifier()

        if args.model == "LinearRegression":
            #response = ClassifierLinearRegression.ClassifierLinearRegression(args.url).classifier()
            print("Algoritmo com problema, tente outro algoritmo.")
            exit()

        if args.model == "KNeighborsClassifier":
            response = ClassifierKNeighborsClassifier.ClassifierKNeighborsClassifier(args.url).classifier()

        if args.model == "MultinomialNB":
            response = ClassifierMultinomialNB.ClassifierMultinomialNB(args.url).classifier()

        if args.model == "GaussianNB":
            response = ClassifierGaussianNB.ClassifierGaussianNB(args.url).classifier()

        if args.model == "DecisionTreeClassifier":
            response = ClassifierDecisionTreeClassifier.ClassifierDecisionTreeClassifier(args.url).classifier()

        if args.model == "SVC":
            response = ClassifierSVC.ClassifierSVC(args.url).classifier()

        if args.model == "MLPClassifier":
            response = ClassifierMLPClassifier.ClassifierMLPClassifier(args.url).classifier()

        if args.model == "all" or args.model == "best":

            results.append(ClassifierLogisticRegression.ClassifierLogisticRegression(args.url).classifier())
            results.append(ClassifierDummyClassifier.ClassifierDummyClassifier(args.url).classifier())
            results.append(ClassifierLinearSVC.ClassifierLinearSVC(args.url).classifier())
            results.append(ClassifierRandomForestClassifier.ClassifierRandomForestClassifier(args.url).classifier())
            results.append(ClassifierKNeighborsClassifier.ClassifierKNeighborsClassifier(args.url).classifier())
            results.append(ClassifierMultinomialNB.ClassifierMultinomialNB(args.url).classifier())
            results.append(ClassifierGaussianNB.ClassifierGaussianNB(args.url).classifier())
            results.append(ClassifierDecisionTreeClassifier.ClassifierDecisionTreeClassifier(args.url).classifier())
            results.append(ClassifierSVC.ClassifierSVC(args.url).classifier())
            results.append(ClassifierMLPClassifier.ClassifierMLPClassifier(args.url).classifier())

            if args.model == "all":
                print_result(results, 2)

            if args.model == "best":
                print_best_alg(results)

        else:
            print_result(response, 1)


def print_result(results, qtde_for):

    if qtde_for == 1:

        for alg in results:

            print("-Usando ["+alg+"] a notícia foi classificada como:")
            print("\t-Categoria: " + results[alg]["categ"])
            print("\t-Probabilidade: {:.1%}".format(results[alg]["probab"]))

    else:

        for result in results:
            for alg in result:

                print("\n-Usando [" + alg + "] a notícia foi classificada como:")
                print("\t-Categoria: " + result[alg]["categ"])
                print("\t-Probabilidade: {:.1%}".format(result[alg]["probab"]))


def print_best_alg(results):

    best_alg = ""
    best_categ = ""
    best_score = 0.0

    for result in results:
        for alg in result:

            if result[alg]["probab"] >= best_score:
                best_score = float(result[alg]["probab"])
                best_categ = result[alg]["categ"]
                best_alg = alg

    print("\n-Usando o melhor modelo [" + best_alg + "] a notícia foi classificada como:")
    print("\t-Categoria: " + best_categ)
    print("\t-Probabilidade: {:.1%}".format(best_score))


if __name__ == "__main__":
    main()
