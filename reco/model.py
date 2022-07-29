from gensim.models import Word2Vec
import pickle


class Model:
    def __init__(self):
        with open('model_iLab_case.pkl', 'rb') as f:
            model_loaded = pickle.load(f)

        self.model = model_loaded

    def predict(self, product_id):
        result = self.model.wv.most_similar(product_id, topn=15)
        return result


model = Model()


def get_model():
    return model
