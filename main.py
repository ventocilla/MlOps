from flask import Flask, request, jsonify
from textblob import TextBlob
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('casas.csv')
colunas = ['tamanho', 'ano','garagem']
#df = df[colunas]

x = df.drop('preco', axis=1) #variavel explicativa
y = df['preco'] #variavel resposta

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42
    )

modelo = LinearRegression()
modelo.fit(x_train,y_train)

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

@app.route('/cotacao/', methods=['POST'])
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas] #list comprehension
    preco = modelo.predict([[dados_input]])
    return jsonify(preco=preco[0])

app.run(debug=True)

