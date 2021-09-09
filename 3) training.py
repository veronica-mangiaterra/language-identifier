train_X = df_fivek['Text']   
train_y = df_fivek['Language']   
test_X = df_oneM['Text']
test_y = df_oneM['Language']

tfidfvectorizer = TfidfVectorizer(analyzer='word') #the feature should be made of word
X_train_tf = tfidfvectorizer.fit_transform(train_X)
tfidf_tokens = tfidfvectorizer.get_feature_names() #Array mapping from feature integer indices to feature name
df_tfidfvect = pd.DataFrame(data = X_train_tf.toarray(),index = ['Italian','French','Spanish','Dutch'],columns = tfidf_tokens)

X_test_tf = tfidfvectorizer.transform(test_X)

naive_bayes_classifier = MultinomialNB()
naive_bayes_classifier.fit(X_train_tf, train_y)
y_pred = naive_bayes_classifier.predict(X_test_tf)

V, z = df_oneM.iloc[:,0],df_oneM.iloc[:,1] #iloc: Purely integer-location based indexing for selection by position
V_train, V_test, z_train, z_test = train_test_split(V, z, test_size=0.2,random_state=None)

V_train_tf = tfidfvectorizer.fit_transform(V_train)

V_test_tf = tfidfvectorizer.transform(V_test)

naive_bayes_classifier = MultinomialNB()
naive_bayes_classifier.fit(V_train_tf, z_train)
z_pred = naive_bayes_classifier.predict(V_test_tf)
