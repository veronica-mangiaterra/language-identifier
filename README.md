LANGUAGE IDENTIFIER (Project for 'Computational skills for text analysis' class at UniTrento, MSc in Cognitive Science)
    The aim of this project is to train a classifier that identifies in which language a text is written.
    The work is organized following these steps:
    1. Scraping,
    2. Preprocessing,
    3. Vectorization and training of the model,
    4. Evaluation
    
    1. SCRAPING
    I used Selenium to navigate through different pages and Requests and BeautifulSoup to get the text from the pages
    
    2. PRE-PROCESSING
Pre-processing consists of two phases since, from the 4 million words in the raw text, two types of data need to be derived.

First of all, the list of the 5000 most frequent words for each language must be obtained. In order to achieve that, we pre-process the text, removing all non-significant elements such as numbers, punctuation and non-Latin characters. After that, we store the data in a dictionary according to each word's frequency and we keep the 5000 most frequent words. The words obtained are now stored in a dataframe, appropriately labelled with the language.

Secondly, we want to obtain a dataframe, in which all the sentences present in our four corpora are reported, also labelled with the language in which they are written. To do that, we take the original raw text and store it in a pandas DataFrame. Then, we pre-process the text in the dataframe and store the text in four list so that it is subsequently possible to create a dataframe that contains all the sentences in all four languages.

3. VECTORIZATION AND TRAINING OF THE MODEL
There are several ways to vectorize a text in order to get information readable by a model. In this project TF-IDF vectorization was used.

In information retrieval, tf–idf short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. This is very common algorithm to transform text into a meaningful representation of numbers which is used to fit machine algorithm for prediction.

First, we consider as features the 5000 most frequent words only. To identify the language in which a text is writter, we will train a classifier, in particular a Naive Bayes classifier. NB classifier is one of the simple "probabilistic classifiers" based on applying Bayes' theorem with strong independence assumptions between the features.

Then we train the model, fitting it to two kinds of data: the tf-idf matrix of the 5000 most frequent words and the labels associated with each words (namely, the languages). We test the model on the sentences

At a later stage, we tried to consider many more features. We divided all sentences into a train data set and a test data set (80%-20%). All the sentences are once again vectorized. Then, we fit the classifier to the data: the matrix of the 80% of our corpora and the label associated with each sentence. We test the model on the remaining sentences.

4. EVALUATION
In order to evaluate the model, we calculate the ACCURACY

(TP + TN)/(TP + TN + FP + FN)

and the CONFUSION MATRIX that returns a representation of classification accuracy. Each column of the matrix represents the predicted values, while each row represents the actual values

CONCLUSION¶
A qualitative analysis of the errors produced by the model leads to the conclusion that it fail to recognize the correct language when the sentence provided is too short (a single letter for example). In addition, some sentences are labelled with a certain language, because they are from a Wikipedia web page in that language but they are not really written in that language; in this cases also the model failed but it cannot be considered a true failure but a problem of the dataset. It could be interesting to test our model on data that are certainly written in the language reported in their label, scraping from wikipedia does not assure this.
