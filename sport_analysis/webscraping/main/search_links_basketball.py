from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .list_links_del import list_delete_links as del_links
from random import randint
from django.db.utils import IntegrityError
from webscraping.models import League


def msn_exceptions(type_try, e):
    # Obtener el mensaje de la excepción como una cadena
    mensaje_error = str(e)
    # Imprimir solo el mensaje de error
    print(f"\nError Try ({type_try}):", mensaje_error[:150])


def delete_links(dict_links):
    # Obtener la lista de los links a eliminar
    list_delete_links = del_links()
    
    count = 0
    # Iterar sobre las llaves del diccioanrio "dict_links"
    for key, value in list(dict_links.items()): 

        # Si la llave de la iteracción está dentro de la lista, elimianr ese para kkey-value
        if value in list_delete_links:
            del dict_links[key]
            count += 1

    print(f'\nSe eliminaron en total {count} pares key-value del diccionario...')
    
    # Retornar el diccionario modificado 
    return dict_links



def get_links():
    # ================================================================================================================ #
    # CHROME DRIVER CONNECTION                                                                                         #
    # ================================================================================================================ #
    options = webdriver.ChromeOptions()
    options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
    driver_path = "drivers/chromedriver.exe"
    driver = webdriver.Chrome(options=options)#, executable_path=driver_path)
    driver.maximize_window()

        # Abrir la ventana principal
    driver.get('https://www.sofascore.com/basketball')    
    # END --------- CHROME DRIVER CONNECTION                                                                           #
    # ================================================================================================================ #

    # ================================================================================================================ #
    # ITERAR SOBRE LOS PAISES                                                                                          #
    # ================================================================================================================ #         
    # Iterar sobre cada país
    # for i_country in range(1, 64, 1):
    dict_links = {}
    i_country = 1
    while True:
    # for i in range(3):
        try:
            # CSS de cada país
            css_contries = '#__next > main > div > div.sc-hLBbgP.sc-eDvSVe.gjJmZQ.fEHohf.sc-836c558d-1.eDNgWX > div.sc'\
                           '-hLBbgP.bMQfbT.sc-836c558d-2.leSghq > div.sc-hLBbgP.dRtNhU > div > div.sc-hLBbgP.gRCqqZ > '\
                            f'a:nth-child({i_country}) > div > img'  

            try:
                # Clic sobre cada país para abirir sus respectivas ligas    
                # div_countries = driver.find_element(By.CSS_SELECTOR, css_contries)
                div_countries = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_contries)))
                div_countries.click()

            except:
                print('\nSe terminaron los paises u ocurrió un erro al acceder a un país...')
                break

            # CSS  del contenedor de las ligas de un país específico
            css_div_link = '#__next > main > div > div.sc-hLBbgP.sc-eDvSVe.gjJmZQ.fEHohf.sc-836c558d-1.eDNgWX > div.sc'\
                           '-hLBbgP.bMQfbT.sc-836c558d-2.leSghq > div.sc-hLBbgP.dRtNhU > div > div.sc-hLBbgP.gRCqqZ > '\
                            'div'
            
            # Captar la información del contenedor de ligas
            div_links_leagues = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_div_link)))

            # ======================================================================================================== #
            # ITERAR SOBRE CADA LINK DEL PAÍS                                                                          #
            # ======================================================================================================== #
            # Buscar todos los elementos <a> dentro del div del país con sus ligas. Cada <a> contine info de una liga.
            a_tags = div_links_leagues.find_elements(By.TAG_NAME, 'a')
            
            # Eliminar el últmio registro. Este contiene la url general del país y no de una liga en particular
            del a_tags[-1]            

            # Máximo 2 ligas por cada país (las más importantes)
            for a_tag in a_tags:        
                try:
                    # String con la url de la liga
                    link_league = a_tag.get_attribute('href')

                    # List a partir de la url de la liga.
                    name_league = link_league.split('/')
                    # Ej: new_tab_open = ['https:', '', 'www.sofascore.com', 'tournament', 'basketball', 'argentina', 
                    # 'super-20', '10701']

                    # Extracción del nombre de la url (de la lista "new_tab_open_split").
                    name_league = f"{name_league[5]} - {name_league[6]}"
                    # Ej: new_name_league = "italia - serie-a2"

                    dict_links[name_league] = link_league

                except Exception as e:
                    msn_exceptions(type_try='2', e=e)    

            # Clic para cerrar el contenedor de ligas 
            div_countries.click()


            i_country += 1

        except Exception as e:
            print(f'\nError en "i_country": {i_country}')
            msn_exceptions(type_try='1', e=e)    


    # Se elimina 140 url's que no cuentan con información y/o estructura relevante
    dict_links_final = delete_links(dict_links=dict_links)

    # ================================================================================================ #
    # GUARDAR DATOS EN LA TABLA "leagues"                                                              #
    # ================================================================================================ #
    for name, link in dict_links_final.items():
        # 5 Intentos para almacenar los datos en la db
        for i_db_leagues in range(5):
            try:
                # Generar id único aleatoriamente
                id_league_ran = randint(1000, 10000)

                # Crear objeto del modelo League
                tb_leagues = League(id_league=id_league_ran, name_league=name, link_league=link)

                # Guardar los datos en la tabla de la base de datos
                tb_leagues.save()                

                print(f"\nSe ha guardado la liga < {tb_leagues.name_league} > correctamente...")

                break
            
            except IntegrityError:
                # Si el id generado ya existe en la tabla, se genera una exception
                print(f'\nEl id {id_league_ran} ya existe en la base de datos.'
                        f'\nGenerando un nuevo id...')
        # END --------- GUARDAR DATOS EN LA TABLA "Leagues"                                                #
        # ================================================================================================ #

