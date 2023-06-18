# Pobranie obrazu bazowego Python
FROM python:3.9

# Utworzenie i ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie plików requirements
COPY requirements.txt .

# Instalacja zależności
RUN pip install -r requirements.txt

# Skopiowanie kodu aplikacji
COPY . .

# Uruchomienie serwera Django
CMD python manage.py runserver 0.0.0.0:8000
