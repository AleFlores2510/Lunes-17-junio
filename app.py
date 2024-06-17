from flask import Flask,redirect, render_template, request
from parqueo import Parqueo
app = Flask(__name__)
parqueo = Parqueo(20)

@app.route('/parqueo')
def parquear():
    
    return render_template("parquear.html")

@app.route('/')
def iniciar():
    layout =[]
    n = int(len(parqueo.campos)/5)+1
    for i in range(n):
        layout.append(parqueo.campos[i*5:i+1*5])

    
    return render_template("index.html",
                           parqueo=layout, 
                           tiene_espacio = parqueo.hay_espacio())    
if __name__ == '__main__':
    app.run(debug=True)