from flask import Flask,render_template, request

app=Flask(__name__,template_folder='template')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Classification')
def Classification():
    return render_template('Classification.html')

@app.route('/Prediction')
def Prediction():
    return render_template('Prediction.html')

@app.route('/Clustering')
def Clustering():
    return render_template('Clustering.html')

if __name__ == '__main__':
    app.run(debug=True)