import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

from Preprocessor import *

dict_categ = {
    "ciencia-e-saude": 1,
    "tecnologia": 2,
    "politica": 3,
    "agro": 4,
    "economia": 5,
    "educacao": 6
}

PATH_SAVE_MODEL = "files/saved_model/LinearRegression.sav"


class ClassifierLinearRegression:

    def __init__(self, url):
        self.url = url.replace("'", "")
        self.y_test = None

    def test_and_train(self) -> Pipeline:

        dataframe = pd.read_csv(get_path_complete_sheet(), sep=";")
        dataframe = dataframe.drop("Unnamed: 0", axis=1)

        dataframe["categ"] = dataframe["categ"].map(dict_categ)

        pipe = load_model(PATH_SAVE_MODEL)

        if not pipe:

            pipe = Pipeline([
                ("Vectorizer", CountVectorizer()),
                ("scaler", StandardScaler(with_mean=False)),
                ("LinearRegression", LinearRegression())
            ])

        else:
            return pipe

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
            dataframe.texto, dataframe.categ, stratify=dataframe.categ, train_size=get_train_size(),
            test_size=get_test_size(), random_state=get_random_state()
        )

        self.y_test = y_test

        pipe.fit(x_train, y_train)
        accuracy = pipe.score(x_test, y_test)

        msg = "[treino-e-teste] Porcentagem de acerto com {:.0%} de dados para treinamento: {:.1%}" \
            .format(get_train_size(), accuracy)

        logging(msg)

        save_model(pipe, PATH_SAVE_MODEL)

        return pipe

    def predict(self, pipe):

        words = get_text_sanitized_from_url(self.url)

        predictCategory = pipe.predict([words])

        #predictProbab = zip(pipe.get_params(), pipe.predict_proba([words])[0])
        #predictProbab = sorted(predictProbab, key=lambda tup: tup[1], reverse=True)

        #msg = "Melhor categoria usando LinearRegression: " + predictCategory[0] + " com {:.1%} de acerto. ".format(predictProbab[0][1])

        #print(msg)

    def classifier(self):

        pipe = self.test_and_train()
        self.predict(pipe)



