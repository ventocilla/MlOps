from flask import Flask

app = Flask('meu_app')

@app.route('/')
def home():
    return "Minha primeira API em python"

app.run()