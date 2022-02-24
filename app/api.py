from app import app
from db import exec_db_query
from flask import jsonify

@app.route("/"):
def get_items():
    data = exec_db_query("SELECT * FROM items")
    resp = jsonify(data)
    resp.status_code = 200
    return resp

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
