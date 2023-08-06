import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from django.db.utils import IntegrityError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .list_css import get_key_value, get_xpath_button_previous, get_div_container_button_season
from webscraping.models import League
from .season import search_change_season, click_on_dropdawn_menu, search_button_b
import pandas as pd


# Lista de keys que referencian cada variable a buscar en la página web
list_this_keys = ['ft', 'date', 'home', 'away', 'q1_h', 'q2_h', 'q3_h', 
                  'q4_h', 'q1_a', 'q2_a', 'q3_a', 'q4_a', 'total_h', 'total_a']       


# ==================================================================================================================== #
# MSN EXCEPTIONS                                                                                                       #
# ==================================================================================================================== #
def msn_exceptions(type_try, e, info_match='No data about click and match...'):
    # Obtener el mensaje de la excepción como una cadena
    mensaje_error = str(e)
    # Imprimir solo el mensaje de error
    print(f"\n{info_match}...\nError Try ({type_try}):", mensaje_error[:150])
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
    initial_change_season = 1
    
    if season_msn[-2:] not in ['24']:
        pass

    else:
        # Buscar la season anterior (2023)
        click_on_dropdawn_menu(driver=driver, div_contain_button=div_contain_button, season=1)
        div_contain_button = search_change_season(driver)
        season_msn = div_contain_button.text
        initial_change_season += 1

        if season_msn[-2:] not in ['24']:
            pass
        
        else:
            raise Exception('\nNo Season 2023 found...')
    # END --------- VERIFICAR PRIMERA SEASON CARGADA EN LA LIGA. Que no sea la 23/24 o la 2024 (recien iniciada)       #
    # ================================================================================================================ #

    # ================================================================================================ #
    # BUTTON "PREVIOUS" INITIAL                                                                        #
    # ================================================================================================ #
    # Usar la función "search_button_b" para buscar el "button_previous" dentro la página web
    tuple_button_previous = search_button_b(driver=driver, flag_no_found_previous_b=True, initial=True)
    
    # "button_previous" es el XPATH localizado del "button_previous"
    # "flag_no_found_previous_b" indica si se encontró no el XPATH del "button_previous"
    button_previous, flag_no_found_previous_b, b_previous = tuple_button_previous    
    # END --------- BUTTON "PREVIOUS" INITIAL                                                          #
    # ================================================================================================ #

    # Indica si se encontró o no el conjuto de XPATH's de "10_MATCHES"
    flag_no_found_css_set = True

    # ================================================================================================================ #
    # ITERAR SOBRE LAS SEASON's                                                                                        #
    # ================================================================================================================ #
    # Iterar sobre 3 "seasons" en cada liga
    # Segundos en 12 minutos
    intervalo_iteracion = 720
    
    # Número de sesiones a obtener data
    num_seasons_catch = 3

    for season in range(num_seasons_catch):
        # Registrar el tiempo de inicio de la iteración
        time_start_season = time.time()
        
    #    if 

        list_dict_matches = []
        try:
            # Integer que indica el conjunto de los XPATH's indicados de cada liga
            pointer_css_s = 0 

            print('\n', '═'*60, f'\n{name_league} → Season: < {season_msn} >\n', '═'*60)
            
            # ======================================================================================================== #
            # OBTNER LOS DATOS DE TODOS LOS PARTIDOS DE LA SEASON ACTUAL                                               #
            # ======================================================================================================== #
            i_click_on_previous_b = 0
            # Cada iteración a continuación carga 10 partidos nuevos por la acción del "button_previous"
            # while True:
            for i_click_on_previous_b in range(3):
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

                                try:
                                    # OBTENER "css_selector" 
                                    # Buscar string con CSS indicado en el archivo "list_css.py"
                                    xpath_i = get_key_value(xpath_temp=xpath_temp, key_rx=key_rx, i_match=i_match)

                                    # Buscar elemento dentro de la págiina web con el CSS obtenido 
                                    # y obtener el ".text"

                                except:                                                                      
                                    for i_match_try in range(10, 0, -1):
                                        try:    
                                            xpath_i = get_key_value(xpath_temp=xpath_temp, key_rx=key_rx, i_match=i_match_try)
                                            break

                                        except:
                                            continue

                                div_i = search_xpath(xpath_i)

                                return div_i        
                            

                            def search_ft(key_rx, i_match, pointer_css_s):
                                # FOR de búsqueda del conjunto de XPATH's que integra cada partido de la liga
                                for i_xpath_ft in range(12):
                                    try:
                                        ft_text = get_search_xpath(xpath_temp=i_xpath_ft, key_rx=key_rx, i_match=i_match)
                                        
                                        pointer_css_s += i_xpath_ft

                                        # Indicarle al código que no ejecute este fragmetnod de nuevo (for de búsqueda)
                                        # en la actual liga
                                        flag_no_found_css_set = False
                                    
                                        break                                                

                                    except Exception:
                                        if i_xpath_ft >= 11:
                                            raise Exception('\nError: XPATH "ft" no encontrado para el partido '\
                                                            f'{i_match}...')
                                        
                                        continue
                                        
                                return ft_text, pointer_css_s, flag_no_found_css_set                         
                            # END --------- AUX FUNCTIONS                                                              #
                            # ======================================================================================== #

                            # ======================================================================================== #
                            # DIV 10 MACTHES                                                                           #
                            # ======================================================================================== #
                            if flag_no_found_css_set:
                                # Obtener "XPATH" de la finalización "FT o AET" del partido
                                set_xpaths = search_ft(key_rx='ft', i_match=i_match, pointer_css_s=pointer_css_s)
                                # search_ft(): return ft_text, pointer_css_s, flag_no_found_css_set  
                                
                                # Desglozar la tupla que retorna la función "search_ft"
                                ft_text, pointer_css_s, flag_no_found_css_set = set_xpaths
                                                                    
                            else:
                                try:
                                    # Extraer texto del div de "FT"
                                    ft_text = get_search_xpath(xpath_temp=pointer_css_s, key_rx='ft', i_match=i_match)

                                # Si ocurre un error inesperado con el conjunto de XPATH's ya encontrado...
                                except:
                                    try:
                                        # La explicación de las siguiente líneas está en el fragmento anterior de código
                                        set_xpaths = search_ft(key_rx='ft', i_match=i_match, pointer_css_s=pointer_css_s)                                        
                                        ft_text, pointer_css_s, flag_no_found_css_set = set_xpaths

                                    except:
                                        flag_no_found_css_set = True
                                        raise Exception('Buscando posible cambio de XPATH_SET en la liga actual en la Season: '\
                                                        f'<{season_msn}> ...')

                            # Diccionario que contendrá los valores (".text") de las variables buscadas
                            dict_data_match = {}
                            # print(ft_text)
                            if (ft_text == 'FT') or (ft_text == 'AET'):                                                   

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

                                    # print(div_i)
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
                                raise Exception(f'Partido en estado: {ft_text}...')
                                # print(f'\nClic número: {i_click_on_previous_b}.\nPartido número: {i_match}')
                                # print(f'Partido en estado: {ft_text}...')

                            
                            # print(dict_data_match)
                            # Acceder a elementos específicos del diccionario
                            dict_home = {
                                            'Season': season_msn,
                                            'Click':i_click_on_previous_b,
                                            'Partido': i_match,
                                            'Date': dict_data_match['date'],
                                            'Name_Team': dict_data_match['home'],
                                            'Is_Home': 1,
                                            'Q1': dict_data_match['q1_h'],
                                            'Q2': dict_data_match['q2_h'],
                                            'Q3': dict_data_match['q3_h'],
                                            'Q4': dict_data_match['q4_h'],
                                            'Total': dict_data_match['total_h'],
                                            'OT': dict_data_match['OT'],
                                        }

                            dict_away = {
                                            'Season': season_msn,
                                            'Click':i_click_on_previous_b,
                                            'Partido': i_match,
                                            'Date': dict_data_match['date'],
                                            'Name_Team': dict_data_match['away'],
                                            'Is_Home': 0,
                                            'Q1': dict_data_match['q1_a'],
                                            'Q2': dict_data_match['q2_a'],
                                            'Q3': dict_data_match['q3_a'],
                                            'Q4': dict_data_match['q4_a'],
                                            'Total': dict_data_match['total_a'],
                                            'OT': dict_data_match['OT'],
                                        }
                            
                            list_dict_matches.append(dict_home)
                            list_dict_matches.append(dict_away)

                            # END --------- DIV 10 MACTHES                                                             #
                            # ======================================================================================== #

                        except Exception as e:
                            # Teóricamente, está "exception" se debe activar únicamente si "ft_text" falla (si no se 
                            # encuentra) Para que se cumpla lo anterior, el mensaje de está "exception" debe estrar 
                            # predecido por "raise Exception('\nError: CSS_SELECTOR "ft" no encontrado...')"
                            msn_exceptions(info_match=f'\nClic número: {i_click_on_previous_b}.\nPartido número: {i_match}',
                                           type_try='4', e=e)
                            break
                        
                    # ================================================================================================ #
                    # BUTTON "PREVIOUS"                                                                                #
                    # ================================================================================================ #
                    # Usar la función "search_button_b" para dar clic sobre "button_previous"
                    #  y capturar el return en una variable sin uso
                    useless_tuple_button_previous = search_button_b(flag_no_found_previous_b=flag_no_found_previous_b,
                                                                    driver=driver, button_previous=button_previous, 
                                                                    b_previous=b_previous)
                    # END --------- BUTTON "PREVIOUS"                                                                  #
                    # ================================================================================================ #

                    i_click_on_previous_b += 1

                except Exception as e:
                    msn_exceptions(info_match=f'Clic número: {i_click_on_previous_b}.\nPartido número: {i_match}',
                                   type_try='3', e=e)
                    # Ir a la siguiente "Season" porque en la actual ya no está disponible "button_previous"
                    break
            # END --------- OBTNER LOS DATOS DE TODOS LOS PARTIDOS DE LA SEASON ACTUAL                                 #
            # ======================================================================================================== #
            
            try:
                df_matches = pd.DataFrame(list_dict_matches)
                print('\n')
                print(df_matches)

                # df_matches.to_csv(f'C:\\Users\\ASUS\\Desktop\\leagues\\{name_league} ({season_msn[-2:]}).csv', index=False,
                #                   encoding='latin-1')
            
            except Exception as e:
                print('\n¿Data Frame vacío?')
                msn_exceptions(type_try='2', e=e)
            
            # ======================================================================================================== #
            # SELECCIONAR NUEVA SEASON                                                                                 #
            # ======================================================================================================== #       
            # Desplegar menú de temporadas y dar clic en una nueva temporada
            if season < (num_seasons_catch-1):
                click_on_dropdawn_menu(driver=driver, div_contain_button=div_contain_button, season=season+initial_change_season)

                # Mensaje a mostrar por consola cada vez que se cambia de season (temporada)
                season_msn = div_contain_button.text

                # Usar la función "search_button_b" para buscar el "button_previous" dentro de la nueva season
                tuple_button_previous = search_button_b(driver=driver, flag_no_found_previous_b=True, b_previous=b_previous,
                                                        initial=True)
                
                # "button_previous" es el XPATH localizado del "button_previous"
                # "flag_no_found_previous_b" indica si se encontró no el XPATH del "button_previous"
                button_previous, flag_no_found_previous_b = tuple_button_previous[:-1]

                # Reiniciar Flag porque en este punto ya se han terminado los partidos de la season actual
                flag_no_found_css_set = True
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


    