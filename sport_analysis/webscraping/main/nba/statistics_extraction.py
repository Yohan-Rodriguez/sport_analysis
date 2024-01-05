from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_statistics_match(driver):
    """
    Obtener las estadisticas de cada partido en las pestaña "STATISTICS" dentro de la página web.

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

    move_px_y = 160
    for i_dev_stat in range(1, 4):
        xpath_stat_dev_x = '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/div/div[1]'\
                        f'/div/div/div[3]/div[2]/div/div/div[2]/div/div[{i_dev_stat}]'
        
        elem_stat_dev_x = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_stat_dev_x)))
        
        try:
            print(f'elem_stat_dev_{i_dev_stat}', elem_stat_dev_x.text)
            # Obtiene el valor actual del atributo style
            # current_style = elem_stat_dev_x.get_attribute("style")
            print(elem_stat_dev_x.get_attribute("style"))

            # # Modificar el valor del atributo style
            # new_style = current_style.replace("top: 0px", f"top: {move_px_y}px")

            # # Establece el nuevo valor del atributo style
            # elem_stat_dev_x.set_attribute("style", new_style)

            # move_px_y += 40
        except Exception as e:
            print(f'{e}, Etiqueta "div_{i_dev_stat}" de las estadísticas no encontrado...')
    