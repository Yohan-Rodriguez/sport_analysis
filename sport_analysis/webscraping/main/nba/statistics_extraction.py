from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

def get_statistics_match(driver, quarter_x):
    """
    Obtener las estadisticas de cada partido en las pestaña "STATISTICS" dentro de la página web.
    Realizar Scroll dentro del div que contiene dichas estadísticas.

    Args:
        driver: WebDriver
        quarter_x: Referencia al cuarto específico sobre el que se está obteniendo las estadísiticas

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

    # Xpath de la barra deslizante vertical donde están contenidas las estadísticas del partido
    xpath_scroll_bar = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/div/div[3]'

    for i_dev_stat in range(1, 4):
        
        # Número de pixeles a mover inicialmente en el scroll_bar
        move_px_scroll_bar = 100 if(i_dev_stat==1) else 110

        # XPATH del div que contiene llas estadísticas del aprtido (son 3 div's)
        xpath_stat_dev_x = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/div/div[1]'\
                        f'/div/div/div[3]/div[2]/div/div/div[2]/div/div[{i_dev_stat}]'
        
        try:
            # Elemento encontrado
            elem_stat_dev_x = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_stat_dev_x)))
            
            # Mostrar las estadísticas del partido
            print(f'elem_stat_dev_{i_dev_stat}', elem_stat_dev_x.text)
        except:
            print(f'Activated EXCEPTIONE: No se ha encontrado el elemento "elem_stat_dev_{i_dev_stat}" de las estadisticas')
        
        # El scroll se realiza solo en las 2 primeras iteraciones
        if i_dev_stat in [1, 2]:
            try:
                scroll_bar = driver.find_element(By.XPATH, xpath_scroll_bar)

                # Permite hacer 'scroll' en la ventana que contiene la información completa del partido seleccionado.
                action = ActionChains(driver)

                # Se mueve "move_px_scroll_bar"px hacia abajo.
                action.move_to_element_with_offset(scroll_bar, 0, move_px_scroll_bar).click().perform()

            except Exception as e:
                print('Activated EXCEPTIONE: On Scroll statistics', e, end='\n')
                continue
