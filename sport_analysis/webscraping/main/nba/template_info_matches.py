import os
import copy
import pandas as pd


class TemplateInfoMatches():

        def __init__(self):
                
                # Obtener la ruta a la carpeta "NBA" en el escritorio del pc. Este es un atributo "privado"
                self.__desktop_nba_path = os.path.join(os.path.expanduser("~"), "Desktop/NBA")

                # 
                self.current_season = None
                
                # Valor a usar para la creación del archivo .csv 
                # con el valor del # de clics dados sobre una la sesión especifica
                self.count_click_on_previous = None

                # Plantilla del formato para guardar temporalmente la información
                self.dict_db_nba = {
                                        # Table "teams" de la database
                                        'teams': [], 
                                                # 'idteams': [],          # Primaty Key principal de toda la db
                                                
                                        
                                        'matches': {},
                }

                self.dict_db_nba_match = {
                                          # General Data
                                          'is_overtime': [],
                                          'date_match': [],
                                          
                                          # General Data Home
                                          'n_home': [],
                                          'h_total_points': [],
                                          'h_q1': [],
                                          'h_q2': [],
                                          'h_q3': [],
                                          'h_q4': [],
                                          
                                          # General Data Away
                                          'n_away': [],
                                          'a_total_points': [],
                                          'a_q1': [],
                                          'a_q2': [],
                                          'a_q3': [],
                                          'a_q4': [],
                                          
                                          # Top Players Home
                                          'h_tp1_name_player': [],
                                          'h_tp1_position': [],
                                          'h_tp1_points': [],
                                          'h_tp1_rebounds': [],
                                          'h_tp1_assists': [],
                                          'h_tp2_name_player': [],
                                          'h_tp2_position': [],
                                          'h_tp2_points': [],
                                          'h_tp2_rebounds': [],
                                          'h_tp2_assists': [],
                                          'h_tp3_name_player': [],
                                          'h_tp3_position': [],
                                          'h_tp3_points': [],
                                          'h_tp3_rebounds': [],
                                          'h_tp3_assists': [],
                                          
                                          # Top Players Away
                                          'a_tp1_name_player': [],
                                          'a_tp1_position': [],
                                          'a_tp1_points': [],
                                          'a_tp1_rebounds': [],
                                          'a_tp1_assists': [],
                                          'a_tp2_name_player': [],
                                          'a_tp2_position': [],
                                          'a_tp2_points': [],
                                          'a_tp2_rebounds': [],
                                          'a_tp2_assists': [],
                                          'a_tp3_name_player': [],
                                          'a_tp3_position': [],
                                          'a_tp3_points': [],
                                          'a_tp3_rebounds': [],
                                          'a_tp3_assists': [],
                                          
                                          # General Data Q1
                                          'h_q1_Free throws': [],
                                          'a_q1_Free throws': [],
                                          'h_q1_2 pointers': [],
                                          'a_q1_2 pointers': [],
                                          'h_q1_3 pointers': [],
                                          'a_q1_3 pointers': [],
                                          'h_q1_Field goals': [],
                                          'a_q1_Field goals': [],
                                          'h_q1_Defensive rebounds': [],
                                          'a_q1_Defensive rebounds': [],
                                          'h_q1_Offensive rebounds': [],
                                          'a_q1_Offensive rebounds': [],
                                          'h_q1_Assists': [],
                                          'a_q1_Assists': [],
                                          'h_q1_Turnovers': [],
                                          'a_q1_Turnovers': [],
                                          'h_q1_Steals': [],
                                          'a_q1_Steals': [],
                                          'h_q1_Blocks': [],
                                          'a_q1_Blocks': [],
                                          'h_q1_Fouls': [],
                                          'a_q1_Fouls': [],
                                          'h_q1_Time spent in lead': [],
                                          'a_q1_Time spent in lead': [],
                                          'h_q1_Biggest lead': [],
                                          'a_q1_Biggest lead': [],
                                          
                                          # General Data Q2
                                          'h_q2_Free throws': [],
                                          'a_q2_Free throws': [],
                                          'h_q2_2 pointers': [],
                                          'a_q2_2 pointers': [],
                                          'h_q2_3 pointers': [],
                                          'a_q2_3 pointers': [],
                                          'h_q2_Field goals': [],
                                          'a_q2_Field goals': [],
                                          'h_q2_Defensive rebounds': [],
                                          'a_q2_Defensive rebounds': [],
                                          'h_q2_Offensive rebounds': [],
                                          'a_q2_Offensive rebounds': [],
                                          'h_q2_Assists': [],
                                          'a_q2_Assists': [],
                                          'h_q2_Turnovers': [],
                                          'a_q2_Turnovers': [],
                                          'h_q2_Steals': [],
                                          'a_q2_Steals': [],
                                          'h_q2_Blocks': [],
                                          'a_q2_Blocks': [],
                                          'h_q2_Fouls': [],
                                          'a_q2_Fouls': [],
                                          'h_q2_Time spent in lead': [],
                                          'a_q2_Time spent in lead': [],
                                          'h_q2_Biggest lead': [],
                                          'a_q2_Biggest lead': [],
                                          
                                          # General Data Q3
                                          'h_q3_Free throws': [],
                                          'a_q3_Free throws': [],
                                          'h_q3_2 pointers': [],
                                          'a_q3_2 pointers': [],
                                          'h_q3_3 pointers': [],
                                          'a_q3_3 pointers': [],
                                          'h_q3_Field goals': [],
                                          'a_q3_Field goals': [],
                                          'h_q3_Defensive rebounds': [],
                                          'a_q3_Defensive rebounds': [],
                                          'h_q3_Offensive rebounds': [],
                                          'a_q3_Offensive rebounds': [],
                                          'h_q3_Assists': [],
                                          'a_q3_Assists': [],
                                          'h_q3_Turnovers': [],
                                          'a_q3_Turnovers': [],
                                          'h_q3_Steals': [],
                                          'a_q3_Steals': [],
                                          'h_q3_Blocks': [],
                                          'a_q3_Blocks': [],
                                          'h_q3_Fouls': [],
                                          'a_q3_Fouls': [],
                                          'h_q3_Time spent in lead': [],
                                          'a_q3_Time spent in lead': [],
                                          'h_q3_Biggest lead': [],
                                          'a_q3_Biggest lead': [],
                                          
                                          # General Data Q4
                                          'h_q4_Free throws': [],
                                          'a_q4_Free throws': [],
                                          'h_q4_2 pointers': [],
                                          'a_q4_2 pointers': [],
                                          'h_q4_3 pointers': [],
                                          'a_q4_3 pointers': [],
                                          'h_q4_Field goals': [],
                                          'a_q4_Field goals': [],
                                          'h_q4_Defensive rebounds': [],
                                          'a_q4_Defensive rebounds': [],
                                          'h_q4_Offensive rebounds': [],
                                          'a_q4_Offensive rebounds': [],
                                          'h_q4_Assists': [],
                                          'a_q4_Assists': [],
                                          'h_q4_Turnovers': [],
                                          'a_q4_Turnovers': [],
                                          'h_q4_Steals': [],
                                          'a_q4_Steals': [],
                                          'h_q4_Blocks': [],
                                          'a_q4_Blocks': [],
                                          'h_q4_Fouls': [],
                                          'a_q4_Fouls': [],
                                          'h_q4_Time spent in lead': [],
                                          'a_q4_Time spent in lead': [],
                                          'h_q4_Biggest lead': [],
                                          'a_q4_Biggest lead': []
                                          }
               
                # Lista con las claves del diccionario dict_db_nba_match 
                self.list_keys_match = list(self.dict_db_nba_match.keys())
                
                # Atributo - copia de self.dict_db_nba_match
                self.dict_db_nba_match_original = self.dict_db_nba_match.copy()


        def restart_dict_db_nba_match(self):
                self.dict_db_nba_match = self.dict_db_nba_match_original



        def create_folder_and_csv(self):

                try:
                        # Nombre de la carpeta a crear si no existe
                        # folder_name = f'season {self.dict_db_nba["season"]}'
                        folder_name_complete = f'season {self.current_season}'
                        # folder_name_complete = folder_name + f'/{self.num_folder}'
                        
                        # list_folders = list(folder_name, folder_name_complete)

                        # Ruta completa de la carpeta
                        folder_path = os.path.join(self.__desktop_nba_path, folder_name_complete)

                        # Verificar si la carpeta ya existe
                        if not os.path.exists(folder_path):
                                # Crear la carpeta si no existe
                                os.makedirs(folder_path)
                                print(f"Folder '{folder_name_complete}' created on Desktop.")
                        else:
                                print(f"There is a folder '{folder_name_complete}' on Desktop.")

                except:
                        print('\nActivated EXCEPTIONE: Problema al crear folder...!')

                try:
                        # Iterar sobre las claves del diccionario y crea un archivo CSV por cada sub-diccionario
                        # file = claves del diccionario
                        # data = valores del diccionario

                        df = pd.DataFrame(self.dict_db_nba_match)
                        # Nombre del archivo a crear
                        folder_path_file = os.path.join(folder_path, f'{self.count_click_on_previous-1}.csv')
                        df.to_csv(folder_path_file, index=False, encoding='utf-8')

                        # for file, data in self.dict_db_nba['matches'].items():
                        #         df = pd.DataFrame(data)
                        #         # Nombre del archivo a crear
                        #         folder_path_file = os.path.join(folder_path, f'{file}.csv')
                        #         df.to_csv(folder_path_file, index=False, encoding='utf-8')

                        print('Se ha creado con exito el archivo .csv actual')


                except Exception as e:
                        print('\nActivated EXCEPTIONE: ¿Data Frame vacío?...!')
