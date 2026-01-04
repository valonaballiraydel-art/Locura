import os
import platform
import zipfile
import tarfile
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

GECKO_VERSION = "v0.34.0"

def download_geckodriver():
    """Descarga geckodriver según el sistema operativo y lo pone en el path actual."""
    system = platform.system()
    
    if system == "Linux":
        url = f"https://github.com/mozilla/geckodriver/releases/download/{GECKO_VERSION}/geckodriver-{GECKO_VERSION}-linux64.tar.gz"
    elif system == "Darwin":
        url = f"https://github.com/mozilla/geckodriver/releases/download/{GECKO_VERSION}/geckodriver-{GECKO_VERSION}-macos.tar.gz"
    elif system == "Windows":
        url = f"https://github.com/mozilla/geckodriver/releases/download/{GECKO_VERSION}/geckodriver-{GECKO_VERSION}-win64.zip"
    else:
        raise Exception("Sistema operativo no soportado")
    
    filename = url.split("/")[-1]
    r = requests.get(url, stream=True)
    with open(filename, "wb") as f:
        f.write(r.content)

    if filename.endswith(".zip"):
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall()
    elif filename.endswith(".tar.gz"):
        with tarfile.open(filename, "r:gz") as tar:
            tar.extractall()
    else:
        raise Exception("Archivo desconocido")

    driver_path = os.path.join(os.getcwd(), "geckodriver.exe" if system=="Windows" else "geckodriver")
    os.environ["PATH"] += os.pathsep + os.getcwd()
    return driver_path

def wait_for_table(driver, timeout=15):
    """Espera a que la tabla de posiciones de Soccerway cargue correctamente."""
    wait = WebDriverWait(driver, timeout)
    tabla = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.table")))
    filas = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.table tbody tr")))
    return tabla, filas

def parse_table(filas):
    """Convierte las filas de la tabla en una lista de diccionarios"""
    data = []
    for fila in filas:
        columnas = fila.find_elements("tag name", "td")
        row = [columna.text for columna in columnas]
        if row:  # ignorar filas vacías
            data.append(row)
    return data
