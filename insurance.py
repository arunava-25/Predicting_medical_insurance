import tensorflow as tf
import flask
import tensorflow.keras as keras
import matplotlib.image as mpimg

app = flask.Flask(__name__)
@app.route('/show')
def show_in():
	return flask.render_template('form_insurance.html')

@app.route('/insurance',methods=["POST"])
def show_insurance():
	user=flask.request.form['name']
	age=float(flask.request.form['age'])
	sex=float(flask.request.form['sex'])
	bmi=float(flask.request.form['bmi'])
	children=float(flask.request.form['children'])
	smoker=float(flask.request.form['smoker'])

	model=keras.models.load_model("insurance_final.h5")
	result=model.predict([[age,sex,bmi,children,smoker]])
	return flask.render_template('result.html',expenses=result[0],name=user)