from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait_for_table(driver, timeout=15):
    """Espera a que la tabla de posiciones de Soccerway cargue correctamente."""
    wait = WebDriverWait(driver, timeout)
    # esperar tabla
    tabla = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.table")))
    # esperar al menos una fila
    filas = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.table tbody tr")))
    return tabla, filas
