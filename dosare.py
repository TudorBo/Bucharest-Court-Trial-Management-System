from flask import render_template, Blueprint, request, redirect, url_for, session, flash

dosare = Blueprint("dosare", __name__, static_folder="static", template_folder="templates")

@dosare.route('/dosare', methods=['GET', 'POST'])
def dosare_page():
    
    cur1 = dosare.mysql.connection.cursor()    

    cur1.execute('''Select D.DosarID, D.Numar, D.Descriere, L.Nume from Dosare D
                    join Legi L on D.LegeID = L.LegeID
                ''')
    data1 = cur1.fetchall()
    cur1.close()
    
    cur2 = dosare.mysql.connection.cursor()
    cur2.execute('''Select D1.Nume from Dosare D
                    join Directii D1 on D.DirectieID = D1.DirectieID
                ''')
    data2 = cur2.fetchall()
    cur2.close()
    
    cur3 = dosare.mysql.connection.cursor()
    cur3.execute('''Select PD.DosarID, concat(P.Nume, ' ' , P.Prenume) as Participant from Dosare D
                    left join participantidosare PD on D.DosarID = PD.DosarID
                    left join participanti P on PD.ParticipantID = P.ParticipantID
                ''')
    data3 = cur3.fetchall()
    cur3.close()
    
    cur4 = dosare.mysql.connection.cursor()
    cur4.execute(''' Select TP.Nume from Dosare D
                    left join participantidosare PD on D.DosarID = PD.DosarID
                    left join tipuriparticipanti TP on PD.TipParticipantID = TP.TipParticipantID
                ''')
    data4 = cur4.fetchall()
    cur4.close()

    participant_data = []
    for i in range(len(data3)):
        participant_data.append(data3[i] + data4[i])
        
    cur5 = dosare.mysql.connection.cursor()
    cur5.execute('''Select D.DosarID,
                    (
                        Select GROUP_CONCAT(CONCAT(J.Nume, ' ', J.Prenume))
                        from judecatori J
                        left join judecatoridosare JD ON J.JudecatorID = JD.JudecatorID
                        where JD.DosarID = D.DosarID
                    ) AS Judecatori
                from 
                    Dosare D;
                ''')
    data5 = cur5.fetchall()
    cur5.close()
    
    dosar_data = []
    for i in range(len(data1)):
        dosar_data.append(data1[i] + data2[i] + data5[i])
    
    return render_template('dosare_pages/dosare.html', dosare = dosar_data, participanti = participant_data)


@dosare.route('/dosare_search/number=<dosar>', methods=['GET', 'POST'])
def dosare_page_search(dosar):
    cur1 = dosare.mysql.connection.cursor()
    cur1.execute('''Select D.Numar from Dosare D''')
    data = cur1.fetchall()
    data = [item[0] for item in data]
    
    dosar = int(dosar)
    
    if dosar in data:

        cur1.execute('''Select D.DosarID, D.Numar, D.Descriere, L.Nume from Dosare D
                        join Legi L on D.LegeID = L.LegeID
                        where D.Numar = %s
                    ''', [dosar])
        data1 = cur1.fetchall()
        cur1.close()
        
        cur2 = dosare.mysql.connection.cursor()
        cur2.execute('''Select D1.Nume from Dosare D
                        join Directii D1 on D.DirectieID = D1.DirectieID
                    ''')
        data2 = cur2.fetchall()
        cur2.close()
        
        cur3 = dosare.mysql.connection.cursor()
        cur3.execute('''Select PD.DosarID, concat(P.Nume, ' ' , P.Prenume) as Participant from Dosare D
                        left join participantidosare PD on D.DosarID = PD.DosarID
                        left join participanti P on PD.ParticipantID = P.ParticipantID
                    ''')
        data3 = cur3.fetchall()
        cur3.close()
        
        cur4 = dosare.mysql.connection.cursor()
        cur4.execute(''' Select TP.Nume from Dosare D
                        left join participantidosare PD on D.DosarID = PD.DosarID
                        left join tipuriparticipanti TP on PD.TipParticipantID = TP.TipParticipantID
                    ''')
        data4 = cur4.fetchall()
        cur4.close()

        participant_data = []
        for i in range(len(data3)):
            participant_data.append(data3[i] + data4[i])
            
        cur5 = dosare.mysql.connection.cursor()
        cur5.execute('''Select D.DosarID,
                        (
                            Select GROUP_CONCAT(CONCAT(J.Nume, ' ', J.Prenume))
                            from judecatori J
                            left join judecatoridosare JD ON J.JudecatorID = JD.JudecatorID
                            where JD.DosarID = D.DosarID
                        ) as Judecatori
                    from 
                        Dosare D;
                    ''')
        data5 = cur5.fetchall()
        cur5.close()
        
        dosar_data = []
        for i in range(len(data1)):
            dosar_data.append(data1[i] + data2[i] + data5[i])
        
        return render_template('dosare_pages/dosare_search_result.html', dosare = dosar_data, participanti = participant_data)
    elif dosar not in data:
        route = "dosare.dosare_page"
        title="Lista Dosare"
        error = "Nu s-a gasit niciun rezultat. Accesati din nou pagina Dosare si cautati din nou"
        return render_template('error.html', route = route, title = title, error = error)