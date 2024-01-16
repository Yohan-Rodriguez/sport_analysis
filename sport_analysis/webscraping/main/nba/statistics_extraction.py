from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


def get_statistics_match(driver, quarter_x):
    """
    Obtener las estadisticas de cada partido en las pestaña "STATISTICS" dentro de la página web.
    Realizar Scroll dentro del div que contiene dichas estadísticas.

    Args:
        driver: WebDriver

    Returns:
        Función sin return.

    Raises:
        print informativo

    Examples:
        >>> get_statistics_match(driver)

            elem_stat_dev_1 23/26 (88%)
            Free throws
            19/22 (86%)
            32/66 (48%)
            2 pointers
            29/52 (55%)
            8/20 (40%)
            3 pointers
            12/33 (36%)
            40/86 (46%)
            Field goals
            41/85 (48%)
            elem_stat_dev_2 38
            Rebounds
            40
            30
            Defensive rebounds
            29
            elem_stat_dev_3

        >>> get_statistics_match(driver)
              
    """


    # dict_stats_quarter = {
    #                         'stats_q_h': {
    #                                         'stats_q1-1': {}, 'stats_q1-2': {}, 'stats_q1-3': {},
    #                                         'stats_q2-1': {}, 'stats_q2-2': {}, 'stats_q2-3': {},
    #                                         'stats_q3-1': {}, 'stats_q3-2': {}, 'stats_q3-3': {},
    #                                         'stats_q4-1': {}, 'stats_q4-2': {}, 'stats_q4-3': {},
    #                         },
    #                         'stats_q_a': {
    #                                         'stats_q1-1': {}, 'stats_q1-2': {}, 'stats_q1-3': {},
    #                                         'stats_q2-1': {}, 'stats_q2-2': {}, 'stats_q2-3': {},
    #                                         'stats_q3-1': {}, 'stats_q3-2': {}, 'stats_q3-3': {},
    #                                         'stats_q4-1': {}, 'stats_q4-2': {}, 'stats_q4-3': {},
    #                         }
    #                      }

    list_stats_quarter = []
    
    # Xpath de contenedor de la barra deslizante vertical donde están contenidas las estadísticas del partido
    xpath_container_scroll_bar = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/div/div[3]'
    # Elemento del contenedor de la barra vertical
    container_scroll_bar = driver.find_element(By.XPATH, xpath_container_scroll_bar)

    # for para ingresar a cad uno de los 3 divs que contieenn las estadísitcas de cada cuarto
    for i_dev_stat in range(1, 4):        
        
        try:
            # XPATH del div que contiene las estadísticas del partido (son 3 div's diferentes)
            xpath_stat_dev_x = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/div/div[1]'\
                            f'/div/div/div[3]/div[2]/div/div/div[2]/div/div[{i_dev_stat}]'
            
            # Elemento de las estadísticas del partido encontrado
            elem_stat_dev_x = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_stat_dev_x)))
            
            # Mostrar las estadísticas del partido
            # print('Estadísticas:', elem_stat_dev_x.text, sep='\n')

            # Lista de datos
            list_elem_stat_dev_x = elem_stat_dev_x.text.splitlines()

            # Longitud de la lista
            len_list_elem_stat_dev_x = len(list_elem_stat_dev_x)

            # Verificar que el conjunto de datos este organizado en subconjuntos de 3 elementos cada uno
            if len_list_elem_stat_dev_x % 3 == 0:

                # Iterar sobre los elementos de la lista que serán las claves del diccionario
                for i_stats_q in range(1, len_list_elem_stat_dev_x, 3):
                    list_stats_quarter.append(f'h_q{quarter_x}_{list_elem_stat_dev_x[i_stats_q]}')
                    list_stats_quarter.append(list_elem_stat_dev_x[i_stats_q-1])
                    list_stats_quarter.append(f'a_q{quarter_x}_{list_elem_stat_dev_x[i_stats_q]}')
                    list_stats_quarter.append(list_elem_stat_dev_x[i_stats_q+1])

                    # dict_stats_quarter['stats_q_h'][f'stats_q{quarter_x}-{i_dev_stat}'][list_elem_stat_dev_x[i_stats_q]] = list_elem_stat_dev_x[i_stats_q-1]
                    # dict_stats_quarter['stats_q_a'][f'stats_q{quarter_x}-{i_dev_stat}'][list_elem_stat_dev_x[i_stats_q]] = list_elem_stat_dev_x[i_stats_q+1]

        except:
            print(f'Activated EXCEPTIONE: No se ha encontrado el elemento "elem_stat_dev_{i_dev_stat}" de las estadisticas')
        
        # El desplazamiento de scroll se realiza solo en la primera iteración
        # déspues de obtener las estadísticas del primer <div> de los 3 div's que contiene estadísticas 
        try:
            if i_dev_stat == 1:
                # Onjeto que permite hacer 'scroll' en las estadísticas completas del partido seleccionado
                action = ActionChains(driver)

                # Se mueve "move_px_scroll_bar" px hacia abajo.
                action.move_to_element_with_offset(container_scroll_bar, 0, 110).click().perform()

            elif i_dev_stat == 3:
                # Vuelve a la posición inicial de la barra de desplazamiento
                action.move_to_element_with_offset(container_scroll_bar, 0, 0).click().perform()
                
                # Vuelve a la posición inicial de la barra de desplazamiento utilizando JavaScript
                # driver.execute_script("arguments[0].scrollTop = 0;", container_scroll_bar)


        except Exception as e:
            print('Activated EXCEPTIONE: On Scroll statistics', e, end='\n')
            continue

    return list_stats_quarter
    # return dict_stats_quarter

    
