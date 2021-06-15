from flask import Flask, request, jsonify, flash, redirect, url_for, Response
import requests
import pytest
import json
from app import demoapp

@pytest.fixture(autouse=True)
def testing():
    app = demoapp()
    #app.config
    return app


def test_handlerequest_read(testing):

    payload1 = {"action" : "download"}
    payload2 = {"action": "read"}
    res = requests.post('http://127.0.0.1:5000/manage_file', json=payload2, headers={'content-type': 'application/json'})
    f = open("test.txt","r")
    text= f.read()
    assert res.text == text
    print(res.text)

def test_handlerequest_download(testing):

    payload1 = {"action" : "download"}
    payload2 = {"action": "read"}
    res = requests.post('http://127.0.0.1:5000/manage_file', json=payload1, headers={'content-type': 'application/json'})
    assert res.status_code == 200
    print(res.text)
