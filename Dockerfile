# Verwende das offizielle Python-Image
FROM python:3.12-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere alle Dateien aus dem lokalen app-Verzeichnis in den Container
COPY app /app

# Installiere die Abhängigkeiten
RUN pip install -r /app/requirements.txt

# Exponiere den Streamlit-Port
EXPOSE 8501

# Führe die Streamlit-App aus
CMD ["streamlit", "run", "/app/space_app.py"]
