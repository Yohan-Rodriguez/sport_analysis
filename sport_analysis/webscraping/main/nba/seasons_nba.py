from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ==================================================================================================================== #
# CHOOSE NBA LEAGUE                                                                                                    #
# ==================================================================================================================== #
def choose_options_menu(driver, choose_option):
    
    """
    Clic en la página web para cambiar la temporada de la NBA

    Args:
        driver: WebDriver
        choose_option: Indica la temrporada a la que se ingresará por cada iteración

    Returns:
        Función sin return.

    Raises:
        Raise exception

    Examples:
        >>> choose_options_menu(driver, choose_option=2)
        Clic para accedeer a la termporada que esta en la posición 2 de la lista <ul> desplegada
        >>> choose_options_menu(driver, choose_option=4)
        Clic para accedeer a la termporada que esta en la posición 4 de la lista <ul> desplegada
        >>> choose_options_menu(driver, choose_option=10)
        Clic para accedeer a la termporada que esta en la posición 10 de la lista <ul> desplegada        
    """

    try:
        # XPATH del botón del menú despegable 
        xpath_button_menu = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/button'    

        # Buscar el botón del menú despegable dentro de la página web
        button_conference = driver.find_element(By.XPATH, xpath_button_menu)

        # Obtener el menú despegable
        driver.execute_script("arguments[0].click();", button_conference)

        # XPATH de la lista desplegable que contiene las temporadas (sesons)
        xpath_ul = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/ul/li[1]'

        # Esperar a que el elemento <ul> se despliegue después de hacer clic en el botón
        ul_conference = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, xpath_ul)))  
        
        # XPATH de la etiqueta <li>
        xpath_li = f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/ul/li[{choose_option}]'
        
        # Acceder a la opcione <li> especifica dentro de la etiqueta <ul>
        season_li = ul_conference.find_element(By.XPATH, xpath_li)
        
        # Hacer clic en una opción específica
        driver.execute_script("arguments[0].click();", season_li)

    except:
        raise ('Error en la función "seasons_nba.py.choose_options_menu"...')
# END --------- CHOOSE NBA LEAGUE                                                                                      #
# ==================================================================================================================== #