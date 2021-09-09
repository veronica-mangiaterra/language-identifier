accuracy = metrics.accuracy_score(test_y, y_pred)
print("accuracy:", accuracy)
conf_matrix = metrics.confusion_matrix(test_y, y_pred)
print(conf_matrix)

accuracy_one = metrics.accuracy_score(z_test, z_pred)
print("accuracy:", accuracy_one)
conf_matrix_one = metrics.confusion_matrix(z_test, z_pred)
print(conf_matrix_one)

matrix = plot_confusion_matrix(naive_bayes_classifier, V_test_tf, z_test)
matrix.ax_.set_title('Confusion matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show

def get_errors (sent, lang):
    list_of_errors = []
    tf_idf_test = tfidfvectorizer.transform(sent)
    pred_lang = naive_bayes_classifier.predict(tf_idf_test)
    zipped = zip(sent, lang, pred_lang)
    all_tuples = tuple(zipped)
    for sent, lang, pred_lang in all_tuples:
        if lang != pred_lang:
            l_ = [sent, lang, pred_lang]
            list_of_errors.append(l_)
    return list_of_errors
  
  
