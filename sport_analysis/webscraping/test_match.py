import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webscraping.models import League
from random import randint
from django.db.utils import IntegrityError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .list_css import store_css, get_list_keys


def msn_exceptions(type_try, e):
    # Obtener el mensaje de la excepción como una cadena
    mensaje_error = str(e)
    # Imprimir solo el mensaje de error
    print(f"\nError Try ({type_try}):", mensaje_error[:150])

# ==================================================================================================================== #
# BUSCAR CSS_SELECTOR BUTTON                                                                                           #
# ==================================================================================================================== #
def search_button(driver, selector_css_button, msn):
    # Salida de emergencia al siguiente bucle para evitar que sea infinito
    flag_emergency_button = 3

    while True:
        try:
            button = driver.find_element(By.CSS_SELECTOR, selector_css_button)
            break

        except Exception:
            print(f'\nReintentando obtener CSS_SELECTOR de "{msn}".\nIntentos Restante: {flag_emergency_button} s')
            time.sleep(1)

            if flag_emergency_button <= 0:
                button = ''
                break

            flag_emergency_button -= 1

    return button
# END --------- BUSCAR CSS_SELECTOR BUTTON                                                                             #
# ==================================================================================================================== #


def test():
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
    # ITERAR SOBRE LOS PAISES                                                                                          #
    # ================================================================================================================ #         
    # Iterar sobre cada país
    for i_country in range(1, 64, 1):
        try:
            # CSS de cada país
            css_contries = '#__next > main > div > div.sc-hLBbgP.sc-eDvSVe.gjJmZQ.fEHohf.sc-836c558d-1.eDNgWX > div.sc'\
                           '-hLBbgP.bMQfbT.sc-836c558d-2.leSghq > div.sc-hLBbgP.dRtNhU > div > div.sc-hLBbgP.gRCqqZ > '\
                            f'a:nth-child({i_country}) > div > img'  

            # Clic sobre cada país para abirir sus respectivas ligas    
            div_countries = driver.find_element(By.CSS_SELECTOR, css_contries)
            div_countries.click()

            # CSS  del contenedor de las ligas de un país específico
            css_div_link = '#__next > main > div > div.sc-hLBbgP.sc-eDvSVe.gjJmZQ.fEHohf.sc-836c558d-1.eDNgWX > div.sc'\
                           '-hLBbgP.bMQfbT.sc-836c558d-2.leSghq > div.sc-hLBbgP.dRtNhU > div > div.sc-hLBbgP.gRCqqZ > '\
                            'div'
            
            # Captar la información del contenedor de ligas
            div_links_leagues = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_div_link)))

            # ======================================================================================================== #
            # ITERAR SOBRE CADA LINK DEL PAÍS                                                                          #
            # ======================================================================================================== #
            # Buscar todos los elementos <a> dentro del div del país con sus ligas. Cada <a> contine info de una liga.
            a_tags = div_links_leagues.find_elements(By.TAG_NAME, 'a')
            
            # Eliminar el últmio registro. Este contiene la url general del país y no de una liga en particular
            del a_tags[-1]

            # Máximo 2 ligas por cada país (las más importantes)
            for a_tag in a_tags[:2]:        
                try:
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
                    # 5 Intentos para almacenar los datos en la db
                    for i_db_leagues in range(5):
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

                            print('\n\n\n', '═'*80, f'\nNueva Liga:\n\t < {tb_leagues.name_league} >')

                            print(f"\nSe ha guardado la liga < {tb_leagues.name_league} > correctamente...")

                            break
                        
                        except IntegrityError:
                            # Si el id generado ya existe en la tabla, se genera una exception
                            print(f'\nEl id {id_league_ran} ya existe en la base de datos.'
                                  f'\nGenerando un nuevo id...')
                    # END --------- GUARDAR DATOS EN LA TABLA "Leagues"                                                #
                    # ================================================================================================ #

                    # ================================================================================================ #
                    # SELECCIONAR SEASON                                                                               #
                    # ================================================================================================ #
                    # Mensaje a mostrar por consola cada vez que se cambia de season (temporada)
                    season_temp = 1

                    # Iterar sobre 3 "seasons" de cada liga
                    for season in range(1, 4, 1):
                        try:
                            print('\n', '═'*60, f'\n\nSeason de {tb_leagues.name_league}:\n\t# <{season_temp}>')
                            
                            # ======================================================================================== #
                            # OBTNER DATOS DE TODOS LOS PARTIDOS DE LA SEASON                                          #
                            # ======================================================================================== #
                            # Cada iteración a continuación carga 10 partidos nuevos por la acción del "button_previous"
                            for i in range(2):
                                # Por ahora, este "try" solo se encarga del "button_previous"
                                try:
                                    for i_match in range(10, 6, -1):
                                        try:
                                            # ==================================================================================== #
                                            # AUX FUNCTION                                                                         #
                                            # ==================================================================================== #
                                            def search_css(this_css):                                                
                                                this_div = driver.find_element(By.CSS_SELECTOR, this_css).text
                                                return this_div
                                            # END --------- AUX FUNCTION                                                           #
                                            # ==================================================================================== #
                                            
                                            # ==================================================================================== #
                                            # DIV 10 MACTHES                                                                       #
                                            # ==================================================================================== #
                                            # Obtener "css_selector" de la finalización del partido
                                            # Buscar CSS indicado en el archivo "list_css.py"                                            
                                            list_this_keys = ['ft', 'date', 'home', 'away', 'q1_h', 'q2_h', 'q3_h', 'q4_h', 'q1_a', 
                                                              'q2_a', 'q3_a', 'q4_a', 'total_h', 'total_a', ]
                                            
                                            for i_css_ft in ['ft', 'ft_2', 'ft_3']:
                                                css_ft = store_css(i_css_ft, i_match)

                                                try:
                                                    div_ft = search_css(css_ft)
                                                    if i_css_ft == 'ft':
                                                        continue

                                                    elif i_css_ft == 'ft_2':
                                                        list_keys_temp = []
                                                        for i in list_this_keys:
                                                            list_keys_temp.append(i + '_2')
                                                                                                                
                                                        list_this_keys = list_keys_temp
                                                    
                                                    elif i_css_ft == 'ft_3':
                                                        list_keys_temp = []
                                                        for i in list_this_keys:
                                                            list_keys_temp.append(i + '_3')
                                                                                                                
                                                        list_this_keys = list_keys_temp

                                                    break

                                                except:
                                                    print('\nCambiando selectores CSS...')


                                            if (div_ft == 'FT') or (div_ft == 'AET'):
                                                
                                                # Diccionario que contendrá el valor ".text" de las variables buscadas
                                                dict_data_match = {}

                                                # Este for no lleva bloque "try-except "
                                                # porque el error es manejado en la función "get_search_css"
                                                for i_tags_dict in list_this_keys:

                                                    # ============================================================================ #
                                                    # AUX FUNCTION                                                                 #
                                                    # ============================================================================ #
                                                    def get_search_css(key_rx, match_def, str_change):
                                                        try:
                                                            # OBTENER "css_selector" 
                                                            # Buscar string con CSS indicado en el archivo "list_css.py"
                                                            css_i = store_css(key_rx=key_rx, i_match=match_def, str_change=str_change)

                                                            # Buscar elemento dentro de la págiina web con el CSS obtenido 
                                                            # y obtener el ".text"
                                                            div_i = search_css(css_i)

                                                            return div_i 

                                                        except Exception:
                                                            # print('Cambiando parámetro "str_change"...')
                                                            return None
                                                    # END --------- AUX FUNCTION                                                   #
                                                    # ============================================================================ #

                                                    if i_tags_dict in list_this_keys[4:-2]:
                                                        
                                                        # Posibles estructuras del CSS de los cuartos del partido 
                                                        list_str_change_q = ['laFqms', 'cKEAmW']
                                                        for i_str_change in list_str_change_q:
                                                            # Este for no lleva bloque "try-except "
                                                            # porque el error es manejado en la función "get_search_css"

                                                            # Usar la función get_search_css para obtener los datos correctos de la página web    
                                                            div_i = get_search_css(i_tags_dict, i_match, i_str_change)       
                                                            
                                                            if div_i !=  None:
                                                                break                     

                                                    elif i_tags_dict in list_this_keys[-2:]:
                                                        
                                                        # Posibles estructuras del CSS del total de puntos de los equipos
                                                        list_str_change_toal_points = ['hVtlqB', 'UgLMb']
                                                        for i_str_change in list_str_change_toal_points:
                                                            # Este for no lleva bloque "try-except "
                                                            # porque el error es manejado en la función "get_search_css"

                                                            # Usar la función get_search_css para obtener los datos correctos de la página web    
                                                            div_i = get_search_css(i_tags_dict, i_match, i_str_change)
                                                            
                                                            if div_i !=  None:
                                                                break              

                                                    elif i_tags_dict in list_this_keys[:4]:  
                                                        div_i = get_search_css(i_tags_dict, i_match, str_change='')                        

                                                    else:
                                                        continue

                                                    # Agregar nueva "key-value" en el diccionario "dict_data_match"
                                                    dict_data_match[i_tags_dict] = div_i
                                                    # Lista con las tags: ['ft', 'date', 'home', ..., 'q2_a', 'q3_a', 'q4_a', 'total_a']
                                                    # "value" = .text obtenido con la función "search_css()"

                                                # Imprimir por consola el partido sensado
                                                print('\n', dict_data_match)

                                            else:
                                                print('\nPartido no iniciado, no finalizado aún o cancelado...')
                                            # END --------- DIV 10 MACTHES                                                         #
                                            # ==================================================================================== #

                                        except Exception as e:
                                            msn_exceptions(type_try='6', e=e)                                
                                        
                                    # ============================================================================================ #
                                    # BUTTON "PREVIOUS"                                                                            #
                                    # ============================================================================================ #
                                    css_previous = '#__next > main > div > div.fresnel-container.fresnel-greaterThanOrEqua'\
                                                    'l-mdMin > div > div.sc-hLBbgP.sc-eDvSVe.gjJmZQ.fEHohf.sc-836c558d-1.eD'\
                                                    'NgWX > div.sc-hLBbgP.fSpQRs.sc-836c558d-2.kBACDz > div:nth-child(5) > '\
                                                    'div > div.sc-csuSiG.ikkoci > div > div > div.sc-hLBbgP.sYIUR > div > d'\
                                                    'iv.sc-hLBbgP.sc-eDvSVe.fcWLie.ilXvf > div:nth-child(1) > button'                                                    
                                    
                                    
                                    button_previous = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 
                                                                                                                    css_previous)))  
                                    driver.execute_script("arguments[0].click();", button_previous)
                                    # END --------- BUTTON "PREVIOUS"                                                              #
                                    # ============================================================================================ #

                                except Exception as e:
                                    msn_exceptions(type_try='5', e=e)
                                    # Ir a la siguiente "Season" porque en la actual ya no está disponible "button_previous"
                                    break
                            # END --------- OBTNER DATOS DE TODOS LOS PARTIDOS DE LA SEASON                            #
                            # ======================================================================================== #

                            # ======================================================================================== #
                            # SELECCIONAR NUEVA SEASON                                                                 #
                            # ======================================================================================== #                            
                            # El CAMBIO de "season" se realiza solo una vez para recopilar datos de 2 "seasons"
                            if season < 2:
                                list_css_seasons = ['94', '44230', '35348', '63922', '53250', '56494', '1408', '62731', '61498',
                                                    '53250', '53374', '3376', '19960', '64269', '34372', '49241', '36657', '59546',
                                                    '53727', '65026'
                                                   ]
                                #downshift-65026-toggle-button
                            
                                
                                for i_season in list_css_seasons:
                                    try:
                                        # Clic para seleccionar la temporada de la liga
                                        button_season = driver.find_element(By.CSS_SELECTOR, f'#downshift-{i_season}-toggle-button')
                                        button_season.click()

                                        # CSS de la lista desplegable que contiene las temporadas (sesons)
                                        css_ul = f'#downshift-{i_season}-menu'

                                        # Esperar a que el elemento <ul> se despliegue después de hacer clic en el botón
                                        ul_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_ul)))  

                                        # Acceder a las opciones dentro del <ul>
                                        opciones_ul = ul_element.find_elements(By.TAG_NAME, 'li')

                                        # Hacer clic en una opción específica
                                        opciones_ul[season].click()

                                        # Este valor solo se usa para ser mostraddo en el mensaje por consola
                                        season_temp += 1
                                        
                                        break

                                    except Exception as e:
                                        msn_exceptions(type_try='4', e=e)

                            else:
                                break
                            # END --------- SELECCIONAR NUEVA SEASON                                                   #
                            # ======================================================================================== #
                        
                        except Exception as e:
                            msn_exceptions(type_try='3', e=e)
                    # END --------- SELECCIONAR SEASON                                                                 #
                    # ================================================================================================ #

                    # Al temrinar de trabajar en la segunda ventana, se cierra está ventana
                    # Cerrar la segunda ventana
                    driver.close()
                    # END --------- ABRIR NUEVA PESTAÑA                                                                #
                    # ================================================================================================ #

                    # Cambiar el enfoque de vuelta a la primera ventana
                    driver.switch_to.window(windows[0])               

                except Exception as e:
                    msn_exceptions(type_try='2', e=e)

                    # Cerrar la segunda ventana
                    driver.close()

                    # Cambiar el enfoque de vuelta a la primera ventana
                    driver.switch_to.window(windows[0])   

                    continue
            # END --------- ITERAR SOBRE CADA LINK DEL PAÍS                                                            #
            # ======================================================================================================== #

            # Clic para cerrar el contenedor de ligas 
            div_countries.click()

        except Exception as e:
            msn_exceptions(type_try='1', e=e)
    # END --------- ITERAR SOBRE LOS PAISES                                                                            #
    # ================================================================================================================ #

    print('\nFIN...\n')

    # Cerrar navegador
    driver.quit()
    