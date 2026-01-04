from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils import wait_for_table, download_geckodriver

def main():
    # Descargar geckodriver automáticamente
    driver_path = download_geckodriver()
    
    # Configurar Firefox headless
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options, executable_path=driver_path)

    try:
        url = "https://int.soccerway.com/national/spain/primera-division/"
        driver.get(url)

        tabla, filas = wait_for_table(driver)
        print(f"Filas encontradas: {len(filas)}")

        for fila in filas:
            columnas = fila.find_elements("tag name", "td")
            datos = [columna.text for columna in columnas]
            print(datos)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

