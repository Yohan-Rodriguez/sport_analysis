
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .list_css import get_xpath_button_previous


# ==================================================================================================================== #
# XPATH BUTTON's CONTAINER                                                                                             #
# ==================================================================================================================== #
def search_change_season(driver):
    # Lista de los XPATH del cambio de Season
    list_xpath_div_b = [
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div'
                       ] 

    # Iterar sonre la lista "list_xpath_div_b"
    for xpath_div_contain_b in list_xpath_div_b:
        try:
            # Buscar el xpath dentro de la página web
            div_contain_button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, xpath_div_contain_b)))  

            break

        except Exception as e:
            # Si ya no hay más elementos sobre los que iterar, lanzar la siguiente exception
            if xpath_div_contain_b == list_xpath_div_b[-1]:
                raise Exception(f'\nERROR: XPATH del cambio de Season no encontrado...\n{e}')
            
    return div_contain_button
# END --------- XPATH BUTTON's CONTAINER                                                                               #
# ==================================================================================================================== #


# ==================================================================================================================== #
# DROPDOWN MENU                                                                                                        #
# ==================================================================================================================== #
def click_on_dropdawn_menu(driver, div_contain_button, season):
    # Dentro del div principal, encontrar el botón del menú desplegable
    button_menu = div_contain_button.find_element(By.TAG_NAME, 'button')

    # Obtener el valor del atributo "aria-controls" del botón
    valor_aria_controls = button_menu.get_attribute('aria-controls')
    # Ejemplo: valor_aria_controls = 'downshift-1024-menu'

    # Extraer el número toggle del valor del atributo "aria-controls" para usar en el "css_buton_menu"
    num_toggle = valor_aria_controls.split('-')[1]
    
    # CSS del botón del menú despegable 
    css_button_menu = f'#downshift-{num_toggle}-toggle-button'
    
    # Bsucar el botón del menú despegable dentro de la página web
    button_season = driver.find_element(By.CSS_SELECTOR, css_button_menu)

    # Obtener el ménu despegable
    # button_season.click()
    driver.execute_script("arguments[0].click();", button_season)
    
    # CSS de la lista desplegable que contiene las temporadas (sesons)
    css_ul = f'#{valor_aria_controls}'
    # Ejemplo: css_ul = #downshift-1024-menu
    
    # Esperar a que el elemento <ul> se despliegue después de hacer clic en el botón
    ul_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_ul)))  
    
    # Acceder a las opciones dentro del <ul>
    opciones_ul = ul_element.find_elements(By.TAG_NAME, 'li')
    
    # Hacer clic en una opción específica
    # opciones_ul[season].click()
    driver.execute_script("arguments[0].click();", opciones_ul[season])
# END --------- DROPDOWN MENU                                                                                          #
# ==================================================================================================================== #
 
 
# ==================================================================================================================== #
# BUTTON PREVIOUS                                                                                                      #
# ==================================================================================================================== #
def search_button_b(driver, flag_no_found_previous_b, button_previous=None, b_previous=None, initial=False):
    
    button_previous = button_previous
    b_previous = b_previous
    
    if flag_no_found_previous_b:

        # Obtener lista de XPATH's del "button_previous"
        xpath_previous = get_xpath_button_previous()

        for b_previous in xpath_previous:
            try:
                # print(f'Buscando el button con XPATH: {b_previous}...')
                # Buscar y dar clic sobre el botón dentro de la página web
                button_previous = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, b_previous)))

                flag_no_found_previous_b = False

                break

            except Exception:
                if b_previous == xpath_previous[-1]:

                    # Si initial=False
                    if not initial:
                        raise Exception(f'\nError al dar clic en "button_previous"...')
                    
                    # Si initial=True
                    else:   
                        pass
                
                continue
            
    else:
        try:                            
            driver.execute_script("arguments[0].click();", button_previous)

        except:
            try:
                button_previous = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, b_previous)))
                driver.execute_script("arguments[0].click();", button_previous)
                # print('\nCheck')
            except:
                raise Exception('No hay Error (Fin de los partidos de la liga actuaL...)')
        
    return button_previous, flag_no_found_previous_b, b_previous
# END --------- BUTTON PREVIOUS                                                                                        #
# ==================================================================================================================== #
        