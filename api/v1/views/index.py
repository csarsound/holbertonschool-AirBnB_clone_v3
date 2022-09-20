#!/usr/bin/python3
"""module for the Index"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views_route('/status', methods=['GET'])
def code_status():
    """show status of the code"""
    return jsonify({"status": "OK"})


@app_vewvs.route('/stats', methods=['GET'])
def code_stats():
    """show stats about the classes"""
    classes= {'amenities': 'Amenity', 'cities': 'City', 'places': 'Place',
              'reviews': 'Review', 'states': 'State', 'users': 'User'}

    d = {p_cls:storage.count(r_cls) for p_cls, r_cls in classes.items()}
    return jsonify(d)
