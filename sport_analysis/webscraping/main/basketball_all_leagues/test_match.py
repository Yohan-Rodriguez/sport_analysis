import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from django.db.utils import IntegrityError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .list_css import get_key_value, get_xpath_button_previous, get_div_container_button_season
from webscraping.models import League
from webscraping.main.season import search_change_season, click_on_dropdawn_menu, search_button_b
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



def test():
    # ================================================================================================================ #
    # CHROME DRIVER CONNECTION                                                                                         #
    # ================================================================================================================ #
    options = webdriver.ChromeOptions()
    options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
    driver_path = "drivers/chromedriver.exe"
    driver = webdriver.Chrome(options=options)#, executable_path=driver_path)

    name_league = 'https://www.sofascore.com/tournament/basketball/usa/nba/132'
    
    driver.maximize_window()
    driver.get(name_league)
    # List a partir de la url de la liga.
    # END --------- CHROME DRIVER CONNECTION                                                                           #
    # ================================================================================================================ #
    
    list_name_league = name_league.split('/')
    # Ej: new_tab_open = ['https:', '', 'www.sofascore.com', 'tournament', 'basketball', 'argentina', 
    # 'super-20', '10701']
    
    # Extracción del nombre de la url (de la lista "list_name_league").
    name_league = f"{list_name_league[5]} - {list_name_league[6]}"
    # Ej: new_name_league = "italia - serie-a2"

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
    
    if season_msn[-2:] not in ['24', '23']:
        pass

    else:
        # Buscar la season anterior (2023)
        click_on_dropdawn_menu(driver=driver, div_contain_button=div_contain_button, season=1)
        div_contain_button = search_change_season(driver)
        season_msn = div_contain_button.text
        initial_change_season += 1

        if season_msn[-2:] not in ['24', '23']:
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
    # Sumatoria del tiempo tomado para iterar sobre todas las season de la liga  actual
    time_seasons = 0

    # Timepo máximo para iterar sobre una sola seson (720 segundos = 12 minutos)
    time_max_per_season = 720

    # Tiempo máximo acumulado en cada div_10_machets
    time_max_per_div_10_matches = 1650

    # Número de sesiones a obtener data
    num_seasons_catch = 3

    for season in range(num_seasons_catch):
        # Registrar el tiempo de inicio de la iteración
        time_start_season = time.time()

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
            # for i_click_on_previous_b in range(3):
            while True:
                # Por ahora, el siguiente bloque "try-exception" solo se encarga del "button_previous",
                # que está al final de este bucle for que controla el evento clic sobre "button_previous"
                try:
                    # Iterar sobre cada div de partido único
                    # for i_match in range (10, 0, -1):
                    for i_match in range(1, 11, 1):
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
                                    for i_match_try in range(1, 11, 1):
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

                    # Registrar el tiempo final de la iteración sobre la actual "div_10_matches"     
                    time_end_div_10_matches = time.time()

                    # Timepo total tomado para iterar sobre cada div_10_matches
                    total_time_div_10_matches = time_end_div_10_matches - time_start_season
                    
                    # Si el tiempo usado para iterar sobre la actual season no ha superado el tiempo maximo destinado,
                    # cambiar de season
                    # print(f'\nTiempo div_10_matches: {total_time_div_10_matches}')
                    if total_time_div_10_matches > time_max_per_div_10_matches:
                        break 

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

                df_matches.to_csv(f'C:\\Users\\ASUS\\Desktop\\leagues\\{name_league} ({season_msn[-2:]}).csv', index=False,
                                  encoding='latin-1')
            
            except Exception as e:
                print('\n¿Data Frame vacío?')
                msn_exceptions(type_try='2', e=e)
            
            # ======================================================================================================== #
            # SELECCIONAR NUEVA SEASON                                                                                 #
            # ======================================================================================================== #
            def choose_season(driver, div_contain_button, season, initial_change_season, b_previous):

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

                return season_msn, button_previous, flag_no_found_previous_b, flag_no_found_css_set


            
            # Registrar el tiempo final de la iteración sobre la season actual     
            time_end_season = time.time()

            # Timepo total tomado para iterar sobre la actual season
            total_time_season = time_end_season - time_start_season
            
            # Si el tiempo usado para iterar sobre la actual season no ha superado el tiempo maximo destinado,
            # cambiar de season
            if (total_time_season) < (time_max_per_season * (season+1)):
                # Desplegar menú de temporadas y dar clic en una nueva temporada
                if season < (num_seasons_catch-1):
                    # Cambiar season por medio de la función auxiliar "choose_season()"
                    news_values_parameters_season = choose_season(season=season, initial_change_season=initial_change_season,
                                                                  driver=driver, div_contain_button=div_contain_button, 
                                                                  b_previous=b_previous)
                                        
                    # Nuevos calores para las variables que controlan el flujo del código de cada iteración de season
                    season_msn, button_previous, flag_no_found_previous_b, flag_no_found_css_set = news_values_parameters_season

                    # Obtener la suma total actual de tiempo transcurrido para iterar todas las season iteradas hasta aqui
                    time_seasons += total_time_season
            
            else:
                # Recargar la página
                driver.refresh()

                # ======================================================================================================== #
                # BUSCAR DE NUEVO "DIV_SEASON" Y "BUTTON_PREVIOUS"                                                         #
                # ======================================================================================================== #
                # Usar la función "search_change_season" para buscar y dvi de "Season"            
                div_contain_button = search_change_season(driver)

                # Usar la función "search_button_b" para buscar el "button_previous" dentro la página web
                tuple_button_previous = search_button_b(driver=driver, flag_no_found_previous_b=True, initial=True)
                
                # "button_previous" es el XPATH localizado del "button_previous"
                # "flag_no_found_previous_b" indica si se encontró no el XPATH del "button_previous"
                button_previous, flag_no_found_previous_b, b_previous = tuple_button_previous
                # END --------- BUSCAR DE NUEVO "DIV_SEASON" Y "BUTTON_PREVIOUS"                                           #
                # ======================================================================================================== #          

                # Desplegar menú de temporadas y dar clic en una nueva temporada
                if season < (num_seasons_catch-1):
                    # Cambiar season por medio de la función auxiliar "choose_season()"
                    news_values_parameters_season = choose_season(season=season, initial_change_season=initial_change_season,
                                                                  driver=driver, div_contain_button=div_contain_button, 
                                                                  b_previous=b_previous)
                                        
                    # Nuevos calores para las variables que controlan el flujo del código de cada iteración de season
                    season_msn, button_previous, flag_no_found_previous_b, flag_no_found_css_set = news_values_parameters_season

                    # Obtener la suma total actual de tiempo transcurrido para iterar todas las season iteradas hasta aqui
                    time_seasons += total_time_season

            print(f'\Tiempo total usado en la liga actual: {time_seasons:.2f} segundos...')
            # END --------- SELECCIONAR NUEVA SEASON                                                                   #
            # ======================================================================================================== #          
        
        except Exception as e:
            msn_exceptions(type_try='1', e=e)
            break
    # END --------- ITERAR SOBRE LAS SEASON's                                                                          #
    # ================================================================================================================ #

    # Cerrar el navegador
    driver.quit()      

    print('\nFIN...\n')         
# END --------- ITERAR SOBRE LOS PAISES                                                                            #
# ================================================================================================================ #
