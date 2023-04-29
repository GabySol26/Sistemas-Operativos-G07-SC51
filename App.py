from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL connection
app.config['MYSQL_HOST'] = '44.204.85.86'
app.config['MYSQL_USER'] = 'Gaby'
app.config['MYSQL_PASSWORD'] = 'trabajop@'
app.config['MYSQL_DB'] = 'TP'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    tabla = request.args.get('tabla', 'Paciente')
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM {}'.format(tabla))
    data=cur.fetchall()
    return render_template('index.html', contacts = data, tabla=tabla)

@app.route('/cambiar_tabla', methods=['POST'])
def cambiar_tabla():
    if request.method == 'POST':
        tabla = request.form.get('tabla')
        flash("Se cambio la tabla")
        flash("Llenar TODOS los campos Obligatoriamente")
        return redirect(url_for('Index', tabla=tabla))

@app.route('/add_contactp', methods=['POST'])
def add_contactp():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidop = request.form['apellidop']
        apellidom = request.form['apellidom']
        dni = request.form['dni']
        genero = request.form['genero']
        fnac = request.form ['fnac']
        email = request.form['email']
        telef = request.form['telef']

        cur = mysql.connection.cursor()
         # Validar DNI
        cur.execute('SELECT dni FROM Paciente WHERE dni = %s', (dni,))
        dni_existente = cur.fetchone()
        if dni_existente:
            return 'El DNI ya existe en la base de datos'
        
        # Validar teléfono
        cur.execute('SELECT telefonoP FROM Paciente WHERE telefonoP = %s', (telef,))
        telef_existente = cur.fetchone()
        if telef_existente:
            return 'El número de teléfono ya existe en la base de datos'

        cur.execute('INSERT INTO Paciente (nombreP, apellidoPP, apellidoMP,dni,generoP,telefonoP,fnacimiento,email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
        (nombre,apellidop,apellidom,dni,genero,telef,fnac,email))
        mysql.connection.commit()
        cur.close()
        flash('Se pudo agregar Paciente')
        return redirect(url_for('Index'))

@app.route('/add_contactm', methods=['POST'])
def add_contactm():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidop = request.form['apellidop']
        apellidom = request.form['apellidom']
        dni = request.form['dni']
        genero = request.form['genero']
        email = request.form['email']
        fnac = request.form ['fnac']
        cole = request.form['cole']
        esp = request.form['esp']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Medico (nombreM, apellidoPM, apellidoMM,dniM,generoM,emailM,fnacimientoM,numColegialM,especialidad) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (nombre,apellidop,apellidom,dni,genero,email,fnac,cole,esp))
        mysql.connection.commit()
        cur.close()
        flash('Se pudo agregar Medico')
        return redirect(url_for('Index', tabla = 'Medico'))

@app.route('/add_contactc', methods=['POST'])
def add_contactc():
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora = request.form['hora']
        nota = request.form['nota']
        idp = request.form['idPaciente']
        idm = request.form['idMedico']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Cita (fecha, hora, nota,idPaciente,idMedico) VALUES (%s,%s,%s,%s,%s)',
        (fecha,hora,nota,idp,idm))
        mysql.connection.commit()
        cur.close()
        flash('Se pudo agregar Cita')
        return redirect(url_for('Index', tabla = 'Cita'))

@app.route('/add_contactT', methods=['POST'])
def add_contactT():
    if request.method == 'POST':
        inicio = request.form['inicio']
        fin = request.form['fin']
        medicamento = request.form['medicamento']
        dosis = request.form['dosis']
        frecuencia = request.form['frecuencia']
        idc = request.form['idCita']


        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Tratamiento (inicio,fin,Medicamento,dosis,frecuencia,idCita) VALUES (%s,%s,%s,%s,%s,%s)',
        (inicio,fin,medicamento,dosis,frecuencia,idc))
        mysql.connection.commit()
        cur.close()
        flash('Se pudo agregar Tratamiento')
        return redirect(url_for('Index', tabla = 'Tratamiento'))

