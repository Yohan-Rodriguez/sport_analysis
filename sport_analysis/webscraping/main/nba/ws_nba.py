import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .aux_functions import choose_options_menu, click_on, click_on_previous, search_box_score_or_statistics
from .statistics_extraction import get_statistics_match
# from .template_info_to_send_to_db import set_info_players_in_dict_team, get_dict_teams
from .template_info_to_send_to_db import TemplateInfoToSendToDB as tisdb



def storage_players(driver, name_team):
    pass
    # # Buscar sección de "MATCHES"
    # xpath_matches = '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[1]'
    # matches = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_matches)))
    # matches.click()


    # # ================================================================================================================ #
    # # GET INFO PLAYERS TEAM                                                                                            #
    # # ================================================================================================================ #
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

    #         dict_info_player = {'Name_Player': name_player, 'Position_Player': position_player, 'Age_Player': int(age_player)}

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



def inicializar_driver():
    # ================================================================================================================ #
    # CHROME DRIVER CONNECTION                                                                                         #
    # ================================================================================================================ #
    options = webdriver.ChromeOptions()
    options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
    driver = webdriver.Chrome(options=options)

    return driver
    # END --------- CHROME DRIVER CONNECTION                                                                           #
    # ================================================================================================================ #

    return driver


# ==================================================================================================================== #
# SCRAPING WEB                                                                                                         #
# ==================================================================================================================== #
def open_and_scraping_web(driver, count_click_on_previous_tx, currente_season, num_folder, list_restricted_id_teams,
                          list_restricted_id_matches):  

    # instanciaq de la clase "template_info_to_send_to_db()"
    obj_dict_data = tisdb()

    # Setear el valor del atributo "num_folder" de la instancia creada de la clase "template_info_to_send_to_db()"
    obj_dict_data.num_folder = num_folder



    # Bandera para recargar la página cada 23 minutos
    time_now = datetime.datetime.now()
    time_end = datetime.datetime.now()
    diff_time = (time_end - time_now).seconds

    count_click_on_previous = count_click_on_previous_tx

    # ============================================================================================================ #
    # BUTTON PREVIOUS INITIAL                                                                                      #
    # ============================================================================================================ #
    if count_click_on_previous > 0:
        # Número de clics sobre "PREVIOUS" dados hasta el momento durante la ejecución del código
        click_on_previous(driver=driver, iterations=(count_click_on_previous))
    # END --------- BUTTON PREVIOUS INITIAL                                                                        #
    # ============================================================================================================ # 
    
    # ============================================================================================================ #
    # ACCES TO MATCHES AND PREVIOUS BUTTON                                                                         #
    # ============================================================================================================ #    
    # Bandera que cambia cuando ya no está disponible el botón "PREVIOUS" 
    flag_no_change_season = False
    while (not flag_no_change_season) and (diff_time < 90):
        
        # div principal que contiene como máximo 10 partidos
        xpath_div_main_10_matches = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]'
        div_main_10_matches = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_div_main_10_matches)))

        # Encontrar todos los elementos div secundarios dentro del div principal
        divs_secundarios = div_main_10_matches.find_elements(By.TAG_NAME, "div")

        # Obtener el número total de divs secundarios
        nume_divs_scundarios = len(divs_secundarios)

        # ============================================================================================================ #
        # ACCESS SEASON'S MATCHES X 10                                                                                 #
        # ============================================================================================================ #
        # Acceder a cada uno de los X partidos cargados en el div principal que contien los partidos
        for i_matches in range(1, (nume_divs_scundarios+1)):

            # xpath de cada partido dentro de la etiqueta <div> que contiene los 10 partidos (como máximo)
            xpath_match_x = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div'\
                            f'[2]/div[{i_matches}]/a'
            
            try:
                # Clic sobre cada partido
                if i_matches ==1:
                    element_match_x = click_on(driver, xpath_match_x, 5)
                else:
                    element_match_x = click_on(driver, xpath_match_x, 5, True)
            
            except:
                print('\nActivated EXCEPTIONE: match no found...')
                # Salir del for que controla el acceso a los partiodos
                break

            try:
                print('\n# Cliks:', count_click_on_previous, '- # del match:', i_matches)
                # Información del partido como: nombres de los equipos, fecha y marcadores.
                print(f'Data:', element_match_x.text, sep='\n')
                
                # Crear la lista con la información base del partido
                list_info_match = element_match_x.text.splitlines()

                # Eliminar la posición "FT"
                del list_info_match[1]
                print('FT eliminado')

                len_list_info_match = len(list_info_match) 

                # Si el partido no tuvo overtime, la lista tendrá 13 elementos string
                if len_list_info_match == 13:
                    # Agregar el overtime en matches.is_overtime
                    obj_dict_data.dict_db_nba['matches']['is_overtime'].append(0)
                    print(list_info_match)

                # Si el partido si tuvo overtime, la lista tendrá 15 elementos string
                elif len_list_info_match == 15:
                    obj_dict_data.dict_db_nba['matches']['is_overtime'].append(1)
                    # Eliminar los elementos que referencian los 2 puntajes del overtime
                    del list_info_match[12]
                    del list_info_match[7]
                    print('AET Eliminado')  
                    print(list_info_match)                

                # Nombre del equipo local
                n_home = list_info_match[1]
                # Nombre del equipo visitante
                n_away = list_info_match[2]

                list_names_teams = [n_home, n_away]

                # Evaluar si los equipos del partido ya existen en el diccionario
                for i_team in list_names_teams:
                    # Si el equipo no existe en el diccionario
                    if i_team not in obj_dict_data.dict_db_nba['teams']['name_team']:
                        # Adicionar los nombres de los equipos local y visitante
                        obj_dict_data.dict_db_nba['teams']['name_team'].append(n_home)
                        obj_dict_data.dict_db_nba['teams']['name_team'].append(n_away)

                    # Agregar nombre del equipo a "team_stats.name_team"
                    obj_dict_data.dict_db_nba['team_stats']['name_team'].append(i_team)
                    
                    if i_team == n_home:
                        # Agregar que el quipo es el local en "team_stats.name_team"
                        obj_dict_data.dict_db_nba['team_stats']['is_home'].append(1) 
                        # Agregar puntos finales del local
                        obj_dict_data.dict_db_nba['team_stats']['total_points'].append([11])
                        # Agregar puntos de los cuartos del local
                        obj_dict_data.dict_db_nba['team_stats']['q1'].append([3])
                        obj_dict_data.dict_db_nba['team_stats']['q2'].append([4])
                        obj_dict_data.dict_db_nba['team_stats']['q3'].append([5])
                        obj_dict_data.dict_db_nba['team_stats']['q4'].append([6])

                    else:
                        # Agregar que el quipo es visitante en "team_stats.name_team"
                        obj_dict_data.dict_db_nba['team_stats']['is_home'].append(0) 
                        # Agregar puntos finales del visitante
                        obj_dict_data.dict_db_nba['team_stats']['total_points'].append([12])
                        # Agregar puntos de los cuartos del visitante
                        obj_dict_data.dict_db_nba['team_stats']['q1'].append([7])
                        obj_dict_data.dict_db_nba['team_stats']['q2'].append([8])
                        obj_dict_data.dict_db_nba['team_stats']['q3'].append([9])
                        obj_dict_data.dict_db_nba['team_stats']['q4'].append([10])

                # Agregar fecha de "matches"
                obj_dict_data.dict_db_nba['matches']['date_match'].append(list_info_match[6:], '-',
                                                                          list_info_match[3:5], '-',
                                                                          list_info_match[:2])
                
            except:
                print('Activated EXCEPTIONE: No se puede acceder al método ".text" del elemento del partido "X"')

            # ======================================================================================================== #
            # ACCESS TO TOP MATCH'S PLAYERS                                                                            #
            # ======================================================================================================== #
            name_search = 'BOX SCORE'
            xpath_box_score_x = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/'\
                                'div/div[1]/div/div/div[3]/div[1]/div/div/div/h2[2]/a'
            search_box_score_or_statistics(driver, xpath_box_score_x, name_search)

            for i_bets_players in range(2):

                for i_3_bp in range(1, 4):
                    xpath_name_position = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/d'\
                                        f'iv[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div[3]/div/div/div[1]/div[2]/a[{i_3_bp}]/div/div/div[2]'

                    xpath_pts_reb_ast = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div'\
                                        f'[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/a[{i_3_bp}]'
                    
                    element_name_position = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_name_position))).text
                    element_pts_reb_ast = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_pts_reb_ast))).text
                    
                    # listas con los datos del jugador top del equipo en el partido 
                    list_bets_player = element_name_position.splitlines()
                    list_element_pts_reb_ast = element_pts_reb_ast.splitlines()

                    # Crear una lista unificda de los datos del jugador top del equipo en el partido
                    list_bets_player.extend(list_element_pts_reb_ast)

                    if len(list_bets_player) == 6:
                        # Eliminar el dato del número de la camiseta
                        del list_bets_player[1]

                        # Agregar los datos al dictionary
                        obj_dict_data.dict_db_nba['top_players']['name_player'].append(list_bets_player[0])
                        obj_dict_data.dict_db_nba['top_players']['position'].append(list_bets_player[1])
                        obj_dict_data.dict_db_nba['top_players']['points'].append(list_bets_player[2])
                        obj_dict_data.dict_db_nba['top_players']['rebounds'].append(list_bets_player[3])
                        obj_dict_data.dict_db_nba['top_players']['assists'].append(list_bets_player[4])

                # Cambiar al equipo visitante y obtener su top de jugadores del partido
                if i_bets_players == 0:
                    xpath_change_team_on_bs = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/'\
                                              'div/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div[2]/div/div[2]'
                    element_change_team_on_bs = click_on(driver, xpath_change_team_on_bs, 10, click_js=True)                    
            # END --------- ACCESS TO TOP MATCH'S PLAYERS                                                              #
            # ======================================================================================================== #

            # ======================================================================================================== #
            # ACCESS TO STATISTICS                                                                                     #
            # ======================================================================================================== #
            # xpath del botón "STATISTICS"
            # y dar clic sobre el componente que contiene las estadísticas del partido "x"
            xpath_statistics_x = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/'\
                                    'div/div[1]/div/div/div[3]/div[1]/div/div/div/h2[3]/a' 
            name_search = 'STATISTICS'
            search_box_score_or_statistics(driver, xpath_statistics_x, name_search)

            # For para acceder a las estadísticas individuales de cada cuarto (Q1, Q2, Q3 y Q4)
            for i_quarters in range(2, 6):
                # xpath de cada cuarto
                xpath_quarter_x = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]'\
                                f'/div/div[1]/div/div/div[3]/div[2]/div/div/div[1]/div[{i_quarters}]'
                
                # Clic sobre cada quarto
                element_quarter_x = click_on(driver, xpath_quarter_x, 10, click_js=True)

                # Núemro del cuarto actual (Q1 o Q2 o Q3 o Q4)
                quarter_x = i_quarters-1
                
                # Obtener las estadísticas del paritdo "x"
                print('# Cliks:', count_click_on_previous, '- # del match:', i_matches, '- Quarto:', quarter_x)
                get_statistics_match(driver)
            # END --------- ACCESS TO STATISTICS                                                                       #
            # ======================================================================================================== #
        
        # END --------- ACCESS SEASON'S MATCHES X 10                                                                       #
        # ============================================================================================================ #

        try:
            click_on_previous(driver)
            
            count_click_on_previous += 1

            time_end = datetime.datetime.now()

        except:
            print('\nActivated EXCEPTIONE: button "PREVIOUS" no found. END SEASON...!')
            flag_no_change_season = True
            break

        diff_time = (time_end - time_now).seconds
        print(f'\nTiempo transcurrido: {diff_time} segundos')    

    # END --------- ACCES TO MATCHES AND PREVIOUS BUTTON                                                                  #
    # ============================================================================================================ # 
    
    # Crear el archivo .csv con los datos obtenidos durante la iteración actual
    obj_dict_data.create_folder_and_csv()
    
    # Eliminar la instancia de clase creada en cada iteración para controlar el uso de memoría
    del obj_dict_data

    return flag_no_change_season, count_click_on_previous
