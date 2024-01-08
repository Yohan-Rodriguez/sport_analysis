import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .aux_functions import choose_options_menu, click_on, click_on_previous
from .statistics_extraction import get_statistics_match
from .dictionaries_db import set_name_dict_team, set_info_players_in_dict_team, get_dict_teams



def storage_players(driver, name_team):
    # Buscar sección de "MATCHES"
    xpath_matches = '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[1]'
    matches = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_matches)))
    matches.click()


    # ================================================================================================================ #
    # GET INFO PLAYERS TEAM                                                                                            #
    # ================================================================================================================ #
    # Buscar sección de "list_players" y dar clic sobre él
    xpath_list_players = '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[2]/label[2]/div/span'    
    list_view_players = driver.find_element(By.XPATH, xpath_list_players)
    driver.execute_script("arguments[0].click();", list_view_players)

    i_player = 1
    while True:
        try:
            xpath_name_player =  '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[3]/table/'\
                                f'tr[{i_player}]/td[1]/a/div/span' 
            
            xpath_position_player =  '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[3]/ta'\
                                    f'ble/tr[{i_player}]/td[2]/div/span'
            
            xpath_age_player =  '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[3]/table/t'\
                               f'r[{i_player}]/td[3]/div'
            
            name_player = driver.find_element(By.XPATH, xpath_name_player).text
            position_player = driver.find_element(By.XPATH, xpath_position_player).text
            age_player = driver.find_element(By.XPATH, xpath_age_player).text                       

            dict_info_player = {'Name_Player': name_player, 'Position_Player': position_player, 'Age_Player': int(age_player)}

            set_info_players_in_dict_team(name_team, dict_info_player, key_dict='Players')


            i_player += 1

        except Exception as e:
            dict_teams = get_dict_teams()
            print(dict_teams)
            break
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
def open_and_scraping_web(driver, count_click_on_previous_tx):  

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
    # ACCES TO MATCHES AND PREVIOUS BUTTON                                                                                      #
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
        # ACCESS SEASON'S MATCHES X 10                                                                                     #
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
                # Información del partido como: nombres de los equipos, fecha y marcadores.
                # print(f'element_match_{i_matches}.text:', element_match_x.text)
                print('\n# Cliks:', count_click_on_previous, '- # del match:', i_matches)




            except:
                print('Activated EXCEPTIONE: No se puede acceder al método ".text" del elemento del partido "X"')

            # ======================================================================================================== #
            # ACCESS TO STATISTICS                                                                                     #
            # ======================================================================================================== #
            # xpath del botón "STATISTICS"
            # y dar clic sobre el componente que contiene las estadísticas del partido "x"
            for i_statisctics in range(10):
                xpath_statistics_x = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/'\
                                    'div/div[1]/div/div/div[3]/div[1]/div/div/div/h2[3]/a' 
                        
                element_statistics_x = click_on(driver, xpath_statistics_x, 10, click_js=True)

                if element_statistics_x.text == 'Statistics':
                    break


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

    # Bandera que cambia cuando ya no está disponible el botón "PREVIOUS" 
    flag_no_change_season_rx = True

    # ============================================================================================================ #
    # ACCESS TO EACH SEASON                                                                                        #
    # ============================================================================================================ #    
    # Mientras hallan seasons a sensar (count_season < 10)
    while count_season < max_season:

        # Si se agotó el tiempo, recargar la página web
        if not flag_no_change_season_rx:
            print('\nRecargando la página web...')
            # Recarga página web
            driver.refresh()

        # si se acabaron los partidos de la season actual. Cambiar de season
        if flag_no_change_season_rx:
            # ============================================================================================================ #
            # CHOOSE NBA LEAGUE                                                                                            #
            # ============================================================================================================ #
            print('\nCambiando de temporada de la NBA...')

            choose_options_menu(driver=driver, choose_option=count_season)
            
            # Fecha de la season. Ejemplo: para "i_teams = 5" → season = '19/20'
            date_season_str = dict_sesons[count_season]

            # Asignar nueva season
            count_season += 1

            # Resetear el valor de "count_click_on_previous_tx"
            count_click_on_previous_tx -= count_click_on_previous_tx
            # END --------- CHOOSE NBA LEAGUE                                                                              #
            # ============================================================================================================ #
            
        # "flag_no_change_season_rx = True" Significa que se acabaron los partidos de la season actual
        # "flag_no_change_season_rx = False" Significa que se agotó el tiempo. Recargar la página
        flag_no_change_season_rx, count_click_on_previous_rx = open_and_scraping_web(driver, count_click_on_previous_tx)

        count_click_on_previous_tx = count_click_on_previous_rx
    # END --------- ACCESS TO EACH SEASON                                                                          #
    # ============================================================================================================ # 
            
    # Cerrar navegador
    driver.quit()

    print('\nFIN...\n')
# END --------- MAIN                                                                                                   #
# ==================================================================================================================== #