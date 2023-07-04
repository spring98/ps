from flask import Flask, request
from flask_restx import Resource

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/start', methods=['GET', 'POST'])
def start_apt():
    if request.method == 'GET':
        return 'start page'
    elif request.method == 'POST':
        if 'Access-Token' in request.headers:
            access_token = request.headers.get('Access-Token')
            if access_token == 'spring-access-token':
                return {
                    'status': 'success',
                    'auth_key': 'spring-auth-key'
                }
            else:
                return {
                    'status': 'unknown candidate'
                }


@app.route('/query', methods=['GET', 'POST'])
def query_apt():
    server_value = 100

    if request.method == 'GET':
        return 'query get'

    if request.method == 'POST':
        try:
            params = request.get_json()
            print(f'0: {params}')
            auth_key = params['auth_key']
            client_value = params['value']
            print(f'1: {auth_key}')
            print(f'2: {client_value}')


            # if 'Access-Token' in request.headers:
            #     access_token = request.headers.get('Access-Token')
            #     if access_token is not 'spring-access-token':
            #         return {
            #             'status': 'unknown candidate'
            #         }

            if auth_key != 'spring-auth-key':
                return {
                    'status': 'unknown authentication key'
                }
            else:
                if server_value > client_value:
                    return {
                        'status': 'success',
                        'result': 'up'
                    }
                elif server_value < client_value:
                    return {
                        'status': 'success',
                        'result': 'down'
                    }
                else:
                    return {
                        'status': 'success',
                        'result': '정답 flag'
                    }
        except Exception as e:
            print(e)



app.run()
