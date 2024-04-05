from flask import Flask, render_template, request, jsonify
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
            carat = float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color = request.form.get('color'),
            clarity = request.form.get('clarity')
        )
        df = custom_data_obj.get_data_as_dataframe()
        prediction_pipeline = PredictPipeline()
        prediction = f'Diamond Price is {prediction_pipeline.predict(df)}'
        return render_template('result.html', results = prediction)

# api testing
@app.route('/predict_api', methods = ['GET', 'POST'])
def api_testing():
    if request.method == 'GET':
        return 0.0
    else:
        custom_data_obj = CustomData(
            carat = request.json['carat'],
            depth = request.json['depth'],
            table = request.json['table'],
            x = request.json['x'],
            y = request.json['y'],
            z = request.json['z'],
            cut = request.json['cut'],
            color = request.json['color'],
            clarity = request.json['clarity']
        )
        df = custom_data_obj.get_data_as_dataframe()
        prediction_pipeline = PredictPipeline()
        prediction = float(prediction_pipeline.predict(df))
        return jsonify(prediction)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)