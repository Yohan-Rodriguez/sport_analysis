import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from django.db.utils import IntegrityError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .list_css import get_key_value, get_xpath_button_previous, get_div_container_button_season
from webscraping.models import League


# Lista de keys que referencian cada variable a buscar en la página web
list_this_keys = ['ft', 'date', 'home', 'away', 'q1_h', 'q2_h', 'q3_h', 'q4_h', 'q1_a', 'q2_a', 'q3_a', 'q4_a', 'total_h', 'total_a']       


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
            button = driver.find_element(By.XPATH, selector_css_button)
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


def test(driver, id_league, name_league, link_league):

    # ================================================================================================================ #
    # ITERAR SOBRE LOS PAISES                                                                                          #
    # ================================================================================================================ #         
    i_country = None

    count_leagues = 0


    # ================================================================================================ #
    # ABRIR NUEVA PESTAÑA                                                                              #
    # ================================================================================================ #
    # Abir nueva ventana (tab) con la url de la liga de la actual iteración
    driver.execute_script(f"window.open('{link_league}');")

    # Cambiar el enfoque a la segunda ventana
    # Obtén los identificadores de todas las ventanas abiertas
    windows = driver.window_handles             

    # Cmbiar enfoque
    driver.switch_to.window(windows[-1])
    
    print('\n', '═'*100, f'\n\nLiga: < {name_league} >\n', '═'*100)

    # ================================================================================================ #
    # SELECCIONAR SEASON                                                                               #
    # ================================================================================================ #
    # Mensaje a mostrar por consola cada vez que se cambia de season (temporada)
    season_temp = 1

    # Iterar sobre 3 "seasons" de cada liga
    for season in range(1, 4, 1):
        try:
            print('\n', '═'*60, f'\n{name_league} → Season: <{season_temp}>\n', '═'*60)
            
            # ======================================================================================== #
            # OBTNER DATOS DE TODOS LOS PARTIDOS DE LA SEASON                                          #
            # ======================================================================================== #
            # Cada iteración a continuación carga 10 partidos nuevos por la acción del "button_previous"
            for i in range(2):
                # Por ahora, el siguiente bloque "try-exception" solo se encarga del "button_previous",
                # que está al final de este bucle for que controla el evento clic sobre "button_previous"
                try:
                    # Iterar sobre cada div de partido único
                    for i_match in range(1, 2, 1):
                        try:
                            # ==================================================================================== #
                            # AUX FUNCTIONS                                                                        #
                            # ==================================================================================== #
                            def search_xpath(this_xpath):                                                
                                this_div = driver.find_element(By.XPATH, this_xpath).text
                                return this_div


                            def get_search_xpath(xpath_temp, key_rx, i_match):
                                # OBTENER "css_selector" 
                                # Buscar string con CSS indicado en el archivo "list_css.py"
                                xpath_i = get_key_value(xpath_temp=xpath_temp, key_rx=key_rx, i_match=i_match)

                                # Buscar elemento dentro de la págiina web con el CSS obtenido 
                                # y obtener el ".text"
                                div_i = search_xpath(xpath_i)

                                return div_i                                 
                            # END --------- AUX FUNCTIONS                                                          #
                            # ==================================================================================== #


                            # ==================================================================================== #
                            # DIV 10 MACTHES                                                                       #
                            # ==================================================================================== #
                            # Integer que indica el conjunto de CSS's indicado de cada liga
                            pointer_css_s = 0 

                            # Obtener "css_selector" de la finalización "FT o AET" del partido
                            for i_xpath_ft in range(3):
                                try:
                                    div_ft = get_search_xpath(xpath_temp=i_xpath_ft, key_rx='ft', i_match=i_match)
                                    
                                    pointer_css_s += i_xpath_ft
                                
                                    break

                                except Exception:
                                    if i_xpath_ft >= 2:
                                        raise Exception(f'\nError: XPATH "ft" no encontrado para el partido {i_match}...')
                                        
                                    continue

                            if (div_ft == 'FT') or (div_ft == 'AET'):                              
                                
                                # Diccionario que contendrá los valores (".text") de las variables buscadas
                                dict_data_match = {}

                                # Iterar sobre la lista de keys del diccionario de los CSS_SELECTOR: ['ft', ..., 'total_a']
                                # Este for no lleva bloque "try-except "
                                # porque el error es manejado en la función "get_search_css"
                                for i_tags_dict in list_this_keys:                                    

                                    # list_this_keys[:4] = ['ft', 'date', 'home', 'away']
                                    if i_tags_dict in list_this_keys[:4]:  
                                        # Usar la función get_search_css para obtener los datos correctos de la página web    
                                        div_i = get_search_xpath(xpath_temp=pointer_css_s, key_rx=i_tags_dict, i_match=i_match)                        
                                    
                                    # list_this_keys[4:-2] = ['q1_h', 'q2_h', 'q3_h', 'q4_h', 'q1_a', 'q2_a', 'q3_a', 'q4_a']
                                    elif i_tags_dict in list_this_keys[4:-2]:                                       
                                        div_i = get_search_xpath(xpath_temp=pointer_css_s, key_rx=i_tags_dict, i_match=i_match)                                                              

                                    # list_this_keys[-2:] = ['total_h', 'total_a']
                                    elif i_tags_dict in list_this_keys[-2:]:
                                        div_i = get_search_xpath(xpath_temp=pointer_css_s, key_rx=i_tags_dict, i_match=i_match)

                                    else:
                                        continue

                                    # Agregar nueva "key-value" en el diccionario "dict_data_match"
                                    dict_data_match[i_tags_dict] = div_i
                                    # Lista con las tags: ['ft', 'date', 'home', ..., 'q2_a', 'q3_a', 'q4_a', 'total_a']
                                    # "value" = .text obtenido con la función "search_css()"

                                # Variable que contiene la información de OverTime en el partido
                                # 0 = False 
                                # 1 = True
                                over_time = 0
                                
                                if div_ft == 'AET':
                                    over_time = 1

                                dict_data_match['OT'] = over_time

                                # Imprimir por consola el partido sensado
                                #print('\n', dict_data_match)

                            else:
                                print('\nPartido no iniciado, no finalizado aún o cancelado...')
                            # END --------- DIV 10 MACTHES                                                         #
                            # ==================================================================================== #

                        except Exception as e:
                            # Teóricamente, está "exception" se debe activar únicamente si "div_ft" falla (si no se encuentra) 
                            # Para que se cunpla lo anterior, el mensaje de está "exception" debe estrar predecido por 
                            # raise Exception('\nError: CSS_SELECTOR "ft" no encontrado...')
                            msn_exceptions(type_try='3', e=e)
                            break
                        
                    # ============================================================================================ #
                    # BUTTON "PREVIOUS"                                                                            #
                    # ============================================================================================ #
                    # Obtener lista de CSS_SELECTOR's del "button_previous"
                    xpath_previous = get_xpath_button_previous()                                                                                          
                    
                    for b_previous in xpath_previous:
                        try:
                            # Buscar y dar clic sobre el botón dentro de la página web
                            button_previous = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, b_previous)))  
                            driver.execute_script("arguments[0].click();", button_previous)

                            break

                        except Exception:
                            if b_previous == xpath_previous[-1]:  
                                raise Exception()
                            
                            continue
                    # END --------- BUTTON "PREVIOUS"                                                              #
                    # ============================================================================================ #

                except Exception as e:
                    msn_exceptions(type_try='2', e=f'\nError al dar clic en "button_previous"...')
                    # Ir a la siguiente "Season" porque en la actual ya no está disponible "button_previous"
                    break
            # END --------- OBTNER DATOS DE TODOS LOS PARTIDOS DE LA SEASON                            #
            # ======================================================================================== #

            # ======================================================================================== #
            # SELECCIONAR NUEVA SEASON                                                                 #
            # ======================================================================================== #                            
            # El CAMBIO de "season" se realiza solo una vez para recopilar datos de 2 "seasons"
            if season < 2:                             

                # Traer la lista de los XPATH del cambio de Season
                list_xpath_div_b = get_div_container_button_season()

                # Iterar sonre la lista de CSS_SELECTOR's de Season's
                for xpath_div_contain_b in list_xpath_div_b:
                    try:
                        # Buscar el xpath dentro de la página web 
                        div_contain_button = driver.find_element(By.XPATH, xpath_div_contain_b) 
                        
                        # Dentro del div principal, encontrar el botón
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
                        button_season.click()
                        
                        # CSS de la lista desplegable que contiene las temporadas (sesons)
                        css_ul = f'#{valor_aria_controls}'
                        # Ejemplo: css_ul = #downshift-1024-menu
                        
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
                        # Si ya no hay más elementos sobre los que iterar, lanzar la siguiente exception
                        if xpath_div_contain_b == list_xpath_div_b[-1]:
                            raise Exception(f'\nERROR: XPATH del cambio de Season no encontrado...\n{e}')

            else:
                break
            # END --------- SELECCIONAR NUEVA SEASON                                                   #
            # ======================================================================================== #
        
        except Exception as e:
            msn_exceptions(type_try='1', e=e)
            break
    # END --------- SELECCIONAR SEASON                                                                 #
    # ================================================================================================ #

    # Al temrinar de trabajar en la segunda ventana, se cierra está ventana
    # Cerrar la segunda ventana
    driver.close()
    

    # Cambiar el enfoque de vuelta a la primera ventana
    driver.switch_to.window(windows[0])               
