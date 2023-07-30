from selenium import webdriver
from selenium.webdriver.common.by import By
from .list_css import store_css, get_list_keys


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
    driver.get('https://www.sofascore.com/tournament/basketball/usa/nba/132#45096')    
    # END --------- CHROME DRIVER CONNECTION                                                                           #
    # ================================================================================================================ #

    for i_match in range(10, 0, -1):
        # ============================================================================================================ #
        # FUNCTION                                                                                                     #
        # ============================================================================================================ #
        def search_css(this_css):
            this_div = driver.find_element(By.CSS_SELECTOR, this_css).text
            return this_div
        # END --------- FUNCTION                                                                                       #
        # ============================================================================================================ #
        
        # Obtener "css_selector" de la finalización del partido
        # Buscar CSS indicado en el archivo "list_css.py"
        css_ft = store_css('ft', i_match)
        div_ft = search_css(css_ft)

        if (div_ft == 'FT') or (div_ft == 'AET'):
            print('\nIN\n')
            
            # Diccionario que contendrá el valor ".text" de las variables buscadas
            dict_data_match = {}

            # Lista con las tags: ['ft', 'date', 'home', 'q1_h', 'q2_h', ..., 'away', 'q1_a', 'q2_a', 'q3_a', 'q4_a', 'total_a']
            list_tags = get_list_keys(i_match)

            for i_tags_dict in list_tags:                
                if i_tags_dict in ['q1_h', 'q2_h', 'q3_h', 'q4_h', 'q1_a', 'q2_a', 'q3_a', 'q4_a']:
                    
                    list_str_change_q = ['laFqms', 'cKEAmW']
                    for i_str_change in list_str_change_q:
                        try:
                            # OBTENER "css_selector" 
                            # Buscar string con CSS indicado en el archivo "list_css.py"
                            css_i = store_css(key_rx=i_tags_dict, i_match=i_match, str_change=i_str_change)

                            # Buscar elemento dentro de la págiina web con el CSS obtenido y obtener el ".text"
                            div_i = search_css(css_i)

                        except Exception:
                            print('\nCambiando parámetro "str_change"...')

                elif i_tags_dict in ['total_h', 'total_a']:
                    
                    list_str_change_toal_points = ['hVtlqB', 'UgLMb']
                    for i_str_change in list_str_change_toal_points:
                        try:
                            # OBTENER "css_selector" 
                            # Buscar string con CSS indicado en el archivo "list_css.py"
                            css_i = store_css(key_rx=i_tags_dict, i_match=i_match, str_change=i_str_change)

                            # Buscar elemento dentro de la págiina web con el CSS obtenido y obtener el ".text"
                            div_i = search_css(css_i)

                        except Exception:
                            print('\nCambiando parámetro "str_change"...')

                else:
                    # OBTENER "css_selector" 
                    # Buscar string con CSS indicado en el archivo "list_css.py"
                    css_i = store_css(key_rx=i_tags_dict, i_match=i_match)

                    # Buscar elemento dentro de la págiina web con el CSS obtenido y obtener el ".text"
                    div_i = search_css(css_i)


                print('\ni_tags_dict: ', i_tags_dict, '\n')
                # "div_i" es el resultado del ".text"

                # Agregar nueva "key-value" en el diccionario "dict_data_match"
                dict_data_match[i_tags_dict] = div_i
                # "key" = ['ft', 'date', 'home', 'q1_h', 'q2_h', ..., 'away', 'q1_a', 'q2_a', 'q3_a', 'q4_a', 'total_a']
                # "value" = .text obtenido con la función "search_css()"

            print(dict_data_match)
                

            