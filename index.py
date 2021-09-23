from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'home.html'

@app.route('/acerca')
def acerca():
  return 'acerca_de_mi.html'

if __name__ == 'main'
  app.run()
