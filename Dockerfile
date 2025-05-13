# Verwende das offizielle Python-Image
FROM python:3.12-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere alle Dateien aus dem lokalen app-Verzeichnis in den Container
COPY app /app

# Installiere die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Exponiere den gewünschten Port
EXPOSE 8502

# Führe die Streamlit-App auf Port 8502 aus
CMD ["streamlit", "run", "/app/space_app.py", "--server.port=8502"]
