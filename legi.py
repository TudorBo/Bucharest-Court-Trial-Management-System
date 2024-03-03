from flask import render_template, Blueprint, request, redirect, url_for, session, flash

legi = Blueprint("legi", __name__, static_folder="static", template_folder="templates")

@legi.route('/legi', methods=['GET', 'POST'])
def legi_page():
    cur = legi.mysql.connection.cursor()
    
    cur.execute('''
                Select L.LegeID, L.Nume, L.Descriere,
                (Select GROUP_CONCAT(D.Numar)
                from Dosare D
                where D.LegeID = L.LegeID) 
                as DosareAsociate
                from Legi L
                order by L.Nume
                ''')
    
    legi_data = cur.fetchall()
    
    return render_template("legi/legi.html", legi_data = legi_data)
    
@legi.route('/add_legi', methods=['POST'])
def add():
    nume = request.form['Nr.Lege']
    descriere = request.form['Descriere']
    
    cur = legi.mysql.connection.cursor()

    # Add a new item
    cur.execute("INSERT INTO Legi (Nume, Descriere) VALUES (%s, %s)", (nume, descriere))
    flash("Legea a fost adaugata cu succes!", "success")

    legi.mysql.connection.commit()
    cur.close()

    return redirect(url_for('legi.legi_page'))  # replace with the name of your view function


@legi.route('/update_legi', methods=['post'])
def update():
    nume = request.form['Nr.Lege']
    descriere = request.form['Descriere']
    id = request.form.get('id')
    
    cur = legi.mysql.connection.cursor()
    cur.execute("UPDATE Legi SET Nume = %s, Descriere = %s WHERE LegeID = %s", (nume, descriere, id))
    legi.mysql.connection.commit()
    cur.close()
        
    return redirect(url_for('legi.legi_page')) 


@legi.route('/delete_legi/<string:id>', methods = ['POST'])
def delete(id):
    
    cur = legi.mysql.connection.cursor()
    
    delete_query = "DELETE FROM Legi WHERE LegeID = %s"
    cur.execute(delete_query, (id,)) # Delete the record
    legi.mysql.connection.commit()
    cur.close()
    
    return redirect(url_for('legi.legi_page'))


@legi.route('/legi_search/number=<path:lege>', methods=['GET', 'POST'])
def lege_page_search(lege):
    cur = legi.mysql.connection.cursor()
    
    cur.execute("Select Nume from Legi")
    data = cur.fetchall()
    data = [item[0] for item in data]
    
    if lege in data:    
        cur.execute('''
                    Select L.LegeID, L.Nume, L.Descriere,
                    (Select GROUP_CONCAT(D.Numar)
                    from Dosare D
                    where D.LegeID = L.LegeID) 
                    as DosareAsociate
                    from Legi L
                    where L.Nume = %s
                    order by L.Nume
                    
                    ''', [lege])
        legi_data = cur.fetchall()
        return render_template("legi/legi_search_result.html", legi_data = legi_data)   
    elif lege not in data:
        route = "legi.legi_page"
        title="Lista Legi";
        error = "Nu exista nicio lege cu acest nume!"
        return render_template("error.html", error = error, title = title, route = route)
    