#!/usr/bin/python3
"""Flask web application"""

from models import storage
from api.v1.views import app_views
from flask import Flask

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(error):
    """Clean-up method
    """
    storage.close()

if __name__ == "__main__":
    host = getenv("ARSUAL_API_HOST", "0.0.0.0")
    port = getenv("ARSUAL_API_PORT", "3000")
    app.run(host=host, port=port, threaded=True, debug=True)
