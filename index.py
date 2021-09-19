from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'Bienvenido a mi portafolio personal'

if __name__ == 'main'
  app.run()
