#!/bin/bash
PORT=${1:-5000}
echo "Starting node on port $PORT"
export FLASK_APP=app/node.py
flask run --host=0.0.0.0 --port=$PORT