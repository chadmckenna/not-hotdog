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

### Usage

There is an API endpoint at `localhost:5000/is_hotdog` that accepts a POST. In the form data, it simply expects the file to have the key `file`. Here's an example cURL request:
```
POST /is_hotdog HTTP/1.1
Host: localhost:5000
Cache-Control: no-cache
Postman-Token: b626461f-9367-76e3-9056-af4e3e9ff18c
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="1.jpg"
Content-Type: image/jpeg


------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

This endpoint will return a simple JSON object with `probability` and `what` values. Probability is simply the value from 0 to 1 that the image is in fact a hotdog. A value closer to 1 means its more sure, closer to 0 means its less sure. On our classifier of `hotdog`/`not hotdog`, we use a 20%/80% split, meaning it has to be very sure to classify something as a hotdog instead of a traditional 50%/50% split. Here is an example of the return JSON:
```JSON
{
    "probability": 0.00001633167266845703,
    "what": "not hotdog"
}
```
