import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ==================================================================================================================== #
# CHROME DRIVER CONNECTION                                                                                             #
# ==================================================================================================================== #
def inicializar_driver():
    """
    Crear la conexión con el navegador web BRAVE para la tarea automatizada

    Args:

    Returns:
        driver: Conección con el el navagador web

    Examples:     
    """
    options = webdriver.ChromeOptions()
    options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
    driver = webdriver.Chrome(options=options)

    return driver
# END --------- CHROME DRIVER CONNECTION                                                                               #
# ==================================================================================================================== #


# ==================================================================================================================== #
# CHOOSE NBA LEAGUE                                                                                                    #
# ==================================================================================================================== #
def choose_options_menu(driver, choose_option):
    
    """
    Clic en la página web para cambiar la temporada de la NBA

    Args:
        driver: WebDriver
        choose_option: Indica la temporada a la que se ingresará por cada iteración

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
        xpath_button_menu = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/di'\
                            'v[2]/div/div[1]/button'    

        # Buscar el botón del menú despegable dentro de la página web
        button_conference = driver.find_element(By.XPATH, xpath_button_menu)

        # Obtener el menú despegable
        driver.execute_script("arguments[0].click();", button_conference)

        # XPATH de la lista desplegable que contiene las temporadas (sesons)
        xpath_ul = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/'\
                   'div[1]/div/div/div[1]/ul/li[1]'

        # Esperar a que el elemento <ul> se despliegue después de hacer clic en el botón
        ul_conference = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath_ul)))  
        
        # XPATH de la etiqueta <li>
        xpath_li = xpath_ul[:-3] + f'[{choose_option}]' 
        
        # Acceder a la opcione <li> especifica dentro de la etiqueta <ul>
        season_li = ul_conference.find_element(By.XPATH, xpath_li)
        
        # Hacer clic en una opción específica
        driver.execute_script("arguments[0].click();", season_li)

    except Exception as e:
        print(f'{e}')
        raise ('Error en la función "seasons_nba.py.choose_options_menu"...')
# END --------- CHOOSE NBA LEAGUE                                                                                      #
# ==================================================================================================================== #


# ==================================================================================================================== #
# CLICK ON BUTTON                                                                                                      #
# ==================================================================================================================== #
def click_on(driver, xpath_element, time_wait, click_js=False):
    """
    Clic Sobre el elemnto a buscar del XPATH del parámetro obtenido

    Args:
        driver: WebDriver
        xpath_element: XPATH del elemtno a buscar dentro de la página web. :: <Strin>
        time_wait = Tiempo de espera ára ser usado en la función "WebDriverWait()" :: <int>
        click_js = Booleano que indica si usar o no el script de javascript para hacer clic :: <boolean>

    Returns:
        Web Element encontrado

    Raises:
        No

    Examples:
        >>> click_on(driver, xpath_element,time_wait, click_js=False):
        
        >>> click_on(driver, xpath_element, time_wait, click_js=Treu):
    """

    # Buscar el elemento
    element = WebDriverWait(driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath_element)))
    
    # Clic sobre el elemtno encontrado
    if click_js:
        driver.execute_script("arguments[0].click();", element)
    else:
        element.click()

    return element
# END --------- CLICK ON BUTTON                                                                                        #
# ==================================================================================================================== #


# ==================================================================================================================== #
# CLICK ON BUTTON PREVIOUS                                                                                             #
# ==================================================================================================================== #
# XPATH del botón "PREVIOUS"
xpath__button_previous = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div'\
                         '[1]/div[1]/button' 

def click_on_previous(driver, iterations=1): 
    """
    Dar un # de clics sobre el botón PREVIOUS

    Args:
        driver: Conexión con el navegador web :: <WebDriver>
        iterations: Número de clcis sobre el botón PREVIOUS:: <int>

    Returns:
        NO

    Raises:

    Examples:
        >>> click_on_previous(driver, iterations=1)
                → Un clic sobre el botón PREVIOUS

        >>> click_on_previous(driver, iterations=10)
                → 10 clics sobre el botón PREVIOUS
    """  

    # Número de veces seguidas que se dará clic sobre el botón "PREVIOUS"
    for i_iterations in range(iterations):
        # Clic sobre el botón
        click_on(driver, xpath__button_previous, 4, click_js=True)
# END --------- CLICK ON BUTTON PREVIOUS                                                                               #
# ==================================================================================================================== #


# ==================================================================================================================== #
# UPDATE DATA GRAL.                                                                                                    #
# ==================================================================================================================== #   
list_keys = ['total_points', 'q1', 'q2', 'q3', 'q4']                 
def update_geral_stats(list_data_temp, list_info_match, list_index, h_or_a, n_team, name_key):
    """
    Agregar la información general del partido ('total_points', 'q1', 'q2', 'q3', 'q4') en la lista princ. del partido

    Args:
        list_data_temp: Refencia a la lista que contiene toda la data del partido <list>
        list_info_match: Lista con la información general del partido :: <list>
        list_index: Liste de los indicies que contiene la información de cada equipo :: <list>
        h_or_a: Referencia a si es el quipo local o visitante :: <String>
        n_team: Nombre del equipo :: <String>
        name_key: Caracter a adjuntar como clave de diccionario  :: <String>

    Returns:
        No

    Examples:
        >>> update_geral_stats(list_info_match, list_index, flag_home='h')

        >>> update_geral_stats(list_info_match, list_index, flag_home='h')
    """

    list_data_temp.append(f'{h_or_a}')
    list_data_temp.append(n_team)

    for i_data in list_keys:
        list_data_temp.append(f'{name_key}_{i_data}')
        list_data_temp.append(list_info_match[list_index[list_keys.index(i_data)]])   
# END --------- UPDATE DATA GRAL.                                                                                      #
# ==================================================================================================================== #  


# ==================================================================================================================== #
# BOX SCORE OR STATISTICS SECTION                                                                                      #
# ==================================================================================================================== #
def search_box_score_or_statistics(driver, xpath_rx, name_search):
    """
    Asegurar que se buscó y encontró la sección "BOX SCORE" o "STATISTICS"

    Args:
        driver: WebDriver
        xpath_rx: XPATH del elelemtno ha buscar
        name_search: Nombre a verificar del elelemnto ha buscar

    Returns:
        No

    Examples:
        >>> search_box_score_or_statistics(driver, xpath_rx, 'BOX SCORE')

        >>> search_box_score_or_statistics(driver, xpath_rx, 'STATISTICS')
    """

    for i_search in range(3):
        
        # Buscar y dar clic sobre el elemento 
        element = click_on(driver, xpath_rx, 3, click_js=True)
        element_text = element.text

        # Confirmar que el elemento encontrado sea el correcto
        if element_text == name_search:
            break

        time.sleep(1)
# END --------- BOX SCORE OR STATISTICS SECTION                                                                        #
# ==================================================================================================================== #
