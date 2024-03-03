from flask import render_template, Blueprint, request, redirect, url_for, session, flash

judecatori = Blueprint("judecatori", __name__, static_folder="static", template_folder="templates")

@judecatori.route('/judecatori', methods=['GET', 'POST'])
def judecatori_page():
    cur = judecatori.mysql.connection.cursor()
    
    cur.execute('''select J.JudecatorID, CONCAT(J.Nume, ' ', J.Prenume) as Judecator, J.CNP, J.        
                Telefon, J.Email,
                (Select GROUP_CONCAT(distinct D.Numar) from dosare D
                join judecatoridosare JD on JD.DosarID = D.DosarID
                where JD.JudecatorID = J.JudecatorID) as Dosare
                from Judecatori J
                order by Judecator
                ''')
    
    judecatori_data = cur.fetchall()
    cur.close()
    
    return render_template("judecatori/judecatori.html", judecatori_data = judecatori_data)

@judecatori.route('/add_judecator', methods=['POST'])
def add():
    nume = request.form['Nume']
    prenume = request.form['Prenume']
    cnp = request.form['CNP']
    telefon = request.form['Telefon']
    email = request.form['Email']
    dosare = request.form['Dosare']
    
    cur = judecatori.mysql.connection.cursor()

    cur.execute("Select CNP from judecatori")
    cnp_data = cur.fetchall()
    cnp_data = [item[0] for item in cnp_data]
    
    cur.execute("Select Numar from dosare")
    dosare_data = cur.fetchall()
    dosare_data = [item[0] for item in dosare_data]
    
    dosare = int(dosare)
    
    if dosare == '' or dosare not in dosare_data:
        route = 'judecatori.judecatori_page'
        title = 'Lista Judecatori'
        error = 'Nu s-a putut realiza adaugarea/modificarea datelor. Introduceti datele corecte.'
        text = 'Reveniti la pagina Judecatori si introduceti datele corecte.'
        return render_template("error.html", route = route, title = title, error = error, text = text)
    elif dosare in dosare_data:
        
        if cnp == '' or cnp == None or cnp in cnp_data:
            route = 'judecatori.judecatori_page'
            title = 'Lista Judecatori'
            error = 'Nu s-a putut realiza adaugarea/modificarea datelor, deoarece ati introdus date existente in baza de date. Introduceti datele corecte.'
            text = 'Reveniti la pagina Judecatori si introduceti datele corecte.'
            return render_template("error.html", route = route, title = title, error = error, text = text)
             
        cur.execute("INSERT INTO Judecatori (Nume, Prenume, CNP, Telefon, Email) VALUES (%s, %s, %s, %s, %s)", (nume, prenume, cnp, telefon, email))
        judecatori.mysql.connection.commit()
        
        cur.execute("Select DosarID from dosare where Numar = %s", (dosare,))
        dosar_id = cur.fetchone()[0]
        
        # Get the JudecatorID of the newly inserted row
        cur.execute("SELECT LAST_INSERT_ID()")
        judecator_id = cur.fetchone()[0]

        # Now insert into judecatoridosare using the obtained JudecatorID
        cur.execute("INSERT INTO judecatoridosare (JudecatorID, DosarID) VALUES (%s, %s)", (judecator_id, dosar_id))
        judecatori.mysql.connection.commit()

    return redirect(url_for('judecatori.judecatori_page'))  # replace with the name of your view function


@judecatori.route('/update_judecator', methods=['GET','POST'])
def update():
    nume = request.form['Nume']
    prenume = request.form['Prenume']
    cnp = request.form['CNP']
    telefon = request.form['Telefon']
    email = request.form['Email']
    id = request.form.get('id')
    
    
    cur = judecatori.mysql.connection.cursor()
    
    cur.execute("Select CNP from judecatori")
    cnp_data = cur.fetchall()
    cnp_data = [item[0] for item in cnp_data]   
    
    cur.execute("UPDATE Judecatori SET Nume = %s, Prenume = %s, CNP = %s, Telefon = %s, Email = %s  WHERE JudecatorID = %s", (nume, prenume, cnp, telefon, email, id))
    
    judecatori.mysql.connection.commit()
    cur.close()
    
    return redirect(url_for('judecatori.judecatori_page')) 


@judecatori.route('/delete_judecator/<id>', methods = ['POST'])
def delete(id):
    print("received ID: ", id)
    cur = judecatori.mysql.connection.cursor()
    
    delete_query = "DELETE FROM judecatori WHERE JudecatorID = %s"
    cur.execute(delete_query, (id,)) # Delete the record
    judecatori.mysql.connection.commit()
    
    cur.execute("Delete from judecatoridosare where JudecatorID = %s", (id,))
    cur.close()
    
    return redirect(url_for('judecatori.judecatori_page'))

@judecatori.route('/judecator_search/name=<judecator>', methods=['GET', 'POST'])
def judecator_page_search(judecator):
    cur = judecatori.mysql.connection.cursor()
    
    cur.execute("Select CONCAT(Nume , ' ' , Prenume) as NumeJudecator from Judecatori")
    data = cur.fetchall()
    data = [item[0] for item in data]
    
    if len(judecator.split()) == 1:
        nume = judecator
        prenume = ""
    else:
        nume, prenume = judecator.split()
    
    if judecator in data:

        cur.execute('''select J.JudecatorID, CONCAT(J.Nume, ' ', J.Prenume) as Judecator, J.CNP, J.        
                    Telefon, J.Email,
                    (Select GROUP_CONCAT(distinct D.Numar) from dosare D
                    join judecatoridosare JD on JD.DosarID = D.DosarID
                    where JD.JudecatorID = J.JudecatorID) as Dosare
                    from Judecatori J
                    where J.Nume = %s and J.Prenume = %s
                    order by Judecator
                    ''', [nume, prenume])
        
        judecatori_data = cur.fetchall()
        cur.close()
        
        return render_template("judecatori/judecatori_search_result.html", judecatori_data = judecatori_data)
    elif judecator not in data:
        cur.close()
        route = 'judecatori.judecatori_page'
        title = 'Lista Judecatori'
        error = 'Nu s-a gasit niciun rezultat. Accesati din nou pagina Judecatori si cautati din nou.'
        return render_template("error.html", route = route, title = title, error = error)