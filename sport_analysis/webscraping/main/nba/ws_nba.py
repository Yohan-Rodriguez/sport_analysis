import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .aux_functions import choose_options_menu, click_on, click_on_previous, search_box_score_or_statistics, \
                            update_geral_stats
from .statistics_extraction import get_statistics_match
from .template_info_matches import TemplateInfoMatches as tim



def storage_players(driver, name_team):
    pass
    # # Buscar sección de "MATCHES"
    # xpath_matches = '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[1]'
    # matches = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_matches)))
    # matches.click()


    # # Buscar sección de "list_players" y dar clic sobre él
    # xpath_list_players = '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[2]/label[2]/div/span'    
    # list_view_players = driver.find_element(By.XPATH, xpath_list_players)
    # driver.execute_script("arguments[0].click();", list_view_players)

    # i_player = 1
    # while True:
    #     try:
    #         xpath_name_player =  '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[3]/table/'\
    #                             f'tr[{i_player}]/td[1]/a/div/span' 
            
    #         xpath_position_player =  '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[3]/ta'\
    #                                 f'ble/tr[{i_player}]/td[2]/div/span'
            
    #         xpath_age_player =  '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[3]/table/t'\
    #                            f'r[{i_player}]/td[3]/div'
            
    #         name_player = driver.find_element(By.XPATH, xpath_name_player).text
    #         position_player = driver.find_element(By.XPATH, xpath_position_player).text
    #         age_player = driver.find_element(By.XPATH, xpath_age_player).text                       


    #         set_info_players_in_dict_team(name_team, dict_info_player, key_dict='Players')


    #         i_player += 1

    #     except Exception as e:
    #         dict_teams = get_dict_teams()
    #         print(dict_teams)
    #         break
    # END --------- GET INFO PLAYERS TEAM                                                                              #
    # ================================================================================================================ #

    # ================================================================================================================ #
    # GET TOP PLAYERS TEAM                                                                                             #
    # ================================================================================================================ #
    # Buscar sección de "list_top_players" y dar clic sobre él
    xpath_list_top_players = '//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div'    
    list_top_players = driver.find_element(By.XPATH, xpath_list_top_players)
    list_top_players.click()

    # ================================================================================================================ #
    # CHOOSE NBA LEAGUE IN TOP PLAYERS                                                                                 #
    # ================================================================================================================ #
    choose_options_menu(driver=driver, num_toggle='0', choose_option=1)
    # END --------- CHOOSE NBA LEAGUE IN TOP PLAYERS                                                                   #
    # ================================================================================================================ #

    # END --------- GET TOP PLAYERS TEAM                                                                               #
    # ================================================================================================================ #


    # ================================================================================================================ #
    # GET ALL MATCHES                                                                                                  #
    # ================================================================================================================ #


    # END --------- GET GET ALL MATCHES                                                                                #
    # ================================================================================================================ #



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
# SCRAPING WEB                                                                                                         #
# ==================================================================================================================== #
# Lista para ser iterada por un for especifico
list_keys_tp = ['name_player', 'position', 'points', 'rebounds', 'assists']
def open_and_scraping_web(driver, count_click_on_previous_tx, current_season):
    """
    Abrir el navegador web y realizar el respectivo scraping sobre los datos indicados a través del código

    Args:
        driver: Conexión con el navegador web :: <WebDriver>
        count_click_on_previous_tx: Número de clics dados sobre el botón PREVIOUS (si los hay) :: <int>
        current_season: Sesión actual iterada :: <String>

    Returns:
        flag_no_change_season: Indica si se debe cambiar de sesión :: <boolean>
        count_click_on_previous: Devuelve el núemro de clics dados sobre el botón PREVIOUS durante 
                                 la ejecución de esta función :: <int>

    Raises:

    Examples:
        >>> open_and_scraping_web(driver=driver, count_click_on_previous_tx=10, current_season='22/23')

        >>> open_and_scraping_web(driver=driver, count_click_on_previous_tx=0, current_season='20/21')
    """

    # Instancia de la clase "TemplateInfoMatches()"
    obj_data_matches = tim()

    # Setear valor de la sesión actual de la instancia de clase creada
    obj_data_matches.current_season = current_season

    # Bandera para recargar la página cada 23 minutos
    time_now = datetime.datetime.now()
    time_end = datetime.datetime.now()
    diff_time = (time_end - time_now).seconds

    # Conteo de click preivos sobre "PREVIOUS"
    count_click_on_previous = count_click_on_previous_tx

    # ================================================================================================================ #
    # BUTTON PREVIOUS INITIAL                                                                                          #
    # ================================================================================================================ #
    if count_click_on_previous > 0:
        # Número de clics sobre "PREVIOUS" dados hasta el momento, durante la ejecución del código
        click_on_previous(driver=driver, iterations=count_click_on_previous)
    # END --------- BUTTON PREVIOUS INITIAL                                                                            #
    # ================================================================================================================ # 
    
    # ================================================================================================================ #
    # ACCES TO MATCHES AND PREVIOUS BUTTON                                                                             #
    # ================================================================================================================ #    
    # Bandera que cambia si ya no está disponible el botón "PREVIOUS" 
    flag_no_change_season = False

    # Tiempo (en segundos) máximo de duración de cada scraping de data
    mum_minutos = 23
    min_to_sec = mum_minutos * 60

    # Extraer data mientras hallan aún partidos o el tiempo trasncurrido sea meanor a "mum_minutos" minuos
    while (not flag_no_change_season) and (diff_time < min_to_sec):
        
        # div principal que contiene como máximo 10 partidos
        xpath_div_main_10_matches = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div'\
                                    '[1]/div/div[2]'
        div_main_10_matches = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, 
                                                                                            xpath_div_main_10_matches)))

        # # Encontrar todos los elementos div secundarios (# de partidos dentro del div princ.) dentro del div principal
        # divs_secundarios = div_main_10_matches.find_elements(By.TAG_NAME, "div")

        # # Obtener el número total de divs secundarios
        # nume_divs_scundarios = len(divs_secundarios)
        # print('\nlen(divs_secundarios)', len(divs_secundarios), sep='\n')

        # ============================================================================================================ #
        # ACCESS SEASON'S MATCHES X 10                                                                                 #
        # ============================================================================================================ #
        # Acceder a cada uno de los X partidos cargados en el div principal que contien los partidos
        for i_matches in range(1, 11):

            # Lista de data a adjuntar posteriormente al diccionario del match
            list_data_temp = []

            # xpath de cada partido dentro de la etiqueta <div> que contiene los 10 partidos (como máximo)
            xpath_match_x = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/'\
                           f'div[2]/div[{i_matches}]/a'

            try:
                # Clic sobre cada partido
                # if para el primer partido
                if i_matches == 1:
                    element_match_x = click_on(driver, xpath_match_x, 5)
                # else para los otros 9 (como máximo) partidos
                else:
                    element_match_x = click_on(driver, xpath_match_x, 5, True)
            
            except:
                print('\nActivated EXCEPTIONE: match no found...')
                # Salir del for que controla el acceso a los partiodos
                break

            try:
                print('\n# Cliks:', count_click_on_previous, '- # del match:', i_matches)
                                
                # Crear la lista con la información base del partido
                list_info_match = element_match_x.text.splitlines()

                # Si el partido fue pospuesto, continuar con el siguiente partido de la lista
                if list_info_match[1] == 'Postponed':
                    print('\nMatch Postponed')
                    continue                
                else:                
                    # Eliminar la posición "FT"
                    del list_info_match[1]

                # Longitud de la lista base
                len_list_info_match = len(list_info_match) 

                # Si el partido no tuvo overtime, la lista tendrá 13 elementos tipo string
                if len_list_info_match == 13:
                    list_data_temp.append('is_overtime')
                    list_data_temp.append(0)

                # Si el partido si tuvo overtime, la lista tendrá 15 elementos tipo string
                elif len_list_info_match == 15:                    
                    list_data_temp.append('is_overtime')
                    list_data_temp.append(1)

                    # Eliminar los elementos que referencian los 2 puntajes del overtime
                    del list_info_match[12]
                    del list_info_match[7]

                # Extraer nombre del equipo local y visitante
                n_home = list_info_match[1]
                n_away = list_info_match[2]

                # Lista que contiene los nombres de los equipos del actual partido
                list_names_teams = [n_home, n_away]

                # for de 2 iteraciones (local y visitante)
                for i_team in list_names_teams:
                    # Si el equipo no existe en el diccionario
                    if i_team not in obj_data_matches.dict_db_nba['teams']:
                        # Adicionar los nombres de los equipos local y visitante
                        obj_data_matches.dict_db_nba['teams'].append(n_home)

                        if n_away not in obj_data_matches.dict_db_nba['teams']:
                            obj_data_matches.dict_db_nba['teams'].append(n_away)                                     

                    # Si la información es del quipo local
                    if i_team == n_home:
                        update_geral_stats(list_data_temp, list_info_match, [-2, 3, 4, 5, 6], 'n_home', n_home, 'h')                        

                    # Si la información es del quipo visitante
                    else:
                        update_geral_stats(list_data_temp, list_info_match, [-1, 7, 8, 9, 10], 'n_away', n_away, 'a')                        

                # Agregar fecha de partido actual
                list_data_temp.append('date_match')
                list_data_temp.append(f'{list_info_match[0]}')                

            except:
                print('Activated EXCEPTIONE: No se puede acceder al método ".text" del elemento del partido "X"')

            # ======================================================================================================== #
            # ACCESS TO TOP MATCH'S PLAYERS                                                                            #
            # ======================================================================================================== #
            name_search = 'Box score'
            xpath_box_score_x = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/'\
                                'div/div[1]/div/div/div[3]/div[1]/div/div/div/h2[2]/a'
            search_box_score_or_statistics(driver, xpath_box_score_x, name_search)

            # Extraer información de los jugadores top de cada equipo en el equipo local y visitante "range(2)"
            for i_bets_players in range(2):

                # Extraer la información de los 3 mejores jugadores de cada equipo
                for i_3_bs in range(1, 4):
                    # Los 2 XPATH de la información del jugador
                    xpath_name_position = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/d'\
                                          'iv/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div[3]/div/div/div[1]/di'\
                                         f'v[2]/a[{i_3_bs}]/div/div/div[2]'

                    xpath_pts_reb_ast = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div'\
                                        '/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div[3]/div/div/div[2]/div[2]'\
                                       f'/a[{i_3_bs}]'
                    
                    try:
                        element_name_position = WebDriverWait(driver, 5).until(EC.presence_of_element_located
                                                                        ((By.XPATH, 
                                                                          xpath_name_position))).text.splitlines()
                        element_pts_reb_ast = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, 
                                                                                  xpath_pts_reb_ast))).text.splitlines()
                    
                    except:
                        print(f'\nActivated EXCEPTIONE: No found best player element...!')
                        # Saltar de inmediato a la siguiente iteración de "for i_3_bs in range(1, 4):"
                        continue

                    # Crear una lista unificda de los datos del jugador top del equipo en el partido
                    # list_bets_player = ['name_player', 'position', 'points', 'rebounds', 'assists']
                    list_bets_player = []
                    list_bets_player.extend(element_name_position)                    
                    list_bets_player.extend(element_pts_reb_ast)

                    if len(list_bets_player) == 6:
                        # Eliminar el dato del número de la camiseta
                        del list_bets_player[1]
                        
                        # Contador para las llaves del diccionario
                        count_keys = 0
                        
                        # Home's Top players
                        if i_bets_players == 0:
                            
                            # Agregar los datos al dictionary
                            for i_keys_h_tp in list_keys_tp:
                                list_data_temp.append(f'h_tp{i_3_bs}_{i_keys_h_tp}')
                                list_data_temp.append(list_bets_player[count_keys])
                                count_keys += 1
                        
                        # Away's Top players
                        else:
                            # Agregar los datos al dictionary
                            for i_keys_a_tp in list_keys_tp:
                                list_data_temp.append(f'a_tp{i_3_bs}_{i_keys_a_tp}')
                                list_data_temp.append(list_bets_player[count_keys])
                                count_keys += 1
            
                # Cambiar al equipo visitante y obtener sus respectivos top de jugadores del partido
                if i_bets_players == 0:
                    xpath_change_team_on_bs = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/d'\
                                              'iv/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div[2]/div/div[2]'
                    element_change_team_on_bs = click_on(driver, xpath_change_team_on_bs, 10, click_js=True)                    
            # END --------- ACCESS TO TOP MATCH'S PLAYERS                                                              #
            # ======================================================================================================== #

            # ======================================================================================================== #
            # ACCESS TO STATISTICS                                                                                     #
            # ======================================================================================================== #
            # xpath del botón "STATISTICS"
            # y dar clic sobre el componente que contiene las estadísticas del partido "x"
            name_search = 'Statistics'
            xpath_statistics_x = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]'\
                                 '/div/div[1]/div/div/div[3]/div[1]/div/div/div/h2[3]/a' 
            search_box_score_or_statistics(driver, xpath_statistics_x, name_search)

            # For para acceder a las estadísticas individuales de cada cuarto (Q1, Q2, Q3 y Q4)
            for i_quarters in range(2, 6):
                # xpath de cada cuarto
                xpath_quarter_x = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2'\
                                 f']/div/div[1]/div/div/div[3]/div[2]/div/div/div[1]/div[{i_quarters}]'
                
                # Clic sobre cada quarto
                element_quarter_x = click_on(driver, xpath_quarter_x, 10, click_js=True)

                # Número del cuarto actual (Q1 o Q2 o Q3 o Q4)
                quarter_x = i_quarters-1
                
                # Obtener las estadísticas del paritdo "x"                
                list_stats_quarter_rx = get_statistics_match(driver, quarter_x)
                
                list_data_temp.extend(list_stats_quarter_rx)
            # END --------- ACCESS TO STATISTICS                                                                       #
            # ======================================================================================================== #
                    
            # ======================================================================================================== #
            # LOAD DICTIONARY                                                                                          #
            # ======================================================================================================== # 

            # Longitud de la lista que contiene toda la data del partido actual
            len_list_data_temp = len(list_data_temp)

            try:
                # Si la lista es de longitud par, se inicia la sincronización con la instancia de clase creada 
                if len_list_data_temp % 2 == 0:
                    
                    # Iterar sobre las futuras llaves del diccionario principal
                    for i_sync_data in range(0, len_list_data_temp, 2):
                        to_next_key = list_data_temp[i_sync_data]

                        # Agregar un nuevo elemento al valor lista de la llave "to_next_key" del dicicoanrio de la 
                        # instancia de clase solo si la llave existe en el diccionario de la instancia de clase
                        if to_next_key in obj_data_matches.list_keys_match:
                            obj_data_matches.dict_db_nba_match[to_next_key].append(list_data_temp[i_sync_data+1])
                
                else:                    
                    raise('La lista temporal de datos del partido no contiene los datos suficientes para sincronizar c'\
                          'on un diccioanrio')

            except:
                print(f'\nActivated EXCEPTIONE:...raise!')   

            # Obtén las longitudes de todas las listas de los valores del dict "obj_data_matches.dict_db_nba_match" 
            lengths = [len(valor) for valor in obj_data_matches.dict_db_nba_match.values()]
            
            # Verificar si todas las longitudes de las listas de los valores del diccionario son iguales
            if all(i_len == lengths[0] for i_len in lengths):
                pass

            else:
                # Encuentra la longitud máxima entre las listas que son los valore del diccionario
                len_max_key_dict = max(len(valor) for valor in obj_data_matches.dict_db_nba_match.values())

                # Llena las listas con valores "None" de la listas que están incompletas o 
                # no tiene valores para el partido actual
                for clave, valor in obj_data_matches.dict_db_nba_match.items():
                    obj_data_matches.dict_db_nba_match[clave] = valor + [None] * (len_max_key_dict - len(valor))

            # END --------- LOAD DICTIONARY                                                                            #
            # ======================================================================================================== #                                
        
        # END --------- ACCESS SEASON'S MATCHES X 10                                                                   #
        # ============================================================================================================ #
        
        try:
            click_on_previous(driver)
            
            count_click_on_previous += 1

            time_end = datetime.datetime.now()

        except:
            print('\nActivated EXCEPTIONE: button "PREVIOUS" no found. END SEASON...!')
            flag_no_change_season = True
            break

        # Calcular los segundos transcurridos en la iteración del bucle while actual
        diff_time = (time_end - time_now).seconds
        print(f'\nTiempo transcurrido: {diff_time} segundos')    

    # END --------- ACCES TO MATCHES AND PREVIOUS BUTTON                                                               #
    # ================================================================================================================ # 
    
    # Setear el valor a usar para la creación del archivo .csv 
    # con el valor del # de clics dados sobre una la sesión actual
    obj_data_matches.count_click_on_previous = count_click_on_previous

    # Crear el archivo .csv con los datos obtenidos durante la iteración actual
    obj_data_matches.create_folder_and_csv()
    obj_data_matches.restart_dict_db_nba_match()
    
    # Eliminar la instancia de clase creada en cada iteración para controlar el uso de memoría
    del obj_data_matches

    return flag_no_change_season, count_click_on_previous
    
