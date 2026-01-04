from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils import wait_for_table

def main():
    # Configurar Firefox
    options = Options()
    options.set_preference("network.proxy.type", 0)
    options.headless = True  # importante para Render

    driver = webdriver.Firefox(options=options)
    
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
