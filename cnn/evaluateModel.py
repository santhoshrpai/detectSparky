from keras.models import model_from_json
import gzip
import cPickle

model_architecture = open('./../cnn/my_model_architecture.json')
model = model_from_json(model_architecture.read())
model.load_weights('./../cnn/model_weights.h5')

def load_data(path):
    if path.endswith(".gz"):
        f = gzip.open(path, 'rb')
    else:
        f = open(path, 'rb')

    data = cPickle.load(f)
    f.close()
    return data  # (X, Y)


validation_path = "./../data_processing/validation_data_10.pkl.gz"
X_test = load_data(validation_path)

classes = model.predict_classes(X_test, batch_size=10)
proba = model.predict_proba(X_test, batch_size= 10)

print classes