# END --------- SCRAPING WEB                                                                                           #
# ==================================================================================================================== #


# ==================================================================================================================== #
# MAIN                                                                                                                 #
# ==================================================================================================================== #
# Season a obtener data
dict_sesons = {0: '', 1: '23-24', 2: '22-23', 3: '21-22', 4: '20-21', 5: '19-20', 6: '18-19', 7: '17-18', 
                      8: '16-17', 9: '15-16',}
max_season = 5
def get_and_set_data_nba():
    """
    Función principal. Crear el WebDriver y abre el navegador
    
    Args:
        No

    Returns:
        No

    Examples:
        >>> get_and_set_data_nba()

        >>> get_and_set_data_nba()
    """

    # ================================================================================================================ #
    # CONN DRIVER                                                                                                      #
    # ================================================================================================================ #   

    # Inicializar el driver
    driver = inicializar_driver()

    # Abrir navegador
    driver.maximize_window()
    driver.get('https://www.sofascore.com/tournament/basketball/usa/nba/132') 
      
    # END --------- CONN DRIVER                                                                                        #
    # ================================================================================================================ # 

    # Contador del número de la season actual
    count_season = 2

    # contador de clics sobre "PREVIOUS" dados durante la ejecución del código
    count_click_on_previous_tx = 80
    flag_count_click_on_previous_tx_del = False

    # Bandera que cambia cuando ya no está disponible el botón "PREVIOUS" 
    flag_no_change_season_rx = True

    # ================================================================================================================ #
    # ACCESS TO EACH SEASON                                                                                            # 
    # ================================================================================================================ #   

    # Mientras hallan seasons a sensar (count_season < 10) en función del diccionario "dict_sesons"
    while count_season < max_season:

        # str con la season actual
        current_season = dict_sesons[count_season]

        # Si se agotó el tiempo, recargar la página web
        if not flag_no_change_season_rx:           
            print('\nRecargando la página web...')
            
            # Recarga página web
            driver.refresh()
            

        # si se acabaron los partidos de la season actual. Cambiar de season
        if flag_no_change_season_rx:
            # 
            if count_click_on_previous_tx != 0:
                # Cambiar contador del valor de season
                count_season += 1

            # ======================================================================================================== #
            # CHOOSE NBA LEAGUE                                                                                        #
            # ======================================================================================================== #
            choose_options_menu(driver=driver, choose_option=count_season)
            # END --------- CHOOSE NBA LEAGUE                                                                          #
            # ======================================================================================================== #      

            if flag_count_click_on_previous_tx_del:
                # Resetear el valor del contador de clics sobre PREVIOUS "count_click_on_previous_tx"
                count_click_on_previous_tx -= count_click_on_previous_tx

            flag_count_click_on_previous_tx_del = True

            print(f'\nSe Cambió a la temporada { dict_sesons[count_season]} de la NBA...')
        
        # "flag_no_change_season_rx = True" Significa que se acabaron los partidos de la season actual
        # "flag_no_change_season_rx = False" Significa que se agotó el tiempo. Recargar la página
        flag_no_change_season_rx, count_click_on_previous_rx = open_and_scraping_web(driver, count_click_on_previous_tx,
                                                                                     current_season)

        count_click_on_previous_tx = count_click_on_previous_rx

    # END --------- ACCESS TO EACH SEASON                                                                              #
    # ================================================================================================================ # 
            
    # Cerrar navegador
    driver.quit()

    print('\nFIN...\n')
# END --------- MAIN                                                                                                   #
# ==================================================================================================================== #
    