@app.route('/edit/<id>')
def get_contact(id):
    tabla = request.args.get('tabla', 'Paciente')
    cur = mysql.connection.cursor()
    if tabla == 'Paciente':
        cur.execute('SELECT * FROM Paciente WHERE idPaciente = %s', (id,))
    elif tabla == 'Medico':
        cur.execute('SELECT * FROM Medico WHERE idMedico = %s', (id,))
    elif tabla == 'Cita':
        cur.execute('SELECT * FROM Cita WHERE idCita = %s', (id,))
    elif tabla == 'Tratamiento':
        cur.execute('SELECT * FROM Tratamiento WHERE idTratamiento = %s', (id,))    

    data = cur.fetchall()
    return render_template('edit-contact.html', contact = data[0], tabla = tabla)

@app.route('/updatep/<int:id>', methods = ['POST'])
def updatep(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidop = request.form['apellidop']
        apellidom = request.form['apellidom']
        dni = request.form['dni']
        genero = request.form['genero']
        fnac = request.form ['fnac']
        email = request.form['email']
        telef = request.form['telef']

        cur = mysql.connection.cursor()
        cur.execute("""UPDATE Paciente SET 
        nombreP = %s, apellidoPP = %s, apellidoMP = %s, dni = %s, generoP = %s, telefonoP = %s, fnacimiento = %s, email = %s
        WHERE idPaciente = %s""", (nombre,apellidop,apellidom,dni,genero,telef,fnac,email,id,))
        mysql.connection.commit()
        flash('Paciente modificado')
        return redirect(url_for('Index', tabla='Paciente'))

@app.route('/updatem/<int:id>', methods = ['POST'])
def updatem(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidop = request.form['apellidop']
        apellidom = request.form['apellidom']
        dni = request.form['dni']
        genero = request.form['genero']
        email = request.form['email']
        fnac = request.form ['fnac']
        cole = request.form['cole']
        esp = request.form['esp']

        cur = mysql.connection.cursor()
        cur.execute("""UPDATE Medico SET 
        nombreM = %s, apellidoPM = %s, apellidoMM = %s, dniM = %s, generoM = %s, emailM = %s, fnacimientoM = %s, numColegialM = %s, especialidad = %s
        WHERE idMedico = %s""", (nombre,apellidop,apellidom,dni,genero,email,fnac,cole,esp,id,))
        mysql.connection.commit()
        flash('Medico modificado')
        return redirect(url_for('Index', tabla='Medico'))

@app.route('/updatec/<int:id>', methods = ['POST'])
def updatec(id):
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora = request.form['hora']
        nota = request.form['nota']

        cur = mysql.connection.cursor()
        cur.execute("""UPDATE Cita SET 
        fecha = %s, hora = %s, nota = %s
        WHERE idCita = %s""", (fecha,hora,nota,id,))
        mysql.connection.commit()
        flash('Cita modificada')
        return redirect(url_for('Index', tabla='Cita'))

@app.route('/update/<int:id>', methods = ['POST'])
def update(id):
    if request.method == 'POST':
        inicio = request.form['inicio']
        fin = request.form['fin']
        medicamento = request.form['medicamento']
        dosis = request.form['dosis']
        frecuencia = request.form['frecuencia']

        cur = mysql.connection.cursor()
        cur.execute("""UPDATE Tratamiento SET 
        inicio = %s, fin = %s, Medicamento = %s, dosis = %s, frecuencia = %s
        WHERE idTratamiento = %s""", (inicio,fin,medicamento,dosis,frecuencia,id,))
        mysql.connection.commit()
        flash('Tratamiento modificado')
        return redirect(url_for('Index', tabla='Tratamiento'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    tabla = request.args.get('tabla', 'Paciente')
    cur = mysql.connection.cursor()
    if tabla == 'Paciente':
        cur.execute('DELETE FROM Paciente WHERE idPaciente = {}'. format(id))
    elif tabla == 'Medico':
        cur.execute('DELETE FROM Medico WHERE idMedico = {}'. format(id))
    elif tabla == 'Cita':
        cur.execute('DELETE FROM Cita WHERE idCita = {}'. format(id))
    elif tabla == 'Tratamiento':
        cur.execute('DELETE FROM Tratamiento WHERE idTratamiento = {}'. format(id))

    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index', tabla=tabla))


if __name__ == '__main__':
    app.run(port = 3000, debug = True)