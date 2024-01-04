import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .seasons_nba import choose_options_menu
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


def get_and_set_data_nba():
    # Inicializar el driver
    driver = inicializar_driver()

    # Abrir navegador
    driver.maximize_window()
    driver.get('https://www.sofascore.com/tournament/basketball/usa/nba/132')

    for i_teams in range(2, 5, 1):
        # ============================================================================================================ #
        # CHOOSE NBA LEAGUE                                                                                            #
        # ============================================================================================================ #
        choose_options_menu(driver=driver, choose_option=i_teams)
        # END --------- CHOOSE NBA LEAGUE                                                                              #
        # ============================================================================================================ #

        # Continuar aquí con la lógica para acceder a cada partido de la termporada de la NBA seleccionada:
        for i_matches in range(10, 0, -1):

 
    #     # Buscar el XPAHT de cada uno de los 30 equipos
    #     div_team = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[3]'\
    #                                          f'/div/a[{i_teams}]/div/div[3]/div/span')

    #     name_team = div_team.text
    #     #name_team = ''
    #     set_name_dict_team(name_team)

    #     driver.execute_script("arguments[0].click();", div_team)

    #     storage_players(driver, name_team)

    #     # xpath_back = '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[3]/div[3]/div[2]/a[1]/div'
    #     # div_back = driver.find_element(By.XPATH, xpath_back)
    #     # driver.execute_script("arguments[0].click();", div_back)
                
    #     print('\nREGRESAR...!')

    #     driver.get('https://www.sofascore.com/tournament/basketball/usa/nba/132')

    #     print('\nSe regresó a la página incial...!')

        time.sleep(3)
    
    # Cerrar navegador
    driver.quit()

    print('\nFIN...\n')