# END --------- ITERAR SOBRE LOS PAISES                                                                            #
# ================================================================================================================ #



def inicializar_driver():
    # ================================================================================================================ #
    # CHROME DRIVER CONNECTION                                                                                         #
    # ================================================================================================================ #
    options = webdriver.ChromeOptions()
    options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
    driver_path = "drivers/chromedriver.exe"
    driver = webdriver.Chrome(options=options)#, executable_path=driver_path)
    # END --------- CHROME DRIVER CONNECTION                                                                           #
    # ================================================================================================================ #

    return driver


def get_and_set_data_basketaball():
    # Llamada a las funciones
    #if __name__ == "__main__":

    # Obtener todos los registros de la tabla League
    data_table_leagues = League.objects.all().order_by('name_league')

    # Inicializar el driver
    driver = inicializar_driver()

    # Abrir navegador en una pastaña en balnco
    driver.maximize_window()
    driver.get('https://www.google.com/')

    # Iterar sobre todos los registros obtenidos
    for registro in data_table_leagues:
        # print(f'ID: {registro.id_league}, Nombre: {registro.name_league}, Enlace: {registro.link_league}')
        test(driver, registro.id_league, registro.name_league, registro.link_league)
        

    print('\nFIN...\n')

    # Cerrar navegador
    driver.quit()



            
            
