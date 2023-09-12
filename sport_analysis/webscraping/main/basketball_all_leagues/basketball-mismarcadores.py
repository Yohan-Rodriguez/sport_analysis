import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webscraping.models import League
from random import randint
from django.db.utils import IntegrityError



# ==================================================================================================================== #
# BUSCAR CSS_SELECTOR BUTTON                                                                                           #
# ==================================================================================================================== #
def search_button(driver, selector_css_button):
    # Salida de emergencia al siguiente bucle para evitar que sea infinito
    flag_emergency_button = 3

    while True:
        try:
            button_previous = driver.find_element(By.CSS_SELECTOR, selector_css_button)
            break

        except Exception:
            print(f'Reintentando obtener CSS_SELECTOR de "Mostrar Más partidos".\nIntentos Restante: {flag_emergency_button} s')
            time.sleep(1)

            if flag_emergency_button <= 0:
                button_previous = ''
                break

            flag_emergency_button -= 1

    return button_previous
# END --------- BUSCAR CSS_SELECTOR BUTTON                                                                             #
# ==================================================================================================================== #


def catch_data_links():
    # ================================================================================================================ #
    # CHROME DRIVER CONNECTION                                                                                         #
    # ================================================================================================================ #
    options = webdriver.ChromeOptions()
    options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
    driver_path = "drivers/chromedriver.exe"
    driver = webdriver.Chrome(options=options)#, executable_path=driver_path)
    driver.maximize_window()

        # Abrir la ventana principal
    driver.get('https://www.flashscore.co/baloncesto/')

    # Guardar el identificador de la ventana actual (main window)
    main_window = driver.current_window_handle
    # END --------- CHROME DRIVER CONNECTION                                                                           #
    # ================================================================================================================ #

    # ================================================================================================================ #
    # CLIC EN "Mostrar más" para ver todos los paises del contenedor                                                   #
    # ================================================================================================================ # 
    while True:
        try:
            button = search_button(driver, '#category-left-menu > div > span')
            driver.execute_script("arguments[0].click();", button)
            print('Click on button "Mostrar más (Countries)..."')
            break

        except Exception as e:
            # Obtener el mensaje de la excepción como una cadena
            mensaje_error = str(e)
            # Imprimir solo el mensaje de error
            print("\nError Try (1):", mensaje_error[:150])
            break
    # END --------- CLIC EN "Mostrar más" para ver todos los paises del contenedor                                     #
    # ================================================================================================================ #



    # ================================================================================================================ #
    # OBTENER LINK's DE LIGAS                                                                                          #
    # ================================================================================================================ # 
    # Son cerca de 80 paises registrados en la página
    for i in range (2, 7):
        try:
            # XPATH único de un país en particular
            div_xpath_country = driver.find_element(By.XPATH, f'//*[@id="category-left-menu"]/div/div[{i}]')    
            
            # Obtener el id del div de cada país en particular
            id_country = div_xpath_country.find_element(By.TAG_NAME, 'a').get_attribute('id')

            while True:
                try:
                    # CSS único de cada país
                    css_button = f'#{id_country} > span'

                    # clic en cada país para desplejar sus ligas respectivas
                    button = search_button(driver, css_button)
                    driver.execute_script("arguments[0].click();", button)
                    
                    break

                except Exception as e:
                    # Obtener el mensaje de la excepción como una cadena
                    mensaje_error = str(e)
                    # Imprimir solo el mensaje de error
                    print("\nError Try (3):", mensaje_error[:150])
                    break

            # div con la información del país y sus ligas respectivas ya desplegadas 
            div_css_country = driver.find_element(By.CSS_SELECTOR, f'#category-left-menu > div > div:nth-child({i})')
            
            # Buscar todos los elementos span dentro del div del país con sus ligas. Cada span contine un una liga.
            spans = div_css_country.find_elements(By.TAG_NAME, 'span')     

            # Iterar sobre los elementos span y buscar las etiquetas 'a' dentro de cada uno
            for span in spans:
                # Buscar todos los elementos 'a' dentro del span
                a_tags = span.find_elements(By.TAG_NAME, 'a')

                # Iterar sobre las etiquetas 'a' y accede al atributo 'href' para obtener el link de la liga
                for a_tag in a_tags:

                    try:    
                        link_league = a_tag.get_attribute('href')
                        link_resultados = link_league + 'resultados/'

                        # ================================================================================================ #
                        # ABRI NUEVA PESTAÑA                                                                               #
                        # ================================================================================================ #
                        # Abrir o recargar la página con la url de la liga actual "new_tab_open"
                        # Abrir una segunda ventana o pestaña (puedes hacer clic en un enlace o abrir una nueva URL)                    
                        driver.execute_script(f"window.open('{link_resultados}');")

                        # Cambiar el enfoque a la segunda ventana
                        # Obtén los identificadores de todas las ventanas abiertas
                        ventanas = driver.window_handles

                        # Cambia el enfoque a la segunda ventana (la última en la lista)
                        driver.switch_to.window(ventanas[-1])

                        # ================================================================================================ #
                        # BUSCAR Y DAR CLIC SOBRE EL CSS_SELECTOR DEL BOTÓN                                                #
                        # ================================================================================================ #
                        
                        # Clic sobre el CSS_SELECTOR encontrado dentro de la página.
                        while True:
                            try:
                                button = search_button(driver, '#live-table > div.event.event--results > div > div > a')
                                driver.execute_script("arguments[0].click();", button)
                                print('Click on button "Mostrar más partidos"')

                            except Exception as e:
                                # Obtener el mensaje de la excepción como una cadena
                                mensaje_error = str(e)
                                # Imprimir solo el mensaje de error
                                print("\nError Try (4):", mensaje_error[:150])
                                break                    
                        # END --------- BUSCAR Y DAR CLIC SOBRE EL CSS_SELECTOR DEL BOTÓN                              # # #
                        # ================================================================================================ #
                                        
                        # ================================================================================================ #
                        # GUARDAR DATOS EN LA TABLA links_leagues                                                          #
                        # ================================================================================================ #
                        while True:
                            try:
                                # Generar id único aleatoriamente
                                id_league_ran = randint(1000, 10000)

                                # List a partir de la url de la liga.
                                name_league = link_league.split('/')
                                # Ej: new_tab_open = ['https', '','www.flashscore.co', 'baloncesto', 'italia', 'serie-a2', 'resultados']

                                # Extracción del nombre de la url (de la lista "new_tab_open_split").
                                name_league = f"{name_league[4]} - {name_league[5]}"
                                # Ej: new_name_league = "italia - serie-a2"

                                # Crear objeto del modelo League
                                tb_leagues = League(id_league=id_league_ran, name_league=name_league, link_league=link_league)

                                # Guardar los datos en la tabla de la base de datos
                                tb_leagues.save()

                                print(f"\nSe ha guardado la liga < {tb_leagues.name_league} > correctamente.\n")

                                break
                            
                            except IntegrityError:
                                # Si el id generado ya existe en la tabla, se genera una exception
                                print(f'El id {id_league_ran} ya existe en la base de datos.'
                                    f'\nGenerando un nuevo id...\n')
                        # END --------- GUARDAR DATOS EN LA TABLA links_leagues                                            #
                        # ================================================================================================ #

                    except Exception as e:
                        # Obtener el mensaje de la excepción como una cadena
                        mensaje_error = str(e)
                        # Imprimir solo el mensaje de error
                        print("\nError Try (5):", mensaje_error[:150])
                        continue

                    # Cuando hayas terminado de trabajar en la segunda ventana, puedes cerrarla
                    # Cerrar la segunda ventana
                    driver.close()

                    # Cambiar el enfoque de vuelta a la primera ventana
                    driver.switch_to.window(ventanas[0])
                    # END --------- ABRI NUEVA PESTAÑA                                                                 #
                    # ================================================================================================ #

        except Exception as e:
            # Obtener el mensaje de la excepción como una cadena
            mensaje_error = str(e)
            # Imprimir solo el mensaje de error
            print("\nError Try (6):", mensaje_error[:150])
            continue
    # END --------- OBTENER LINK's DE LIGAS                                                                            #
    # ================================================================================================================ #

    print('FIN...')

    driver.quit()

# catch_data_links()