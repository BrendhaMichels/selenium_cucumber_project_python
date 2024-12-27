from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

try:
    # Acessa uma página
    driver.get("https://www.google.com")
    
    # Encontra o campo de busca e insere texto
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    
    # Pressiona Enter
    search_box.submit()
    
    # Exibe o título da página
    print(f"Título da página: {driver.title}")
finally:
    # Fecha o navegador
    driver.quit()
