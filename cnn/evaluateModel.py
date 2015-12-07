from keras.models import model_from_json
import gzip
import cPickle

model_architecture = open('model_architecture_200.json')
model = model_from_json(model_architecture.read())
model.load_weights('model_weights_200.h5')

def load_data(path):
    if path.endswith(".gz"):
        f = gzip.open(path, 'rb')
    else:
        f = open(path, 'rb')

    data = cPickle.load(f)
    f.close()
    return data


validation_path = "./../data_processing/validation_data_200.pkl.gz"
X_test = load_data(validation_path)

img_rows, img_cols = 256, 384

X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
X_test = X_test.astype("float32")
X_test /= 255


classes = model.predict_classes(X_test, batch_size=10)
proba = model.predict_proba(X_test, batch_size= 10)

print classes
