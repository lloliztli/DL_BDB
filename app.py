from flask import Flask, render_template, json, request, jsonify
from PIL import Image

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'nombre': u'Cactus',
        'raza': u'salchicha',
        'edad': u'2 anios',
        'color': u'negro con cafe',
        'descripcion': u'Es un perro muy docil trae un collar rojo', 
        'fecha de extravio': u'11-11-2017',
        'lugar de extravio': u'Amsterdam 173, Condesa, CDMX'
    },
    {
        'id': 2,
        'nombre': u'tayson',
        'raza': u'pitbull',
        'edad': u'5 anios',
        'color': u'Gris/blue',
        'descripcion': u'Tyson es un perro muy grande y gordo suele traer la lengua de fuera', 
        'fecha de extravio': u'01-12-2016',
        'lugar de extravio': u'Av Cuauhtemoc 1236, Benito Juarez, CDMX'
    },
    {
        'id': 3,
        'nombre': u'snoppy',
        'raza': u'dogo argentino',
        'edad': u'8 meses',
        'color': u'blanco',
        'descripcion': u'en perro muy grande con collar de cuero y una cicatriz en la oreja', 
        'fecha de extravio': u'23-04-2017',
        'lugar de extravio': u'Centro Atlixco, Puebla'
    }
]


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/signUp', methods=['POST'] )
def test():
    
    var = request.form['inputName']
    print var
    return jsonify({'task': tasks}), 201
 

@app.route('/dogs', methods=['GET'])
def get_dogs():
    return jsonify({'tasks': tasks})

@app.route('/new_dog', methods=['POST'])
def add_dog():
    var = request.json['nombre']
    task = {
        #'id': tasks[-1]['id'] + 1,
        #'nombre': request.json['nombre'],
        #'raza': request.json['raza'],
        #'edad': request.json['edad'],
        #'color': request.json['color'],
        #'descripcion': request.json['descripcion'],
        #'fecha de extravio': request.json['fecha'],
        #'lugar de extravio': request.json['lugar']
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/upload_image', methods=['POST'])
def image():
    picture = request.files['file']
    img = Image.open(request.files['file'])
    #img.show()
    img.save("final.jpg")
    results =  os.system('python classify.py final.jpg')
    print results
    return "OK"

if __name__ == "__main__":
    app.run(port=5000)