# END --------- SCRAPING WEB                                                                                           #
# ==================================================================================================================== #


# ==================================================================================================================== #
# MAIN                                                                                                                 #
# ==================================================================================================================== #
# Season a obtener data
dict_sesons = {0: '', 1: '23/24', 2: '22/23', 3: '21/22', 4: '20/21', 5: '19/20', 6: '18/19', 7: '17/18', 
                      8: '16/17', 9: '15/16',}

# Número de seasons a sensar
# max_season = len(dict_sesons.values())
max_season = 5

def get_and_set_data_nba():

    # Inicializar el driver
    driver = inicializar_driver()

    # Abrir navegador
    driver.maximize_window()
    driver.get('https://www.sofascore.com/tournament/basketball/usa/nba/132')   

    # Contador del número de la season actual
    count_season = 2

    # contador de clics sobre "PREVIOUS" dados durante la ejecución del código
    count_click_on_previous_tx = 0

    # Contador para referenciar del archivo .csv ha crear
    num_folder = 1

    # Lista de id's de equipo ya asignados
    list_restricted_id_teams = []
    
    # Lista de id's de equipo ya asignados
    list_restricted_id_matches = []

    # Bandera que cambia cuando ya no está disponible el botón "PREVIOUS" 
    flag_no_change_season_rx = True

    # ============================================================================================================ #
    # ACCESS TO EACH SEASON                                                                                        #
    # ============================================================================================================ #   

    # Mientras hallan seasons a sensar (count_season < 10)
    while count_season < max_season:

        # str con la season actual
        currente_season = dict_sesons[count_season]

        # Si se agotó el tiempo, recargar la página web
        if not flag_no_change_season_rx:           
            print('\nRecargando la página web...')
            
            # Recarga página web
            driver.refresh()
            
            num_folder += 1

        # si se acabaron los partidos de la season actual. Cambiar de season
        if flag_no_change_season_rx:
            # ============================================================================================================ #
            # CHOOSE NBA LEAGUE                                                                                            #
            # ============================================================================================================ #
            print(f'\nCambiando a la temporada {currente_season} de la NBA...')

            choose_options_menu(driver=driver, choose_option=count_season)
            
            # Fecha de la season. Ejemplo: para "i_teams = 5" → season = '19/20'
            date_season_str = dict_sesons[count_season]

            # Asignar nueva season
            count_season += 1

            # Resetear el valor de "count_click_on_previous_tx"
            count_click_on_previous_tx -= count_click_on_previous_tx

            # Reset sobre el contador que referencia el archivo .csv ha crear
            num_folder -= num_folder
            # END --------- CHOOSE NBA LEAGUE                                                                              #
            # ============================================================================================================ #      
        
        # "flag_no_change_season_rx = True" Significa que se acabaron los partidos de la season actual
        # "flag_no_change_season_rx = False" Significa que se agotó el tiempo. Recargar la página
        flag_no_change_season_rx, count_click_on_previous_rx = open_and_scraping_web(driver, count_click_on_previous_tx,
                                                                                     currente_season, num_folder, list_restricted_id_teams,
                                                                                     list_restricted_id_matches)

        count_click_on_previous_tx = count_click_on_previous_rx

    # END --------- ACCESS TO EACH SEASON                                                                          #
    # ============================================================================================================ # 
            
    # Cerrar navegador
    driver.quit()

    print('\nFIN...\n')
# END --------- MAIN                                                                                                   #
# ==================================================================================================================== #