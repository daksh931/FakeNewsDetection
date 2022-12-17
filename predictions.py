
def pre(list):

    #     mp = pickle.load(open('E:\\Data Science\\FakeNewsTwitterProject\\ProjectTwitterSentAna\\SupervisedNN\\SupervisedFakeNews\\modelpickle','rb'))
    import numpy as np
    import keras
    import nltk
    import re
    from nltk.corpus import stopwords
    from tensorflow.keras.preprocessing.text import one_hot
    from tensorflow.keras.preprocessing.sequence import pad_sequences

    mp = keras.models.load_model("static\\deeplearningmodel.h5")
    from nltk.stem.porter import PorterStemmer
    ps = PorterStemmer()
    corpus_new2 = []
    for i in range(0, len(list)):

        review = re.sub('[^a-zA-Z]', ' ', list[i])
        review = review.lower()
        review = review.split()

        review = [ps.stem(word)
                  for word in review if not word in stopwords.words('english')]
        review = ' '.join(review)
        corpus_new2.append(review)
        voc_size = 5000
    onehot_repr = [one_hot(words, voc_size)for words in corpus_new2]
    onehot_repr

    sent_length = 20
    embedded_docs_new = pad_sequences(
        onehot_repr, padding='pre', maxlen=sent_length)
    # print(embedded_docs_new)

    unseen_predictions = np.where(mp.predict(embedded_docs_new) > 0.90, 1, 0)

    # unseen_predictions

    output = []
    for i in range(len(unseen_predictions)):
        if unseen_predictions[i] == 1:
            output.append("True")
        else:
            output.append("False")
    return output


# corpus_new = ['RT @bluevirginia: Haha, @RTDNEWS has video of Youngkin getting booed at the VCU game last night, and someone yelling "I didnt vote for you ',
#               'Amazon in final talks for the rights to a Warhammer 40,000 series adaptation, with Henry Cavill attached to star and executive ']
# output = pre(corpus_new)
# print(output)
