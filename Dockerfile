# 1. Image de base
FROM python:3.12-slim

# 2. Variables d’environnement pour désactiver les invites interactives
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Installer Firefox et Geckodriver
RUN apt-get update && \
    apt-get install -y firefox-esr wget gnupg && \
    wget -q https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux64.tar.gz && \
    tar -xzf geckodriver-v0.36.0-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-v0.36.0-linux64.tar.gz


# 4. Définir le dossier de travail
WORKDIR /app

# 5. Copier le code et les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 6. Commande de lancement des tests
CMD ["pytest", "tests/", "--html=reports/report.html", "--self-contained-html"]
