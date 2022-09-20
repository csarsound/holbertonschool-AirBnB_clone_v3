#!/usr/bin/python3
"""module for the Index"""

from api.v1.views import app_views
from flask import jsonify


@app_views_route('/status', methods=['GET'])
def code_status():
    """show status of the code"""
    return jsonify({"status": "OK"})