#            # END --------- ABRIR NUEVA PESTAÑA                                                                #
#            # ================================================================================================ #      
#
#                    # ================================================================================================ #
#                    # GUARDAR DATOS EN LA TABLA "leagues"                                                              #
#                    # ================================================================================================ #
#                    # 5 Intentos para almacenar los datos en la db
#                    for i_db_leagues in range(5):
#                        try:
#                            # Generar id único aleatoriamente
#                            id_league_ran = randint(1000, 10000)
#
#                            # List a partir de la url de la liga.
#                            name_league = link_league.split('/')
#                            # Ej: new_tab_open = ['https:', '', 'www.sofascore.com', 'tournament', 'basketball', 'argentina', 
#                            # 'super-20', '10701']
#
#                            # Extracción del nombre de la url (de la lista "new_tab_open_split").
#                            name_league = f"{name_league[5]} - {name_league[6]}"
#                            # Ej: new_name_league = "italia - serie-a2"
#
#                            # Crear objeto del modelo League
#                            tb_leagues = League(id_league=id_league_ran, name_league=name_league, link_league=link_league)
#
#                            # Guardar los datos en la tabla de la base de datos
#                            tb_leagues.save()
#
#                            print('\n\n\n', '═'*80, f'\nNueva Liga:\n\t < {tb_leagues.name_league} >')
#
#                            print(f"\nSe ha guardado la liga < {tb_leagues.name_league} > correctamente...")
#
#                            break
#                        
#                        except IntegrityError:
#                            # Si el id generado ya existe en la tabla, se genera una exception
#                            print(f'\nEl id {id_league_ran} ya existe en la base de datos.'
#                                  f'\nGenerando un nuevo id...')
#                    # END --------- GUARDAR DATOS EN LA TABLA "Leagues"                                                #
#                    # ================================================================================================ #
#
#
#                    
#
#        except Exception as e:
#            msn_exceptions(type_try='1', e=e)
#    
#            # END --------- ITERAR SOBRE CADA LINK DEL PAÍS                                                            #
#            # ======================================================================================================== #


    