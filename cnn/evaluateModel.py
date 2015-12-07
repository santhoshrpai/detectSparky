from keras.models import model_from_json
import gzip
import cPickle

model = model_from_json(open('my_model_architecture.json').read())

def load_data(path):
    if path.endswith(".gz"):
        f = gzip.open(path, 'rb')
    else:
        f = open(path, 'rb')

    data = cPickle.load(f)
    f.close()
    return data  # (X, Y)


validation_path = "./../data_processing/validation_data_10.pkl.gz"
(X_test, y_test) = load_data(validation_path)

classes = model.predict_classes(X_test, batch_size=32)
proba = model.predict_proba(X_test, batch_size=32)

print classes
