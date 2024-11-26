import os
import subprocess
from datetime import datetime, timedelta
import random

# Configuración
REPO_NAME = "random-contribuciones"
AUTHOR_NAME = "YukaC"
AUTHOR_EMAIL = "agusyuk@hotmail.com"

# Generar un patrón aleatorio
def generar_patron_aleatorio(weeks, days_per_week):
    return [[random.randint(0, 4) for _ in range(days_per_week)] for _ in range(weeks)]

# Configurar el número de semanas y días por semana (52 semanas y 7 días)
PATTERN = generar_patron_aleatorio(52, 7)

def create_repo():
    """Crea un repositorio local si no existe."""
    if not os.path.exists(REPO_NAME):
        os.makedirs(REPO_NAME)
        subprocess.run(["git", "init", REPO_NAME])
        print(f"Repositorio '{REPO_NAME}' creado e inicializado.")

def set_git_config():
    """Configura nombre y correo electrónico de Git."""
    subprocess.run(["git", "config", "--global", "user.name", AUTHOR_NAME])
    subprocess.run(["git", "config", "--global", "user.email", AUTHOR_EMAIL])
    print("Configuración de Git establecida.")

def commit_for_date(repo_path, date, intensity):
    """Realiza commits en una fecha específica."""
    os.chdir(repo_path)
    for _ in range(intensity):
        with open("README.md", "a") as file:
            file.write(f"Commit para {date}\n")
        subprocess.run(["git", "add", "README.md"])
        subprocess.run(
            ["git", "commit", "--date", date.strftime("%Y-%m-%dT%H:%M:%S"), "-m", f"Commit {date}"]
        )
    os.chdir("..")

def draw_pattern(start_date):
    """Dibuja el patrón en el gráfico de contribuciones."""
    repo_path = os.path.abspath(REPO_NAME)
    for week, row in enumerate(PATTERN):
        for day, intensity in enumerate(row):
            if intensity > 0:
                commit_date = start_date + timedelta(weeks=week, days=day)
                commit_for_date(repo_path, commit_date, intensity)

if __name__ == "__main__":
    create_repo()
    set_git_config()
    start_date = datetime.today() - timedelta(days=365)  # Fecha de inicio hace un año
    draw_pattern(start_date)
    print("¡Patrón aleatorio dibujado en tu gráfico de contribuciones!")
