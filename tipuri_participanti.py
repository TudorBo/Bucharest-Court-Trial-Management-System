from flask import render_template, Blueprint, request, redirect, url_for, session, flash

tipuri_participanti = Blueprint("tipuri_participanti", __name__, static_folder="static", template_folder="templates")

@tipuri_participanti.route('/tipuri_participanti', methods=['GET', 'POST'])
def tipuri_participanti_page():
    
    cur = tipuri_participanti.mysql.connection.cursor()
    
    cur.execute(''' Select TP.Nume, TP.Descriere, count(PD.ParticipantID) as Numar_participanti from participantidosare PD
                join tipuriparticipanti TP on PD.TipParticipantID = TP.TipParticipantID
                group by TP.Nume
                ''')
    
    tipuri_participanti_data = cur.fetchall()
    cur.close()

    return render_template('tipuri_participanti/tipuri_participanti.html', tipuri_participanti_data = tipuri_participanti_data)

@tipuri_participanti.route('/tip_participanti_search/name=<path:tip>', methods=['POST'])
def tipuri_participanti_search_page(tip):
    
    cur = tipuri_participanti.mysql.connection.cursor()
    
    cur.execute('''Select Nume from tipuriparticipanti''')
    data = cur.fetchall()
    data = [item[0] for item in data]
    
    if tip in data:
        
        cur.execute(''' Select TP.Nume, TP.Descriere, count(PD.ParticipantID) as Numar_participanti from participantidosare PD
                    join tipuriparticipanti TP on PD.TipParticipantID = TP.TipParticipantID
                    where TP.Nume = %s
                    group by TP.Nume
                    ''', [tip])
        
        tipuri_participanti_data = cur.fetchall()
        
        cur.close()
        return render_template('tipuri_participanti/tipuri_participanti_search_result.html', tipuri_participanti_data = tipuri_participanti_data)
    elif tip not in data:
        cur.close()
        route = 'tipuri_participanti.tipuri_participanti_page'
        title = 'Lista Tipuri Participanti'
        error = 'Nu s-a gasit niciun rezultat. Accesati din nou pagina Tipuri Participanti si cautati din nou.'
        return render_template('error.html', route = route, title = title, error = error)