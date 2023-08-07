import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from django.db.utils import IntegrityError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .list_css import get_key_value
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
    # Sumatoria del tiempo tomado para iterar sobre todas las season de la liga  actual
    time_seasons = 0

    # Timepo máximo para iterar sobre una sola seson (720 segundos = 12 minutos)
    time_max_per_season = 720

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
                    time_seasons += time_end_season
            
            else:
                # Recargar la página
                driver.refresh()

                # Desplegar menú de temporadas y dar clic en una nueva temporada
                if season < (num_seasons_catch-1):
                    # Cambiar season por medio de la función auxiliar "choose_season()"
                    news_values_parameters_season = choose_season(season=season, initial_change_season=initial_change_season,
                                                                  driver=driver, div_contain_button=div_contain_button, 
                                                                  b_previous=b_previous)
                                        
                    # Nuevos calores para las variables que controlan el flujo del código de cada iteración de season
                    season_msn, button_previous, flag_no_found_previous_b, flag_no_found_css_set = news_values_parameters_season

                    # Obtener la suma total actual de tiempo transcurrido para iterar todas las season iteradas hasta aqui
                    time_seasons += time_end_season
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
def yes_test_get_and_set_data_basketaball():
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



# ==================================================================================================================== #
# OBTENER LIGAS DE LA DB Y ENVIARLAS A MAIN                                                                            #
# ==================================================================================================================== #
def test_get_and_set_data_basketaball():
    # Llamada a las funciones
    #if __name__ == "__main__":

    list_info_matches = [{'id_league': 4093, 'name_league': 'australia - big-v', 'link_league': 'https://www.sofascore.com/tournament/basketball/australia/big-v/3084'}, {'id_league': 6635, 'name_league': 'australia - big-v-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/australia/big-v-women/10267'}, {'id_league': 9001, 'name_league': 'australia - nbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/australia/nbl/1524'}, {'id_league': 5588, 'name_league': 'australia - nbl1-central', 'link_league': 'https://www.sofascore.com/tournament/basketball/australia/nbl1-central/16739'}, {'id_league': 8049, 'name_league': 'australia - nbl1-north', 'link_league': 'https://www.sofascore.com/tournament/basketball/australia/nbl1-north/16818'}, {'id_league': 6317, 'name_league': 'australia - nbl1-south', 'link_league': 'https://www.sofascore.com/tournament/basketball/australia/nbl1-south/16776'}, {'id_league': 8383, 'name_league': 'australia - nbl1-west', 'link_league': 'https://www.sofascore.com/tournament/basketball/australia/nbl1-west/16740'}, {'id_league': 4424, 'name_league': 'australia - nbl1-women-central', 'link_league': 'https://www.sofascore.com/tournament/basketball/australia/nbl1-women-central/16741'}, {'id_league': 9110, 'name_league': 'australia - nbl1-women-north', 'link_league': 'https://www.sofascore.com/tournament/basketball/australia/nbl1-women-north/16819'}, {'id_league': 6191, 'name_league': 'australia - nbl1-women-south', 'link_league': 'https://www.sofascore.com/tournament/basketball/australia/nbl1-women-south/16821'}, {'id_league': 8782, 'name_league': 'australia - nbl1-women-west', 'link_league': 'https://www.sofascore.com/tournament/basketball/australia/nbl1-women-west/16742'}, {'id_league': 5214, 'name_league': 'australia - wnbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/australia/wnbl/1506'}, {'id_league': 2408, 'name_league': 'austria - awbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/austria/awbl/300'}, {'id_league': 4655, 'name_league': 'austria - bsl', 'link_league': 'https://www.sofascore.com/tournament/basketball/austria/bsl/297'}, {'id_league': 5051, 'name_league': 'austria - cup', 'link_league': 'https://www.sofascore.com/tournament/basketball/austria/cup/1470'}, {'id_league': 5921, 'name_league': 'belgium - 2nd-division', 'link_league': 'https://www.sofascore.com/tournament/basketball/belgium/2nd-division/1934'}, {'id_league': 6196, 'name_league': 'belgium - belgium-basketball-cup', 'link_league': 'https://www.sofascore.com/tournament/basketball/belgium/belgium-basketball-cup/2331'}, {'id_league': 3733, 'name_league': 'belgium - blb', 'link_league': 'https://www.sofascore.com/tournament/basketball/belgium/blb/1492'}, {'id_league': 1046, 'name_league': 'bolivia - libobasquet', 'link_league': 'https://www.sofascore.com/tournament/basketball/bolivia/libobasquet/13906'}, {'id_league': 3852, 'name_league': 'bosnia-herzegovina - 1st-division', 'link_league': 'https://www.sofascore.com/tournament/basketball/bosnia-herzegovina/1st-division/14306'}, {'id_league': 1364, 'name_league': 'brazil - lbf-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/brazil/lbf-women/19970'}, {'id_league': 8288, 'name_league': 'brazil - nbb', 'link_league': 'https://www.sofascore.com/tournament/basketball/brazil/nbb/1562'}, {'id_league': 2161, 'name_league': 'bulgaria - nbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/bulgaria/nbl/1920'}, {'id_league': 8717, 'name_league': 'canada - nbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/canada/nbl/11561'}, {'id_league': 8040, 'name_league': 'chile - liga-nacional', 'link_league': 'https://www.sofascore.com/tournament/basketball/chile/liga-nacional/9506'}, {'id_league': 6525, 'name_league': 'china - cba', 'link_league': 'https://www.sofascore.com/tournament/basketball/china/cba/1566'}, {'id_league': 4412, 'name_league': 'china - wcba', 'link_league': 'https://www.sofascore.com/tournament/basketball/china/wcba/2339'}, {'id_league': 4242, 'name_league': 'chinese-taipei - p-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/chinese-taipei/p-league/18639'}, {'id_league': 3085, 'name_league': 'croatia - a1-liga-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/croatia/a1-liga-women/580'}, {'id_league': 8822, 'name_league': 'croatia - druga-muska-liga-centar', 'link_league': 'https://www.sofascore.com/tournament/basketball/croatia/druga-muska-liga-centar/16620'}, {'id_league': 1857, 'name_league': 'croatia - druga-muska-liga-istok', 'link_league': 'https://www.sofascore.com/tournament/basketball/croatia/druga-muska-liga-istok/16367'}, {'id_league': 3640, 'name_league': 'croatia - druga-muska-liga-jug', 'link_league': 'https://www.sofascore.com/tournament/basketball/croatia/druga-muska-liga-jug/16359'}, {'id_league': 6171, 'name_league': 'croatia - druga-muska-liga-sjever', 'link_league': 'https://www.sofascore.com/tournament/basketball/croatia/druga-muska-liga-sjever/19773'}, {'id_league': 1667, 'name_league': 'croatia - druga-muska-liga-zapad', 'link_league': 'https://www.sofascore.com/tournament/basketball/croatia/druga-muska-liga-zapad/19834'}, {'id_league': 4700, 'name_league': 'croatia - ht-premijer-liga', 'link_league': 'https://www.sofascore.com/tournament/basketball/croatia/ht-premijer-liga/579'}, {'id_league': 5659, 'name_league': 'croatia - kresimir-cosic-cup', 'link_league': 'https://www.sofascore.com/tournament/basketball/croatia/kresimir-cosic-cup/10189'}, {'id_league': 5354, 'name_league': 'croatia - prva-muska-liga', 'link_league': 'https://www.sofascore.com/tournament/basketball/croatia/prva-muska-liga/16346'}, {'id_league': 7471, 'name_league': 'cyprus - division-a', 'link_league': 'https://www.sofascore.com/tournament/basketball/cyprus/division-a/9557'}, {'id_league': 4363, 'name_league': 'czech-republic - 1-liga', 'link_league': 'https://www.sofascore.com/tournament/basketball/czech-republic/1-liga/1482'}, {'id_league': 1635, 'name_league': 'czech-republic - nbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/czech-republic/nbl/250'}, {'id_league': 2304, 'name_league': 'czech-republic - zbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/czech-republic/zbl/1484'}, {'id_league': 8997, 'name_league': 'denmark - basketligaen', 'link_league': 'https://www.sofascore.com/tournament/basketball/denmark/basketligaen/843'}, {'id_league': 9571, 'name_league': 'dominican-republic - lnb', 'link_league': 'https://www.sofascore.com/tournament/basketball/dominican-republic/lnb/14089'}, {'id_league': 4437, 'name_league': 'england - bbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/england/bbl/230'}, {'id_league': 9016, 'name_league': 'england - bbl-cup', 'link_league': 'https://www.sofascore.com/tournament/basketball/england/bbl-cup/2167'}, {'id_league': 9120, 'name_league': 'estonia - kml', 'link_league': 'https://www.sofascore.com/tournament/basketball/estonia/kml/973'}, {'id_league': 2690, 'name_league': 'finland - korisliiga', 'link_league': 'https://www.sofascore.com/tournament/basketball/finland/korisliiga/226'}, {'id_league': 1034, 'name_league': 'finland - korisliiga-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/finland/korisliiga-women/19929'}, {'id_league': 2023, 'name_league': 'france - coupe-de-france', 'link_league': 'https://www.sofascore.com/tournament/basketball/france/coupe-de-france/1666'}, {'id_league': 3350, 'name_league': 'france - coupe-de-france-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/france/coupe-de-france-women/10167'}, {'id_league': 1406, 'name_league': 'france - lfb-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/france/lfb-women/1854'}, {'id_league': 8876, 'name_league': 'france - pro-a', 'link_league': 'https://www.sofascore.com/tournament/basketball/france/pro-a/156'}, {'id_league': 3444, 'name_league': 'france - pro-b', 'link_league': 'https://www.sofascore.com/tournament/basketball/france/pro-b/1189'}, {'id_league': 9881, 'name_league': 'germany - 1-dbbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/germany/1-dbbl/251'}, {'id_league': 1025, 'name_league': 'germany - bbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/germany/bbl/227'}, {'id_league': 5895, 'name_league': 'germany - bbl-pokal', 'link_league': 'https://www.sofascore.com/tournament/basketball/germany/bbl-pokal/359'}, {'id_league': 8726, 'name_league': 'germany - pro-a', 'link_league': 'https://www.sofascore.com/tournament/basketball/germany/pro-a/1165'}, {'id_league': 5414, 'name_league': 'greece - a1', 'link_league': 'https://www.sofascore.com/tournament/basketball/greece/a1/304'}, {'id_league': 7047, 'name_league': 'greece - a1-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/greece/a1-women/9543'}, {'id_league': 1751, 'name_league': 'greece - elite-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/greece/elite-league/10599'}, {'id_league': 2482, 'name_league': 'greece - greece-cup', 'link_league': 'https://www.sofascore.com/tournament/basketball/greece/greece-cup/608'}, {'id_league': 8582, 'name_league': 'hungary - nb-i', 'link_league': 'https://www.sofascore.com/tournament/basketball/hungary/nb-i/10594'}, {'id_league': 1840, 'name_league': 'hungary - nb-i-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/hungary/nb-i-women/14199'}, {'id_league': 6946, 'name_league': 'iceland - cup', 'link_league': 'https://www.sofascore.com/tournament/basketball/iceland/cup/17281'}, {'id_league': 6816, 'name_league': 'iceland - cup-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/iceland/cup-women/17282'}, {'id_league': 3034, 'name_league': 'iceland - urvalsdeild', 'link_league': 'https://www.sofascore.com/tournament/basketball/iceland/urvalsdeild/9507'}, {'id_league': 7643, 'name_league': 'iceland - urvalsdeild-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/iceland/urvalsdeild-women/9504'}, {'id_league': 9367, 'name_league': 'indonesia - ibl', 'link_league': 'https://www.sofascore.com/tournament/basketball/indonesia/ibl/10155'}, {'id_league': 7988, 'name_league': 'international - aba-liga-2', 'link_league': 'https://www.sofascore.com/tournament/basketball/international/aba-liga-2/11469'}, {'id_league': 2552, 'name_league': 'international - admiralbet-aba-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/international/admiralbet-aba-league/235'}, {'id_league': 1392, 'name_league': 'international - alpe-adria-cup', 'link_league': 'https://www.sofascore.com/tournament/basketball/international/alpe-adria-cup/2156'}, {'id_league': 7440, 'name_league': 'international - champions-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/international/champions-league/9357'}, {'id_league': 6536, 'name_league': 'international - eurocup-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/international/eurocup-women/10260'}, {'id_league': 8544, 'name_league': 'international - euroleague', 'link_league': 'https://www.sofascore.com/tournament/basketball/international/euroleague/138'}, {'id_league': 2693, 'name_league': 'international - euroleague-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/international/euroleague-women/1167'}, {'id_league': 9442, 'name_league': 'international - europe-cup', 'link_league': 'https://www.sofascore.com/tournament/basketball/international/europe-cup/2165'}, {'id_league': 2306, 'name_league': 'iran - super-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/iran/super-league/11511'}, {'id_league': 5727, 'name_league': 'israel - national-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/israel/national-league/11499'}, {'id_league': 1872, 'name_league': 'israel - state-cup', 'link_league': 'https://www.sofascore.com/tournament/basketball/israel/state-cup/14525'}, {'id_league': 5598, 'name_league': 'israel - super-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/israel/super-league/1197'}, {'id_league': 4973, 'name_league': 'italy - serie-a', 'link_league': 'https://www.sofascore.com/tournament/basketball/italy/serie-a/262'}, {'id_league': 5752, 'name_league': 'italy - serie-a1-femminile', 'link_league': 'https://www.sofascore.com/tournament/basketball/italy/serie-a1-femminile/556'}, {'id_league': 6091, 'name_league': 'italy - serie-a2', 'link_league': 'https://www.sofascore.com/tournament/basketball/italy/serie-a2/1520'}, {'id_league': 6544, 'name_league': 'italy - serie-b', 'link_league': 'https://www.sofascore.com/tournament/basketball/italy/serie-b/14251'}, {'id_league': 2349, 'name_league': 'japan - b2league', 'link_league': 'https://www.sofascore.com/tournament/basketball/japan/b2league/1516'}, {'id_league': 5658, 'name_league': 'japan - bleague', 'link_league': 'https://www.sofascore.com/tournament/basketball/japan/bleague/1502'}, {'id_league': 9661, 'name_league': 'japan - w-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/japan/w-league/19521'}, {'id_league': 8254, 'name_league': 'kosovo - liga-e-dyte', 'link_league': 'https://www.sofascore.com/tournament/basketball/kosovo/liga-e-dyte/16781'}, {'id_league': 4468, 'name_league': 'kosovo - liga-e-pare', 'link_league': 'https://www.sofascore.com/tournament/basketball/kosovo/liga-e-pare/16734'}, {'id_league': 2338, 'name_league': 'kosovo - princ-caffe-superliga', 'link_league': 'https://www.sofascore.com/tournament/basketball/kosovo/princ-caffe-superliga/16731'}, {'id_league': 8446, 'name_league': 'latvia - lbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/latvia/lbl/982'}, {'id_league': 5171, 'name_league': 'lebanon - first-division', 'link_league': 'https://www.sofascore.com/tournament/basketball/lebanon/first-division/14250'}, {'id_league': 9500, 'name_league': 'lithuania - king-mindaugas-cup', 'link_league': 'https://www.sofascore.com/tournament/basketball/lithuania/king-mindaugas-cup/11012'}, {'id_league': 8325, 'name_league': 'lithuania - lkl', 'link_league': 'https://www.sofascore.com/tournament/basketball/lithuania/lkl/975'}, {'id_league': 8153, 'name_league': 'lithuania - nkl', 'link_league': 'https://www.sofascore.com/tournament/basketball/lithuania/nkl/11432'}, {'id_league': 6378, 'name_league': 'mexico - lnbp', 'link_league': 'https://www.sofascore.com/tournament/basketball/mexico/lnbp/1472'}, {'id_league': 9477, 'name_league': 'mexico - lnbp-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/mexico/lnbp-women/20467'}, {'id_league': 9070, 'name_league': 'netherlands - dbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/netherlands/dbl/1504'}, {'id_league': 6671, 'name_league': 'new-zealand - nbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/new-zealand/nbl/13476'}, {'id_league': 7929, 'name_league': 'norway - blno', 'link_league': 'https://www.sofascore.com/tournament/basketball/norway/blno/11470'}, {'id_league': 9503, 'name_league': 'poland - 1-liga', 'link_league': 'https://www.sofascore.com/tournament/basketball/poland/1-liga/11467'}, {'id_league': 2242, 'name_league': 'poland - ebl', 'link_league': 'https://www.sofascore.com/tournament/basketball/poland/ebl/263'}, {'id_league': 5486, 'name_league': 'poland - plkk', 'link_league': 'https://www.sofascore.com/tournament/basketball/poland/plkk/1916'}, {'id_league': 7649, 'name_league': 'portugal - lpb', 'link_league': 'https://www.sofascore.com/tournament/basketball/portugal/lpb/1926'}, {'id_league': 3611, 'name_league': 'portugal - super-cup', 'link_league': 'https://www.sofascore.com/tournament/basketball/portugal/super-cup/9501'}, {'id_league': 3702, 'name_league': 'puerto-rico - bsn', 'link_league': 'https://www.sofascore.com/tournament/basketball/puerto-rico/bsn/17374'}, {'id_league': 1679, 'name_league': 'romania - lnb-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/romania/lnb-women/19359'}, {'id_league': 6035, 'name_league': 'romania - lnbm-mozzart', 'link_league': 'https://www.sofascore.com/tournament/basketball/romania/lnbm-mozzart/1948'}, {'id_league': 4748, 'name_league': 'russia - premier-league-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/russia/premier-league-women/1201'}, {'id_league': 2560, 'name_league': 'russia - vtb-united-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/russia/vtb-united-league/1438'}, {'id_league': 2046, 'name_league': 'saudi-arabia - premier-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/saudi-arabia/premier-league/19433'}, {'id_league': 5032, 'name_league': 'serbia - admiralbet-kls', 'link_league': 'https://www.sofascore.com/tournament/basketball/serbia/admiralbet-kls/754'}, {'id_league': 8015, 'name_league': 'serbia - prva-rl-istok', 'link_league': 'https://www.sofascore.com/tournament/basketball/serbia/prva-rl-istok/19295'}, {'id_league': 5592, 'name_league': 'slovakia - nike-extraliga-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/slovakia/nike-extraliga-women/1412'}, {'id_league': 9436, 'name_league': 'slovakia - nike-sbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/slovakia/nike-sbl/1410'}, {'id_league': 7510, 'name_league': 'slovenia - cup', 'link_league': 'https://www.sofascore.com/tournament/basketball/slovenia/cup/3074'}, {'id_league': 4785, 'name_league': 'slovenia - liga-novakbm', 'link_league': 'https://www.sofascore.com/tournament/basketball/slovenia/liga-novakbm/745'}, {'id_league': 1048, 'name_league': 'south-korea - kbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/south-korea/kbl/1540'}, {'id_league': 3395, 'name_league': 'south-korea - wkbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/south-korea/wkbl/2334'}, {'id_league': 9362, 'name_league': 'spain - leb-oro', 'link_league': 'https://www.sofascore.com/tournament/basketball/spain/leb-oro/1514'}, {'id_league': 6359, 'name_league': 'spain - liga-acb', 'link_league': 'https://www.sofascore.com/tournament/basketball/spain/liga-acb/264'}, {'id_league': 5062, 'name_league': 'spain - liga-femenina', 'link_league': 'https://www.sofascore.com/tournament/basketball/spain/liga-femenina/1538'}, {'id_league': 7366, 'name_league': 'sweden - sbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/sweden/sbl/277'}, {'id_league': 1721, 'name_league': 'sweden - sbl-women', 'link_league': 'https://www.sofascore.com/tournament/basketball/sweden/sbl-women/14195'}, {'id_league': 9343, 'name_league': 'switzerland - lna', 'link_league': 'https://www.sofascore.com/tournament/basketball/switzerland/lna/1938'}, {'id_league': 6234, 'name_league': 'thailand - tbl', 'link_league': 'https://www.sofascore.com/tournament/basketball/thailand/tbl/13683'}, {'id_league': 1321, 'name_league': 'tunisia - national-a-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/tunisia/national-a-league/14574'}, {'id_league': 8709, 'name_league': 'turkey - kbsl', 'link_league': 'https://www.sofascore.com/tournament/basketball/turkey/kbsl/1532'}, {'id_league': 7190, 'name_league': 'turkey - tb2l', 'link_league': 'https://www.sofascore.com/tournament/basketball/turkey/tb2l/19844'}, {'id_league': 2518, 'name_league': 'turkey - tbsl', 'link_league': 'https://www.sofascore.com/tournament/basketball/turkey/tbsl/519'}, {'id_league': 5840, 'name_league': 'ukraine - fbu-superleague', 'link_league': 'https://www.sofascore.com/tournament/basketball/ukraine/fbu-superleague/2162'}, {'id_league': 9168, 'name_league': 'uruguay - el-metro', 'link_league': 'https://www.sofascore.com/tournament/basketball/uruguay/el-metro/13647'}, {'id_league': 2255, 'name_league': 'uruguay - lub', 'link_league': 'https://www.sofascore.com/tournament/basketball/uruguay/lub/10587'}, {'id_league': 9379, 'name_league': 'usa - nba-g-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/usa/nba-g-league/1580'}, {'id_league': 9739, 'name_league': 'usa - nba-preseason', 'link_league': 'https://www.sofascore.com/tournament/basketball/usa/nba-preseason/2329'}, {'id_league': 8273, 'name_league': 'usa - nba-summer-league', 'link_league': 'https://www.sofascore.com/tournament/basketball/usa/nba-summer-league/10415'}, {'id_league': 5743, 'name_league': 'usa - wnba', 'link_league': 'https://www.sofascore.com/tournament/basketball/usa/wnba/486'}, {'id_league': 8286, 'name_league': 'venezuela - superliga', 'link_league': 'https://www.sofascore.com/tournament/basketball/venezuela/superliga/16764'}]

    # Inicializar el driver
    driver = inicializar_driver()

    # Abrir navegador en una pastaña en balnco
    driver.maximize_window()
    driver.get('https://www.google.com/')

    count_errors = 0
    # Iterar sobre todos los registros obtenidos
    for registro in list_info_matches:

        try:            
            # print(f'ID: {registro.id_league}, Nombre: {registro.name_league}, Enlace: {registro.link_league}')
            test_catch_data_leagues(driver, registro['id_league'], registro['name_league'], registro['link_league'])

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


    