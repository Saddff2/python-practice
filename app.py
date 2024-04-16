from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_cloud():
  """Displays Hello, Cloud! message on the root path."""
  return "Hello, Cloud!"

if __name__ == "__main__":
  app.run(debug=True)
