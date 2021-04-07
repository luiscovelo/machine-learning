import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import FunctionTransformer

from Preprocessor import *

PATH_SAVE_MODEL = "files/saved_model/GaussianNB.sav"


class ClassifierGaussianNB:

    def __init__(self, url):
        self.url = url.replace("'", "")

    def test_and_train(self) -> Pipeline:

        dataframe = pd.read_csv(get_path_complete_sheet(), sep=";")
        dataframe = dataframe.drop("Unnamed: 0", axis=1)

        pipe = Pipeline([
            ("Vectorizer", CountVectorizer()),
            ("transformer", FunctionTransformer(lambda x: x.todense(), accept_sparse=True)),
            ("LogisticRegression", GaussianNB())
        ])

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
            dataframe.texto, dataframe.categ, stratify=dataframe.categ, train_size=get_train_size(),
            test_size=get_test_size(), random_state=get_random_state()
        )

        pipe.fit(x_train, y_train)

        accuracy = pipe.score(x_test, y_test)

        msg = "[treino-e-teste] Porcentagem de acerto com {:.0%} de dados para treinamento: {:.1%}" \
            .format(get_train_size(), accuracy)

        logging(msg)

        return pipe

    def predict(self, pipe):

        words = get_text_sanitized_from_url(self.url)
        predictCategory = pipe.predict([words])

        predictProbab = zip(pipe.classes_, pipe.predict_proba([words])[0])
        predictProbab = sorted(predictProbab, key=lambda tup: tup[1], reverse=True)

        msg = "Melhor categoria usando GaussianNB: " + predictCategory[0] + " com {:.1%} de acerto. ".format(predictProbab[0][1])

        print_result(msg)

        response = {
            "GaussianNB": {
                "categ": predictCategory[0],
                "probab": predictProbab[0][1]
            }
        }

        return response

    def classifier(self):

        try:

            pipe = self.test_and_train()
            return self.predict(pipe)

        except ValueError as err:
            print("Ocorreu um erro: " + __name__, err)