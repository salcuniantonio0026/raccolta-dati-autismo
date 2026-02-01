#EMAIL_RECEIVER = "salcuniantonio00@gmail.com"   # o un’altra email se preferisci
import streamlit as st
import smtplib
from email.mime.text import MIMEText
import pandas as pd
from datetime import date
from io import StringIO

# -----------------------------------------
# CONFIGURAZIONE PAGINA
# -----------------------------------------
st.set_page_config(
    page_title="Raccolta Dati – Funzioni Esecutive",
    layout="centered"
)

st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>📊 Raccolta Dati – Funzioni Esecutive</h1>
    <p style='text-align: center; font-size: 16px; color: #555;'>
        Compila una scheda per ogni attività svolta dal bambino.
    </p>
""", unsafe_allow_html=True)

# -----------------------------------------
# CONFIGURAZIONE EMAIL
# -----------------------------------------
EMAIL_SENDER = "salcuniantonio00@gmail.com"
EMAIL_PASSWORD = "esouvldgawxywvyn"
#EMAIL_RECEIVER = "gennaro.fiananese@gmail.com"
EMAIL_RECEIVER = "salcuniantonio00@gmail.com"   # o un’altra email se preferisci

# -----------------------------------------
# SEZIONE 1 — DATI DEL BAMBINO
# -----------------------------------------
st.markdown("<h2 style='color:#1A5276;'>👤 Dati del bambino</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    data = st.date_input("Data", value=date.today())
with col2:
    eta = st.text_input("Età (MM/AAAA)", help="Inserire solo mese e anno, es. 04/2010")

chiave = st.text_input("Chiave primaria", help="Identificativo univoco del bambino")

# -----------------------------------------
# SEZIONE 2 — FUNZIONI ESECUTIVE
# -----------------------------------------
st.markdown("<h2 style='color:#1A5276;'>🧠 Compito svolto</h2>", unsafe_allow_html=True)

funzioni = {
    "Attenzione": [
        "Cercare oggetti di un colore specifico",
        "Ripetere una sequenza di numeri",
        "Stop & Go (verde vai, rosso stop)",
        "Cambiare regola di gioco",
        "Preparare zaino",
        "Riconoscere emozioni",
        "Ordinare giochi",
        "Gioco 'trova le differenze'",
        "Seguire istruzioni a 2 step",
        "Attività di cancellazione (barrare figure target)"
    ],
    "Memoria di lavoro": [
        "Gioco 'trova le differenze'",
        "Ripetere sequenza di parole",
        "Simon says (solo se preceduto)",
        "Ordinare oggetti per colore poi forma",
        "Sequenza per vestirsi",
        "Respirazione guidata",
        "Mettere oggetti in scatole"
    ],
    "Inibizione comportamentale": [
        "Seguire con il dito un percorso su foglio",
        "Memory con carte",
        "Non toccare oggetti target",
        "Usare oggetto in modo alternativo",
        "Preparare tavolo",
        "Pausa calmante",
        "Classificare per colore"
    ],
    "Flessibilità cognitiva": [
        "Battere le mani solo quando sente una parola target",
        "Ripetere una sequenza di movimenti",
        "Aspettare turno",
        "Cambiare percorso",
        "Costruire puzzle",
        "Uso di immagini emotive",
        "Classificare per forma"
    ],
    "Pianificazione": [
        "Puzzle con tempo limitato",
        "Ricordare 3 oggetti visti prima",
        "Giochi con regole",
        "Gioco 'ora diverso'",
        "Ordinare immagini di una storia",
        "Termometro emotivo",
        "Ordinare grande-piccolo"
    ],
    "Autoregolazione emotiva": [
        "Ascoltare una storia e rispondere a domande",
        "Ricordare istruzioni orali",
        "Battere le mani solo al segnale giusto",
        "Cambiare strategia",
        "Preparare merenda",
        "Raccontare emozione",
        "Mettere in sequenza"
    ],
    "Organizzazione": [
        "Memory visivo",
        "Ripetere una frase complessa",
        "Non rispondere subito",
        "Stesso gioco con regole nuove",
        "Sequenza per lavarsi mani",
        "Stringere palla antistress",
        "Usare contenitori",
        "Ordinare immagini per sequenza",
        "Gioco 'Simon says'",
        "Resistere a premio visivo",
        "Passare da un compito a un altro",
        "Costruire torre",
        "Esercizi di rilassamento",
        "Preparare materiale",
        "Seguire istruzioni a 2 step",
        "Ricordare percorso fatto prima",
        "Cambiare risposta automatica",
        "Cambiare ordine",
        "Preparare attività",
        "Visualizzare calma",
        "Riordinare stanza",
        "Gioco delle campanelle (suono = azione)",
        "Ripetere suoni in ordine",
        "Gioco del semaforo",
        "Modificare sequenza",
        "Seguire piano a 3 step",
        "Gioco del semaforo emotivo",
        "Sistemare cartellina",
        "Ricercare simboli uguali su scheda",
        "Ricordare immagini viste per 10 secondi",
        "Rimanere fermo per 10 secondi",
        "Accettare errore e riprovare",
        "Completare labirinto",
        "Attendere premio",
        "Separare per categorie",
        "Attività di cancellazione (barrare figure target)",
        "Riordinare immagini viste prima",
        "Non imitare movimento",
        "Usare materiali diversi",
        "Pianificare disegno",
        "Chiedere aiuto",
        "Riordinare immagini",
        "Guardare un breve video e raccontarlo",
        "Ricordare colori mostrati",
        "Trattenere risposta motoria",
        "Adattare soluzione",
        "Organizzare gioco",
        "Usare carta emotiva",
        "Archiviare schede",
        "Copiare un disegno semplice",
        "Ripetere filastrocca breve",
        "Ritardare scelta",
        "Gioco delle categorie",
        "Sequenza di cucina finta",
        "Riconoscere rabbia",
        "Preparare zaino",
        "Seguire una linea tratteggiata",
        "Ripetere azioni in ordine",
        "Giochi di autocontrollo",
        "Associare in modo nuovo",
        "Costruire con blocchi",
        "Cambiare attività",
        "Sistemare tavolo"
    ]
}

funzione = st.selectbox("Funzione esecutiva", list(funzioni.keys()))
esercizio = st.selectbox("Esercizio", funzioni[funzione])

# -----------------------------------------
# SEZIONE 3 — TENTATIVI
# -----------------------------------------
st.markdown("<h2 style='color:#1A5276;'>📈 Valutazione tentativi</h2>", unsafe_allow_html=True)

tentativi = {}
cols = st.columns(5)

for i in range(1, 11):
    col = cols[(i - 1) % 5]
    with col:
        tentativi[f"Tentativo_{i}"] = st.slider(f"Tentativo {i}", 0, 5, 0)

note = st.text_area("Note aggiuntive")

# -----------------------------------------
# FUNZIONE EMAIL MIGLIORATA
# -----------------------------------------
def invia_email(df_row: pd.DataFrame):
    html_table = df_row.to_html(index=False, border=0, justify="left")

    html_body = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #333;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin-top: 20px;
                }}
                th {{
                    background-color: #2E86C1;
                    color: white;
                    padding: 10px;
                    border-bottom: 2px solid #ddd;
                }}
                td {{
                    padding: 10px;
                    border-bottom: 1px solid #ddd;
                }}
                tr:nth-child(even) {{
                    background-color: #f8f9f9;
                }}
            </style>
        </head>
        <body>
            <h2 style="color:#2E86C1;">Nuova raccolta dati – Funzioni esecutive</h2>
            <p>Ecco i dati inviati dal professionista:</p>
            {html_table}
        </body>
    </html>
    """

    msg = MIMEText(html_body, "html")
    msg["Subject"] = "Nuova raccolta dati – Funzioni esecutive"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

# -----------------------------------------
# SUBMIT
# -----------------------------------------
if st.button("Invia dati"):
    if not eta or not chiave:
        st.error("Compila almeno Età e Chiave primaria prima di inviare.")
    else:
        record = {
            "Data": data.isoformat(),
            "Età": eta,
            "Chiave": chiave,
            "Funzione": funzione,
            "Esercizio": esercizio,
            "Note": note
        }
        record.update(tentativi)

        df = pd.DataFrame([record])

        st.success("Dati inviati correttamente. Controlla la tua email.")
        st.dataframe(df)

        df.to_csv("raccolta_dati_locale.csv", mode="a", header=False, index=False)

        try:
            invia_email(df)
        except Exception as e:
            st.error(f"Errore nell'invio email: {e}")
