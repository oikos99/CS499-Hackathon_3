from flask import Flask, render_template, request
from sklearn import svm

app = Flask(__name__, static_url_path='')

traffic_dataset = [[10, 0, 1, 8], [10, 0, 2, 9], [10, 1, 1, 13], [5, 0, 1, 15], [5, 1, 5, 16], [5, 1, 6, 18]]
traffic_status = [8, 7, 5, 6, 9, 9]
clf = svm.SVC(gamma=0.001, C=100, )


@app.route('/')
def root():
    return app.send_static_file('index.html')


def insertData(road, direction, day, time, status):
    temp = [int(road), int(direction), int(day), int(time)]
    global traffic_dataset
    traffic_dataset.append(temp)
    global traffic_status
    traffic_status.append(int(status))
    clf.fit(traffic_dataset, traffic_status)
    display = [int(road), int(direction), int(day), int(time), int(status)]
    return str(display) + " Inserted to Traffic Dataset: " + str(traffic_dataset)


def predict_status(road, direction, day, time):
    result = clf.predict([[int(road), int(direction), int(day), int(time)]])
    return "Predicted Traffic Status: " + str(result)


def clear_data():
    global traffic_dataset
    traffic_dataset = [[0, 0, 0, 0]]
    global traffic_status
    traffic_status = [0]


@app.route('/save',methods=['GET','POST'])
def save():
    road = request.args.get('road_id')
    direction = request.args.get('direction')
    day = request.args.get('dayOfWeek')
    time = request.args.get('timeOfDay')
    status = request.args.get('traffic_status')

    res = insertData(road, direction, day, time, status)
    return res


@app.route('/predict',methods=['GET','POST'])
def predict():
    road = request.args.get('road_id')
    direction = request.args.get('direction')
    day = request.args.get('dayOfWeek')
    time = request.args.get('timeOfDay')
    res = predict_status(road, direction, day, time)
    return res


@app.route('/clear',methods=['GET','POST'])
def clear():
    clear_data()
    print(traffic_dataset)
    return "Traffic dataset cleared!"


@app.route('/predict_ui', methods=['GET', 'POST'])
def predict_ui():
    res = None
    if request.method == 'POST':
        road = request.form['road_id']
        direction = request.form['direction']
        day = request.form['dayOfWeek']
        time = request.form['timeOfDay']

        res = predict_status(road, direction, day, time)
    return render_template('predict_ui.html', response=res)


@app.route('/insert_ui', methods=['GET', 'POST'])
def insert_ui():
    res = None
    if request.method == 'POST':
        road = request.form['road_id']
        direction = request.form['direction']
        day = request.form['dayOfWeek']
        time = request.form['timeOfDay']
        status = request.form['traffic_status']

        res = insertData(road, direction, day, time, status)
    return render_template('insert_ui.html', response=res)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
