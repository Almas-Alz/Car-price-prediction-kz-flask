from flask import Flask, redirect, url_for, render_template, request
from features import prepare_to_html, prepare_to_model
import pickle


app = Flask(__name__)
model = pickle.load(open('randomforest.pkl', 'rb'))


@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		features = request.form.to_dict()
		to_html = prepare_to_html(features)
		to_model = prepare_to_model(features)
		prediction = round(int(model.predict(to_model)[0]), -3)
		return render_template("prediction.html", input_data=to_html, prediction=prediction)
	return render_template("index.html")



if __name__ == "__main__":
	app.run()
