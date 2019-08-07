from django.shortcuts import render
import json


def get_schedule(request):
    df_request = json.loads(request.body)
    print(df_request)
    group_number = df_request['queryResult']['parameters']['groupNumber']
    date = df_request['queryResult']['parameters']['date']