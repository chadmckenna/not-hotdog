### Setup Instructions:

1. Make sure Venv is setup and you have version 3.6 of Python installed
2. Clone the repo
3. `cd` into the repo and run `virtualenv venv`
4. run `. venv/bin/activate`
5. run `pip install -r requirements.txt`

Now everything is setup.

To run the the Flask server:
1. `cd app`
2. `export FLASK_APP=app.py`
3. `flask run`
4. Visit `localhost:5000/` to see the app running

To run the Jupyter notebook:
1. Make sure you are in the root directory (`cd ../` if you're in `./app/`)
2. `jupyter notebook`
3. Visit `localhost:8888` to view the notebook. All notebooks are in `notebook` dir
