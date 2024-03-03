from flask import render_template, Blueprint, request, redirect, url_for, session, flash

directii = Blueprint("directii", __name__, static_folder="static", template_folder="templates")

@directii.route('/directii', methods=['GET', 'POST'])
def directii_page():
    cur = directii.mysql.connection.cursor()
    
    cur.execute('''
                Select DR.DirectieID, DR.Nume, DR.Descriere, GROUP_CONCAT(D.Numar) as DosareAsociate
                from Directii DR
                left join Dosare D ON DR.DirectieID = D.DirectieID
                group by DR.DirectieID, DR.Nume, DR.Descriere
                order by DR.Nume
                ''')
    
    directii_data = cur.fetchall()
    
    cur.close()
    
    return render_template("directii/directii.html", directii_data = directii_data)

@directii.route('/add_directie', methods=['POST'])
def add():
    nume = request.form['Nume']
    descriere = request.form['Descriere']
    cur = directii.mysql.connection.cursor()

    cur.execute("INSERT INTO Directii (Nume, Descriere) VALUES (%s, %s)", (nume, descriere))
    directii.mysql.connection.commit()

    cur.close()

    return redirect(url_for('directii.directii_page'))

@directii.route('/update_directie', methods=['POST'])
def update():
    nume = request.form['Nume']
    descriere = request.form['Descriere']
    id = request.form.get('id')
    cur = directii.mysql.connection.cursor()

    # Update Directii
    cur.execute("UPDATE Directii SET Nume = %s, Descriere = %s WHERE DirectieID = %s", (nume, descriere, id))
    directii.mysql.connection.commit()

    cur.close()

    return redirect(url_for('directii.directii_page'))

@directii.route('/delete_directie/<string:id>', methods=['POST','GET'])
def delete(id):
    print("received ID: ", id)
    
    cur = directii.mysql.connection.cursor()
    cur.execute("DELETE FROM Directii WHERE DirectieID = %s", (id,))
    directii.mysql.connection.commit()
    cur.close()
    
    print(f"deleted record with ID: {id}")

    return redirect(url_for('directii.directii_page'))

@directii.route('/directie_search/name=<directie>', methods=['GET', 'POST'])
def directie_page_search(directie):
    cur = directii.mysql.connection.cursor()
    
    cur.execute("Select Nume from Directii")
    data = cur.fetchall()
    data = [item[0] for item in data]
    
    if directie in data:

        cur.execute('''select DR.DirectieID, DR.Nume, DR.Descriere,
                    (Select GROUP_CONCAT(distinct D.Numar) from dosare D
                    where D.DirectieID = DR.DirectieID) as Dosare
                    from Directii DR
                    where DR.Nume = %s
                    order by DR.Nume
                    ''', [directie])
        
        directii_data = cur.fetchall()
        cur.close()
        
        return render_template("directii/directii_search_result.html", directii_data = directii_data)
    else:
        route = "directii.directii_page"
        title = "Lista Directii"
        error = "Nu s-a gasit niciun rezultat. Accesati din nou pagina Directii si cautati din nou."
        
        return render_template("error.html", error = error, title = title, route = route)