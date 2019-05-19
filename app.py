from flask import Flask, request, make_response, jsonify
import logging
import datetime
from pymongo import MongoClient

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
connection = MongoClient('localhost', 27017)
db = connection.get_database("SSU_schedule")
app = Flask(__name__)


def is_num(date):
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    week = datetime.date(int(year), int(month), int(day)).isocalendar()[1]
    if week % 2 == 1:
        return True
    else:
        return False


full_type = {
    'лек.': 'лекция',
    'пр.': 'практика',
}


def form_response(res):
    result = ''
    for s in sorted(res, key=lambda i: i["lesson"]):
        print(s['subjectName'], full_type[s['type']], sep=', ')
        result += s['subjectName'] + ', ' + full_type[s['type']] + '\n'
        print(s['teacherName'])
        result += s['teacherName'] + '\n'
        print(s['classroom'])
        result += s['classroom'] + '\n'
        if s['subGroup'] != 0:
            print(str(s['subGroup']) + 'подгруппа')
            result += str(s['subGroup']) + 'подгруппа' + '\n'
        print(s['timePeriod'])
        result += s['timePeriod'] + '\n'
        print('---------')
        result += '---------' + '\n'
    return {'fulfillmentText': result}


week_day = {
    1: 'пн',
    2: 'вт',
    3: 'ср',
    4: 'чт',
    5: 'пт',
    6: 'сб',
    7: 'вс',
}


def get_data_from_database(course, spec, date, group_number):
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    week = datetime.date(int(year), int(month), int(day)).isocalendar()[2]
    if is_num(date) is False:
        res = db.schedule.find({"daysOfWeek": week_day[week], "groupNumber": int(group_number)})
        if res.count() == 0:
            return {'fulfillmentText': 'Сегодня занятий нет. Можете отдохнуть!'}
        else:
            return form_response(res)
    else:
        res = db.schedule.find({"daysOfWeek": week_day[week], "groupNumber": int(group_number), "num": True})
        print(res)
        if res.count() == 0:
            return {'fulfillmentText': 'В этот день занятий нет. Можете отдохнуть!'}
        else:
            return form_response(res)


@app.route('/webhook', methods=['GET', 'POST'])
def get_schedule():
    data = request.get_json(silent=True, force=True)
    course = data['queryResult']['parameters']['course']
    spec = data['queryResult']['parameters']['specialization']
    date = data['queryResult']['parameters']['date']
    group_number = data['queryResult']['parameters']['groupNumber']
    response = get_data_from_database(course, spec, date, group_number)
    return make_response(jsonify(response))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
