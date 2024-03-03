from flask import render_template, Blueprint, request, redirect, url_for, session, flash

participanti = Blueprint("participanti", __name__, static_folder="static", template_folder="templates")

@participanti.route('/participanti', methods=['GET', 'POST'])
def participanti_page():
    
    cur = participanti.mysql.connection.cursor()
    
    cur.execute('''Select concat(P.Nume, ' ' , P.Prenume)as NumeParticipant, P.CNP, P.Telefon, P.Email,
                    (Select GROUP_CONCAT(distinct D.Numar) from dosare D
                    join participantidosare PD on PD.DosarID = D.DosarID
                    where PD.ParticipantID = P.ParticipantID) as Dosare
                    from participanti P
                ''')
    
    participanti_data = cur.fetchall()
    
    cur.close()
    
    return render_template('participanti/participanti.html', participanti_data = participanti_data)

@participanti.route('/participant_search/name=<participant>', methods=['POST'])
def participant_search_page(participant):
    
    cur = participanti.mysql.connection.cursor()
    
    cur.execute('''Select CONCAT(Nume, ' ', Prenume) as NumeParticipant from participanti''')
    data = cur.fetchall()
    data = [item[0] for item in data]
    
    if len(participant.split()) == 1:
        nume = participant
        prenume = ""
    else:
        nume, prenume = participant.split()
        
    if participant in data:
    
        cur.execute('''Select concat(P.Nume, ' ' , P.Prenume)as NumeParticipant, P.CNP, P.Telefon, P.Email,
                        (Select GROUP_CONCAT(distinct D.Numar) from dosare D
                        join participantidosare PD on PD.DosarID = D.DosarID
                        where PD.ParticipantID = P.ParticipantID) as Dosare
                        from participanti P
                        where P.Nume = %s and P.Prenume = %s
                    ''', [nume, prenume])
        
        participanti_data = cur.fetchall()
           
        cur.close()
        return render_template('participanti/participanti_search_result.html', participanti_data = participanti_data)
    elif participant not in data:
        cur.close()
        route = 'participanti.participanti_page'
        title = 'Lista Participanti'
        error = 'Nu s-a gasit niciun rezultat. Accesati din nou pagina participanti si cautati din nou.'
        return render_template('error.html', route = route, title = title, error = error)   