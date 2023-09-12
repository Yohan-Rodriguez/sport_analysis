from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ==================================================================================================================== #
# CHOOSE NBA LEAGUE                                                                                                    #
# ==================================================================================================================== #
def choose_options_menu(driver, num_toggle, choose_option):
    # CSS del botón del menú despegable 
    css_button_menu = f'#downshift-{num_toggle}-toggle-button'    

    # Buscar el botón del menú despegable dentro de la página web
    button_conference = driver.find_element(By.CSS_SELECTOR, css_button_menu)

    # Obtener el menú despegable
    driver.execute_script("arguments[0].click();", button_conference)

    # CSS de la lista desplegable que contiene las temporadas (sesons)
    css_ul = f'#downshift-{num_toggle}-menu'

    # Esperar a que el elemento <ul> se despliegue después de hacer clic en el botón
    ul_conference = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_ul)))  
    
    # Acceder a las opciones dentro del <ul>
    opciones_ul = ul_conference.find_elements(By.TAG_NAME, 'li')
    
    # Hacer clic en una opción específica
    # opciones_ul[season].click()
    driver.execute_script("arguments[0].click();", opciones_ul[choose_option])
# END --------- CHOOSE NBA LEAGUE                                                                                      #
# ==================================================================================================================== #