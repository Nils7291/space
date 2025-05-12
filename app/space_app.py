import streamlit as st
import requests
import pandas as pd

# API-Endpunkt für die Anzahl der Menschen im Weltraum
url_astro = "http://api.open-notify.org/astros.json"
url_iss_location = "http://api.open-notify.org/iss-now.json"

# Sende GET-Anfrage an die API für Menschen im Weltraum
response_astro = requests.get(url_astro)
data_astro = response_astro.json()

# Sende GET-Anfrage an die API für den aktuellen ISS-Standort
response_iss = requests.get(url_iss_location)
data_iss = response_iss.json()

# Streamlit App - Titel und Beschreibung
st.title('Aktuelle Informationen zu Menschen im Weltraum und ISS')
st.markdown("""
    Diese Anwendung zeigt die aktuelle Anzahl der Menschen, die sich im Weltraum befinden,
    sowie deren Namen und den aktuellen Standort der Internationalen Raumstation (ISS).
    Die Daten werden in Echtzeit von den Open Notify APIs abgerufen.
""")

# Zeige die Anzahl der Menschen im Weltraum
st.subheader(f"Es gibt aktuell {data_astro['number']} Menschen im Weltraum:")

# Zeige die Namen der Menschen im Weltraum
for astronaut in data_astro['people']:
    st.write(f"- {astronaut['name']} (Raumschiff: {astronaut['craft']})")

# Zeige den aktuellen ISS-Standort
iss_lat = float(data_iss['iss_position']['latitude'])
iss_lon = float(data_iss['iss_position']['longitude'])

# Zeige die Koordinaten der ISS
st.subheader(f"Aktuelle Position der Internationalen Raumstation (ISS):")
st.write(f"Breitengrad: {iss_lat}, Längengrad: {iss_lon}")

# Visualisiere die ISS-Position auf der Karte
st.markdown("""
    **Die Internationale Raumstation (ISS) befindet sich an dem oben genannten Punkt auf der Karte.**
""")

# Datenrahmen für den ISS-Standort
iss_location = pd.DataFrame({
    'lat': [iss_lat],
    'lon': [iss_lon]
})

# Stelle sicher, dass der Zoom und die Kartenausschnitt gut eingestellt sind
st.map(iss_location, zoom=1)
