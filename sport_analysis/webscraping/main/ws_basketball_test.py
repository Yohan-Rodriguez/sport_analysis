import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from django.db.utils import IntegrityError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .list_css import get_key_value, get_xpath_button_previous, get_div_container_button_season
from webscraping.models import League
from.season import search_change_season, click_on_dropdawn_menu


# Lista de keys que referencian cada variable a buscar en la página web
list_this_keys = ['ft', 'date', 'home', 'away', 'q1_h', 'q2_h', 'q3_h', 
                  'q4_h', 'q1_a', 'q2_a', 'q3_a', 'q4_a', 'total_h', 'total_a']       


# ==================================================================================================================== #
# MSN EXCEPTIONS                                                                                                       #
# ==================================================================================================================== #
def msn_exceptions(type_try, e):
    # Obtener el mensaje de la excepción como una cadena
    mensaje_error = str(e)
    # Imprimir solo el mensaje de error
    print(f"\nError Try ({type_try}):", mensaje_error[:150])
# END --------- MSN EXCEPTIONS                                                                                         #
# ==================================================================================================================== #


# ==================================================================================================================== #
# MAIN                                                                                                                 #
# ==================================================================================================================== #
def test_catch_data_leagues(driver, id_league, name_league, link_league):    

    # ================================================================================================================ #
    # ABRIR NUEVA PESTAÑA                                                                                              #
    # ================================================================================================================ #
    # Abir nueva ventana (tab) con la url de la liga de la actual iteración
    driver.execute_script(f"window.open('{link_league}');")

    # Cambiar el enfoque a la segunda ventana
    # Obtén los identificadores de todas las ventanas abiertas
    windows = driver.window_handles             

    # Cmbiar enfoque
    driver.switch_to.window(windows[-1])    
    # END --------- ABRIR NUEVA PESTAÑA                                                                                #
    # ================================================================================================================ #

    print('\n', '═'*100, f'\n\nLiga: < {name_league} >\n', '═'*100)

    # Usar la función "search_change_season" para buscar y dvi de "Season"            
    div_contain_button = search_change_season(driver)

    # Mensaje a mostrar por consola cada vez que se cambia de season (temporada)
    season_msn = div_contain_button.text
    # season_msn = "22/23" o season_msn = "2023"

    # ================================================================================================================ #
    # VERIFICAR PRIMERA SEASON CARGADA EN LA LIGA. Que no sea la 23/24 o la 2024 (recien iniciada)                     #
    # ================================================================================================================ #
    # "23/24" o "2024" (Sobre está temporada no se trabaja)
    if season_msn[-2:] != '24':
        pass

    else:
        # Buscar la season anterior (2023)
        click_on_dropdawn_menu(driver=driver, div_contain_button=div_contain_button, season=1)
        div_contain_button = search_change_season(driver)
        season_msn = div_contain_button.text

        if season_msn[-2:] != '24':
            pass
        
        else:
            raise Exception('\nNo Season 2023 found...')
    # END --------- VERIFICAR PRIMERA SEASON CARGADA EN LA LIGA. Que no sea la 23/24 o la 2024 (recien iniciada)       #
    # ================================================================================================================ #

    # Integer que indica el conjunto de los XPATH's indicados de cada liga
    pointer_css_s = 0 

    # Indica si se encontró o no el conjuto de XPATH's de "10_MATCHES"
    flag_no_found_css_set = True

    # Indica si se encontró no el XPATH del "button_previous"
    flag_no_found_previous_b = True

    # ================================================================================================================ #
    # ITERAR SOBRE LAS SEASON's                                                                                        #
    # ================================================================================================================ #
    # Iterar sobre 3 "seasons" en cada liga
    for season in range(3):
        try:
            print('\n', '═'*60, f'\n{name_league} → Season: < {season_msn} >\n', '═'*60)
            
            # ======================================================================================================== #
            # OBTNER LOS DATOS DE TODOS LOS PARTIDOS DE LA SEASON ACTUAL                                               #
            # ======================================================================================================== #
            # Cada iteración a continuación carga 10 partidos nuevos por la acción del "button_previous"
            # while True:
            for i in range(2):
                # Por ahora, el siguiente bloque "try-exception" solo se encarga del "button_previous",
                # que está al final de este bucle for que controla el evento clic sobre "button_previous"
                try:
                    # Iterar sobre cada div de partido único
                    # for i_match in range (10, 0, -1):
                    for i_match in range(1, 2, 1):
                        try:
                            # ======================================================================================== #
                            # AUX FUNCTIONS                                                                            #
                            # ======================================================================================== #
                            def search_xpath(this_xpath):
                                this_div = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, this_xpath)))
                                this_div = this_div.text
                                return this_div


                            def get_search_xpath(xpath_temp, key_rx, i_match):
                                # OBTENER "css_selector" 
                                # Buscar string con CSS indicado en el archivo "list_css.py"
                                xpath_i = get_key_value(xpath_temp=xpath_temp, key_rx=key_rx, i_match=i_match)

                                # Buscar elemento dentro de la págiina web con el CSS obtenido 
                                # y obtener el ".text"
                                div_i = search_xpath(xpath_i)

                                return div_i        
                            

                            def search_ft(key_rx, i_match, pointer_css_s):
                                # FOR de búsqueda del conjunto de XPATH's que integra cada partido de la liga
                                for i_xpath_ft in range(5):
                                    try:
                                        ft_text = get_search_xpath(xpath_temp=i_xpath_ft, key_rx=key_rx, i_match=i_match)
                                        
                                        pointer_css_s += i_xpath_ft

                                        # Indicarle al código que no ejecute este fragmetnod de nuevo (for de búsqueda)
                                        # en la actual liga
                                        flag_no_found_css_set = False
                                    
                                        break                                                

                                    except Exception:
                                        if i_xpath_ft >= 4:
                                            raise Exception(f'\nError: XPATH "ft" no encontrado para el partido {i_match}...')
                                        
                                return ft_text, pointer_css_s, flag_no_found_css_set                         
                            # END --------- AUX FUNCTIONS                                                              #
                            # ======================================================================================== #

                            # ======================================================================================== #
                            # DIV 10 MACTHES                                                                           #
                            # ======================================================================================== #
                            if flag_no_found_css_set:
                                # Obtener "XPATH" de la finalización "FT o AET" del partido
                                set_xpaths = search_ft(key_rx='ft', i_match=i_match, pointer_css_s=pointer_css_s)
                                
                                # Desglozar la tupla que retorna la función "search_ft"
                                ft_text, pointer_css_s, flag_no_found_css_set = set_xpaths[0], set_xpaths[1], set_xpaths[2]
                                                                    
                            else:
                                try:
                                    # Extraeer texto del div de "FT"
                                    ft_text = get_search_xpath(xpath_temp=pointer_css_s, key_rx='ft', i_match=i_match)

                                # Si ocurre un error inesperado con el conjunto de XPATH's ya encontrado...
                                except:
                                    try:
                                        # La explicación de las siguiente líneas está en el fragmento anterior de código
                                        set_xpaths = search_ft(key_rx='ft', i_match=i_match, pointer_css_s=pointer_css_s)                                        
                                        ft_text, pointer_css_s, flag_no_found_css_set = set_xpaths[0], set_xpaths[1], set_xpaths[2]

                                    except:
                                        flag_no_found_css_set = True
                                        raise Exception(f'Buscando posible cambio de XPATH_SET en la liga actual en la Season: <{season_msn}> ...')

                            if (ft_text == 'FT') or (ft_text == 'AET'):                   
                                
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
                                
                                if ft_text == 'AET':
                                    over_time = 1

                                dict_data_match['OT'] = over_time

                                # Imprimir por consola el partido sensado
                                #print('\n', dict_data_match)

                            else:
                                print(f'\nPartido en estado: {ft_text}...')

                            # print(dict_data_match)

                            # END --------- DIV 10 MACTHES                                                             #
                            # ======================================================================================== #

                        except Exception as e:
                            # Teóricamente, está "exception" se debe activar únicamente si "ft_text" falla (si no se encuentra) 
                            # Para que se cunpla lo anterior, el mensaje de está "exception" debe estrar predecido por 
                            # raise Exception('\nError: CSS_SELECTOR "ft" no encontrado...')
                            msn_exceptions(type_try='3', e=e)
                            break
                        
                    # ================================================================================================ #
                    # BUTTON "PREVIOUS"                                                                                #
                    # ================================================================================================ #                    
                    if flag_no_found_previous_b:
                    
                        # Obtener lista de CSS_SELECTOR's del "button_previous"
                        xpath_previous = get_xpath_button_previous()

                        for b_previous in xpath_previous:
                            try:
                                # print(f'Buscando el button con XPATH: {b_previous}...')
                                # Buscar y dar clic sobre el botón dentro de la página web
                                button_previous = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, b_previous)))  
                                driver.execute_script("arguments[0].click();", button_previous)

                                flag_no_found_previous_b = False

                                break

                            except Exception:
                                if b_previous == xpath_previous[-1]:
                                    raise Exception(f'\nError al dar clic en "button_previous"...')
                                
                                continue
                            
                    else:
                        try:
                            # print('Dando clic sobre el button con el XPATH ya encontrado: "button_previous"')
                            driver.execute_script("arguments[0].click();", button_previous)

                        except:
                            # Reiniciar Flag
                            flag_no_found_css_set = True
                            raise Exception('No hay Error (Fin de los partidos de la liga actuaL...)')
                    # END --------- BUTTON "PREVIOUS"                                                                  #
                    # ================================================================================================ #

                except Exception as e:
                    msn_exceptions(type_try='2', e=e)
                    # Ir a la siguiente "Season" porque en la actual ya no está disponible "button_previous"
                    break
            # END --------- OBTNER LOS DATOS DE TODOS LOS PARTIDOS DE LA SEASON ACTUAL                                 #
            # ======================================================================================================== #

            # ======================================================================================================== #
            # SELECCIONAR NUEVA SEASON                                                                                 #
            # ======================================================================================================== #                            
            # El CAMBIO de "season" se realiza solo una vez para recopilar datos de 2 "seasons"
            if (season + 1) < 2:
                # Desplegar menú de temporadas y dar clic en una nueva temporada
                click_on_dropdawn_menu(driver=driver, div_contain_button=div_contain_button, season=season+1)

                # Mensaje a mostrar por consola cada vez que se cambia de season (temporada)
                season_msn = div_contain_button.text

            else:
                break
            # END --------- SELECCIONAR NUEVA SEASON                                                                   #
            # ======================================================================================================== #
        
        except Exception as e:
            msn_exceptions(type_try='1', e=e)
            break
    # END --------- ITERAR SOBRE LAS SEASON's                                                                          #
    # ================================================================================================================ #

    # Al temrinar de trabajar en la segunda ventana, se cierra está ventana
    # Cerrar la segunda ventana
    driver.close()
    

    # Cambiar el enfoque de vuelta a la primera ventana
    driver.switch_to.window(windows[0])               
