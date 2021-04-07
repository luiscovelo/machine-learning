Trabalho de Machine Learning
-
A aplicação visa classificar a categoria de uma dada noticia, esta deve ser informada pelo usuário no momento da execução da aplicação.

Categorias treinadas:
* ciencia-e-saude
* tecnologia
* agro
* educacao
* politica
* economia

> Atenção, caso <b>não</b> exista a base de dados completa (*files/urls-complete.csv*) contendo o texto das notícias para treino e teste, na primeira execução de uma classificação a aplicação irá baixar o conteúdo necessário utilizando a planilha (*files/urls.csv*) como base. Caso não deseje aguardar a aplicação realizar a captura do conteúdo, faça o download de uma base já populada disponível em [download](https://drive.google.com/file/d/1Y6XbU9yOV6m70xXA2WuGSwSPaes3zoNY/view?usp=sharing "Download da planilha ja populada para classificação.").

> Observação: Ao executar a classificação de uma notícia, o modelo treinado e testado é armazenado em disco (*files/saved_model*), desta forma ao executar novamente uma classificação a aplicação não precisará treinar e testar a base de dados, portanto conseguimos melhorar a performance em processar o resultado para o usuário.

<br>
Bora para a prática!
-
#
Atenção para os comandos _pip_ e o _py_, estes podem sofrer alterações conforme o seu sistema operacional, possíveis alternativas:
* pip
* pip3
* python
* python3
#

Clone a aplicação em um diretório de sua preferência:
```
git clone git@github.com:luiscovelo/machine-learning.git
```

Como instalar:

```python
pip install -r requirements.txt
```

Como usar:

```python
py main.py --how_to_use app 
```

Modelos de classificação disponíveis:

```python
py main.py --list alg 
```

Classificando uma notícia utilizando todos os modelos disponíveis:

```python
py main.py --url https://www.moneytimes.com.br/gestora-brasileira-hashdex-divulga-cronograma-para-seu-etf-de-bitcoin/ --model all
```

Classificando uma notícia com todos os modelos e verificando qual modelo obteve a melhor taxa de acerto:

```python
py main.py --url https://www.moneytimes.com.br/gestora-brasileira-hashdex-divulga-cronograma-para-seu-etf-de-bitcoin/ --model best
```

Classificando uma notícia com um modelo específico:
* DecisionTree:

    ```python
    py main.py --url https://www.moneytimes.com.br/gestora-brasileira-hashdex-divulga-cronograma-para-seu-etf-de-bitcoin/ --model DecisionTreeClassifier
    ```
* Dummy:

    ```python
    py main.py --url https://www.moneytimes.com.br/gestora-brasileira-hashdex-divulga-cronograma-para-seu-etf-de-bitcoin/ --model DummyClassifier
    ```
* GaussianNB:

    ```python
    py main.py --url https://www.moneytimes.com.br/gestora-brasileira-hashdex-divulga-cronograma-para-seu-etf-de-bitcoin/ --model GaussianNB
    ```

* KNeighbors:

    ```python
    py main.py --url https://www.moneytimes.com.br/gestora-brasileira-hashdex-divulga-cronograma-para-seu-etf-de-bitcoin/ --model KNeighborsClassifier
    ```

* LinearSVC:

    ```python
    py main.py --url https://www.moneytimes.com.br/gestora-brasileira-hashdex-divulga-cronograma-para-seu-etf-de-bitcoin/ --model LinearSVC
    ```

* LogisticRegression:

    ```python
    py main.py --url https://www.moneytimes.com.br/gestora-brasileira-hashdex-divulga-cronograma-para-seu-etf-de-bitcoin/ --model LogisticRegression
    ```

* MLP:

    ```python
    py main.py --url https://www.moneytimes.com.br/gestora-brasileira-hashdex-divulga-cronograma-para-seu-etf-de-bitcoin/ --model MLPClassifier
    ```

* MultinomialNB:

    ```python
    py main.py --url https://www.moneytimes.com.br/gestora-brasileira-hashdex-divulga-cronograma-para-seu-etf-de-bitcoin/ --model MultinomialNB
    ```

* RandomForest:

    ```python
    py main.py --url https://www.moneytimes.com.br/gestora-brasileira-hashdex-divulga-cronograma-para-seu-etf-de-bitcoin/ --model RandomForestClassifier
    ```

* SVC:

    ```python
    py main.py --url https://www.moneytimes.com.br/gestora-brasileira-hashdex-divulga-cronograma-para-seu-etf-de-bitcoin/ --model SVC
    ```