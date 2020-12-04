from flask import render_template, make_response, request
from app import app
from app.selenium_api import SeleniumCheck
import json


@app.route('/api/element/exists/')
def index():
    element = request.headers.get("element")
    body = request.json
    if body and element:
        selenium = SeleniumCheck()
        status = selenium.selenium_check(body,element)
        json_object = json.dumps(status)
    return(json_object)




