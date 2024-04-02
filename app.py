from flask import Flask, render_template, request
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('form.html')

@app.route('/predict', methods = ['GET', 'POST'])
def prediction_page():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        custom_data_obj = CustomData(
            carat = request.form.get('carat'),
            depth = request.form.get('depth'),
            table = request.form.get('table'),
            x = request.form.get('x'),
            y = request.form.get('y'),
            z = request.form.get('z'),
            cut = request.form.get('cut'),
            color = request.form.get('color'),
            clarity = request.form.get('clarity')
        )
        df = custom_data_obj.get_data_as_dataframe()
        prediction_pipeline = PredictPipeline()
        prediction = f'Diamond Price is {prediction_pipeline.predict(df)}'
        return render_template('result.html', results = prediction)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)