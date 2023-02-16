from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return "Minha primeira API em python"

@app.route('/sentimento/<frase>')
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(from_lang='pt_br', to='en')
    polaridade = tb_en.sentiment.polarity
    return f"Polaridade: {polaridade}"

app.run(debug=True)