# END --------- MAIN                                                                                                   #
# ==================================================================================================================== #


# ==================================================================================================================== #
# CHROME DRIVER CONNECTION                                                                                             #
# ==================================================================================================================== #
def inicializar_driver():
    options = webdriver.ChromeOptions()
    options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
    driver_path = "drivers/chromedriver.exe"
    driver = webdriver.Chrome(options=options)#, executable_path=driver_path)

    return driver
# END --------- CHROME DRIVER CONNECTION                                                                               #
# ==================================================================================================================== #


# ==================================================================================================================== #
# OBTENER LIGAS DE LA DB Y ENVIARLAS A MAIN                                                                            #
# ==================================================================================================================== #
def test_get_and_set_data_basketaball():
    # Llamada a las funciones
    #if __name__ == "__main__":

    # Obtener todos los registros de la tabla League (id, nombre y link de todas las ligas guardadas)
    data_table_leagues = League.objects.all().order_by('name_league')

    # Inicializar el driver
    driver = inicializar_driver()

    # Abrir navegador en una pastaña en balnco
    driver.maximize_window()
    driver.get('https://www.google.com/')

    count_errors = 0
    # Iterar sobre todos los registros obtenidos
    for registro in data_table_leagues:
        try:            
            # print(f'ID: {registro.id_league}, Nombre: {registro.name_league}, Enlace: {registro.link_league}')
            test_catch_data_leagues(driver, registro.id_league, registro.name_league, registro.link_league)    

        except Exception as e:
            if count_errors >= 500:
                break

            else:
                msn_exceptions(type_try='MAIN', e=e)
                count_errors += 1
                continue

    print('\nFIN...\n')

    # Cerrar navegador
    driver.quit()
# END --------- OBTENER LIGAS DE LA DB Y ENVIARLAS A MAIN                                                              #
# ==================================================================================================================== #



            
            
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


    