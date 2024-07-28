```python
# Imports the Google Cloud client library
from flask import Flask

# Instantiates a Flask app
app = Flask(__name__)

# Sets the route and the associated function
@app.route("/")
def hello_world():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

# Runs the app
if __name__ == "__main__":
    app.run()
```