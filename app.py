from flask import Flask, render_template

# Crear una instancia de Flask
app = Flask(__name__)

# Ruta principal: cuando alguien entra a http://localhost:5000
@app.route('/')
def inicio():
    return render_template('index.html')  # Muestra el HTML que está en la carpeta "templates"

# Solo si se ejecuta directamente este archivo (no si se importa en otro)
if __name__ == '__main__':
    app.run(debug=True)
