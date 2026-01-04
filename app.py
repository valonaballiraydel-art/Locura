from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils import download_geckodriver, wait_for_table, parse_table

app = Flask(__name__)

# Descargar geckodriver al iniciar
DRIVER_PATH = download_geckodriver()

@app.route("/tabla", methods=["GET"])
def get_tabla():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=DRIVER_PATH)

    try:
        url = "https://int.soccerway.com/national/spain/primera-division/"
        driver.get(url)
        _, filas = wait_for_table(driver)
        data = parse_table(filas)
        return jsonify({"tabla": data})
    finally:
        driver.quit()

if __name__ == "__main__":
    # Render suele usar $PORT
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
