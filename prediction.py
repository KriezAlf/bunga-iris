import jolib

def predict(data):
	clf = joblib.load("knn_model.sav")

	return clf.predict(data)
