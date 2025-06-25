#!/bin/bash

# Crée le dossier reports/ s'il n'existe pas
mkdir -p reports

# Lance les tests et génère le rapport HTML
pytest tests/ --html=reports/report.html --self-contained-html

# Affiche un message de fin
echo "✔ Tests completed. HTML report generated at: reports/report.html"