# -*- coding: utf-8 -*-
import logging

from flask import Flask, request

from docs.server.apidesc.models import APIDesc

app = Flask(__name__)
logger = logging.getLogger('APP')
logger.setLevel('DEBUG')


# @app.route('/testrun', methods=['POST'])
# def run_tests():
#     post_body=request.json
#     file_path = ' '.join(post_body.get('filePath'))
#     env = post_body.get('env','alpha')
#     logger.info(env)
#     pytest_commands = "{files} --env={env} --html=test_result/api_result.html"\
#         .format(files=file_path,env=env)
#     logger.info(pytest_commands)
#     pytest.main(pytest_commands)
#     return "test is running"


@app.route('/api',methods=['POST'])
def save_api_desc():
    post_body = request.json
    result =APIDesc(post_body).update_or_insert()
    print(result)

if __name__ == '__main__':
    app.run(debug=True)
