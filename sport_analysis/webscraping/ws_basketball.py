import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webscraping.models import League
from random import randint
from django.db.utils import IntegrityError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .list_css import store_css, get_list_keys


# ==================================================================================================================== #
# BUSCAR CSS_SELECTOR BUTTON                                                                                           #
# ==================================================================================================================== #
def search_button(driver, selector_css_button):
    # Salida de emergencia al siguiente bucle para evitar que sea infinito
    flag_emergency_button = 3

    while True:
        try:
            button_previous = driver.find_element(By.CSS_SELECTOR, selector_css_button)
            break

        except Exception:
            print(f'\nReintentando obtener CSS_SELECTOR de "Mostrar Más partidos".\nIntentos Restante: {flag_emergency_button} s')
            time.sleep(1)

            if flag_emergency_button <= 0:
                button_previous = ''
                break

            flag_emergency_button -= 1

    return button_previous
# END --------- BUSCAR CSS_SELECTOR BUTTON                                                                             #
# ==================================================================================================================== #


def catch_data_leagues():
    # ================================================================================================================ #
    # CHROME DRIVER CONNECTION                                                                                         #
    # ================================================================================================================ #
    options = webdriver.ChromeOptions()
    options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
    driver_path = "drivers/chromedriver.exe"
    driver = webdriver.Chrome(options=options)#, executable_path=driver_path)
    driver.maximize_window()

        # Abrir la ventana principal
    driver.get('https://www.sofascore.com/basketball')    
    # END --------- CHROME DRIVER CONNECTION                                                                           #
    # ================================================================================================================ #

    # ================================================================================================================ #
    # OBTENER LINK's DE LIGAS                                                                                          #
    # ================================================================================================================ #     
    # Cambiar este for por un while:
    for i in range (1, 3):
        try:
            # CSS de cada país
            css_contries = '#__next > main > div > div.sc-hLBbgP.sc-eDvSVe.gjJmZQ.fEHohf.sc-836c558d-1.eDNgWX > div.sc'\
                           '-hLBbgP.bMQfbT.sc-836c558d-2.leSghq > div.sc-hLBbgP.dRtNhU > div > div.sc-hLBbgP.gRCqqZ > '\
                            f'a:nth-child({i}) > div > img'  

            # Clic sobre cada país para abirir sus respectivas ligas    
            div_countries = driver.find_element(By.CSS_SELECTOR, css_contries)
            div_countries.click()

            # CSS  del contenedor de las ligas de un país específico
            css_div_link = '#__next > main > div > div.sc-hLBbgP.sc-eDvSVe.gjJmZQ.fEHohf.sc-836c558d-1.eDNgWX > div.sc'\
                           '-hLBbgP.bMQfbT.sc-836c558d-2.leSghq > div.sc-hLBbgP.dRtNhU > div > div.sc-hLBbgP.gRCqqZ > '\
                            'div'
            
            # Captar la información del contenedor de ligas
            time_out = 3
            div_links_leagues = WebDriverWait(driver, time_out).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
                                                                                                  css_div_link)))

            # ======================================================================================================== #
            # ITERAR SOBRE CADA LINK DEL PAÍS                                                                          #
            # ======================================================================================================== #
            # Buscar todos los elementos span dentro del div del país con sus ligas. Cada span contine un una liga.
            a_tags = div_links_leagues.find_elements(By.TAG_NAME, 'a')
            
            # Eliminar el últmio registro. Este contiene la url general del país y no de una liga en particular
            del a_tags[-1]

            # Máximo 3 ligas por país (las más importantes)
            max_leagues = 1
            for a_tag in a_tags:        
                try:
                    # Controlador del conteo del número de ligas (son max 3 ligas por país)
                    if max_leagues > 3:
                        break

                    # String con la url de la liga
                    link_league = a_tag.get_attribute('href')

                    # ================================================================================================ #
                    # ABRIR NUEVA PESTAÑA                                                                              #
                    # ================================================================================================ #
                    # Abrir o recargar la página con la url de la liga actual "new_tab_open"
                    # Abrir una segunda ventana o pestaña (puedes hacer clic en un enlace o abrir una nueva URL)                    
                    driver.execute_script(f"window.open('{link_league}');")

                    # Cambiar el enfoque a la segunda ventana
                    # Obtén los identificadores de todas las ventanas abiertas
                    windows = driver.window_handles             

                    # Cmbiar enfoque
                    driver.switch_to.window(windows[-1])

                    # ================================================================================================ #
                    # GUARDAR DATOS EN LA TABLA "leagues"                                                              #
                    # ================================================================================================ #
                    while True:
                        try:
                            # Generar id único aleatoriamente
                            id_league_ran = randint(1000, 10000)

                            # List a partir de la url de la liga.
                            name_league = link_league.split('/')
                            # Ej: new_tab_open = ['https:', '', 'www.sofascore.com', 'tournament', 'basketball', 'argentina', 
                            # 'super-20', '10701']

                            # Extracción del nombre de la url (de la lista "new_tab_open_split").
                            name_league = f"{name_league[5]} - {name_league[6]}"
                            # Ej: new_name_league = "italia - serie-a2"

                            # Crear objeto del modelo League
                            tb_leagues = League(id_league=id_league_ran, name_league=name_league, link_league=link_league)

                            # Guardar los datos en la tabla de la base de datos
                            tb_leagues.save()

                            print(f"\nSe ha guardado la liga < {tb_leagues.name_league} > correctamente.\n")

                            break
                        
                        except IntegrityError:
                            # Si el id generado ya existe en la tabla, se genera una exception
                            print(f'El id {id_league_ran} ya existe en la base de datos.'
                                f'\nGenerando un nuevo id...\n')
                    # END --------- GUARDAR DATOS EN LA TABLA "Leagues"                                                #
                    # ================================================================================================ #

                    # ================================================================================================ #
                    # SELECCIONAR SEASON                                                                               #
                    # ================================================================================================ #
                    # Iterar sobre 3 "seasons" de cada liga
                    for season in range(1, 4, 1):
                        try:
                            # ======================================================================================== #
                            # OBTNER DATOS DE TODOS LOS PARTIDOS DE LA SEASON                                          #
                            # ======================================================================================== #
                            for i_match in range(10, 0, -1):
                                # ============================================================================================================ #
                                # FUNCTION                                                                                                     #
                                # ============================================================================================================ #
                                def search_css(this_css):
                                    this_div = driver.find_element(By.CSS_SELECTOR, this_css).text
                                    return this_div
                                # END --------- FUNCTION                                                                                       #
                                # ============================================================================================================ #
                                
                                # Obtener "css_selector" de la finalización del partido
                                # Buscar CSS indicado en el archivo "list_css.py"
                                css_ft = store_css('ft', i_match)
                                div_ft = search_css(css_ft)

                                if (div_ft == 'FT') or (div_ft == 'AET'):
                                    print('\nIN\n')
                                    
                                    # Diccionario que contendrá el valor ".text" de las variables buscadas
                                    dict_data_match = {}

                                    # Lista con las tags: ['ft', 'date', 'home', 'q1_h', 'q2_h', ..., 'away', 'q1_a', 'q2_a', 'q3_a', 'q4_a', 'total_a']
                                    list_tags = get_list_keys(i_match)

                                    for i_tags_dict in list_tags:                
                                        if i_tags_dict in ['q1_h', 'q2_h', 'q3_h', 'q4_h', 'q1_a', 'q2_a', 'q3_a', 'q4_a']:
                                            
                                            list_str_change_q = ['laFqms', 'cKEAmW']
                                            for i_str_change in list_str_change_q:
                                                try:
                                                    # OBTENER "css_selector" 
                                                    # Buscar string con CSS indicado en el archivo "list_css.py"
                                                    css_i = store_css(key_rx=i_tags_dict, i_match=i_match, str_change=i_str_change)

                                                    # Buscar elemento dentro de la págiina web con el CSS obtenido y obtener el ".text"
                                                    div_i = search_css(css_i)

                                                except Exception:
                                                    print('\nCambiando parámetro "str_change"...')

                                        elif i_tags_dict in ['total_h', 'total_a']:
                                            
                                            list_str_change_toal_points = ['hVtlqB', 'UgLMb']
                                            for i_str_change in list_str_change_toal_points:
                                                try:
                                                    # OBTENER "css_selector" 
                                                    # Buscar string con CSS indicado en el archivo "list_css.py"
                                                    css_i = store_css(key_rx=i_tags_dict, i_match=i_match, str_change=i_str_change)

                                                    # Buscar elemento dentro de la págiina web con el CSS obtenido y obtener el ".text"
                                                    div_i = search_css(css_i)

                                                except Exception:
                                                    print('\nCambiando parámetro "str_change"...')

                                        else:
                                            # OBTENER "css_selector" 
                                            # Buscar string con CSS indicado en el archivo "list_css.py"
                                            css_i = store_css(key_rx=i_tags_dict, i_match=i_match)

                                            # Buscar elemento dentro de la págiina web con el CSS obtenido y obtener el ".text"
                                            div_i = search_css(css_i)


                                        print('\ni_tags_dict: ', i_tags_dict, '\n')
                                        # "div_i" es el resultado del ".text"

                                        # Agregar nueva "key-value" en el diccionario "dict_data_match"
                                        dict_data_match[i_tags_dict] = div_i
                                        # "key" = ['ft', 'date', 'home', 'q1_h', 'q2_h', ..., 'away', 'q1_a', 'q2_a', 'q3_a', 'q4_a', 'total_a']
                                        # "value" = .text obtenido con la función "search_css()"

                                    print(dict_data_match)
                            # END --------- OBTNER DATOS DE TODOS LOS PARTIDOS DE LA SEASON                            #
                            # ======================================================================================== #

                            # ======================================================================================== #
                            # SELECCIONAR NUEVA SEASON                                                                 #
                            # ======================================================================================== #                            
                            # El CAMBIO de "season" se realiza solo una vez para recopilar daots de 2 "seasons"
                            if season < 1:
                                # Clic para seleccionar la temporada de la liga
                                button_season = driver.find_element(By.CSS_SELECTOR, '#downshift-94-toggle-button')
                                button_season.click()

                                # CSS de la lista desplegable que contiene las temporadas (sesons)
                                css_ul = '#downshift-94-menu'

                                # Esperar a que el elemento <ul> se despliegue después de hacer clic en el botón
                                ul_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_ul)))  

                                # Acceder a las opciones dentro del <ul>
                                opciones_ul = ul_element.find_elements(By.TAG_NAME, 'li')

                                # Hacer clic en una opción específica
                                opciones_ul[season].click()

                            else:
                                break
                            # END --------- SELECCIONAR NUEVA SEASON                                                   #
                            # ======================================================================================== #
                        
                        except Exception:
                            continue
                    # END --------- SELECCIONAR SEASON                                                                 #
                    # ================================================================================================ #

                    # Al temrinar de trabajar en la segunda ventana, se cierra está ventana
                    # Cerrar la segunda ventana
                    driver.close()
                    # END --------- ABRIR NUEVA PESTAÑA                                                                #
                    # ================================================================================================ #

                    # Cambiar el enfoque de vuelta a la primera ventana
                    driver.switch_to.window(windows[0])               

                    # Controlador de ligas máximas por país
                    max_leagues += 1

                except Exception:
                    print('\nError Try (5): Exception in button season...')

                    # Cerrar la segunda ventana
                    driver.close()

                    # Cambiar el enfoque de vuelta a la primera ventana
                    driver.switch_to.window(windows[0])   
                    
                    # Controlador de ligas máximas por país
                    max_leagues += 1

                    continue
            # END --------- ITERAR SOBRE CADA LINK DEL PAÍS                                                            #
            # ======================================================================================================== #

            # Clic para cerrar el contenedor de ligas 
            div_countries.click()

        except Exception as e:
            # Obtener el mensaje de la excepción como una cadena
            mensaje_error = str(e)
            # Imprimir solo el mensaje de error
            print("\nError Try (6):", mensaje_error[:150])
            continue
    # END --------- OBTENER LINK's DE LIGAS                                                                            #
    # ================================================================================================================ #

    print('\nFIN...\n')

    # Cerrar navegador
    driver.quit()
    