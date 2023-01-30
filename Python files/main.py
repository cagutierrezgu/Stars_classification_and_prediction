import numpy as np
from flask import Flask, jsonify, request
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from data_loading import dataload
from data_exploring import preprocess
from training import train
from evaluation import usuario

app = Flask(__name__)

link = 'https://drive.google.com/uc?export=download&id=1oOgj9f5UTITTDzMehEIIzNz2aoR2IlgZ'
name = 'stars.csv'
df_stars = dataload(link, name)

x_train, x_test, y_train, y_test, scaler = preprocess(df_stars)

cr, depth = train(x_train, y_train)

def evaluate(data_input):
  tree = DecisionTreeClassifier(criterion = cr, max_depth = depth)
  tree.fit(x_train, y_train)
  #prediction = tree.predict(np.array([[3.068, 0.002400, 0.1700, 16.12, 0, 1, 2, 0.2, 1,1,1,1,1,1,1,1,1,1,1,1,1]]))
  prediction = tree.predict(np.array(data_input))
  return prediction[0]




@app.route("/")
def home():
    return 'Página funcionando'

@app.route("/run", methods=["POST"])
def run():
    json=request.get_json(force=True)
    data_input = json['Data']
    return 'Tipo de Estrella: {}'.format(usuario(data_input))



if __name__ == '__main__':
    app.run()