import os
import pandas as pd


class TemplateInfoToSendToDB():

        def __init__(self):
                
                # Obtener la ruta a la carpeta "NBA" en el escritorio del pc. Este es un atributo "privado"
                self.__desktop_nba_path = os.path.join(os.path.expanduser("~"), "Desktop/NBA")

                # Referencia el número del archivo .csv ha crear
                self.num_folder = None

                # 
                self.current_season = None

                # Plantilla del formato para guardar temporalmente la información
                self.dict_db_nba = {
                                        # Table "teams" de la database
                                        'teams': [], 
                                                # 'idteams': [],          # Primaty Key principal de toda la db
                                                
                                        
                                        'matches': {},
                }

                self.dict_db_nba_match = {
                                                # 'idmatches': [],        # Primaty Key secundaria de toda la db
                                                'date_match': None, 
                                                'n_home': None,
                                                'n_away': None,
                                                'is_overtime': None, 

                                                'team_stats_home': None,
                                                'team_stats_away': None,


                }

                # Estadísticas equipo Local
                self.dict_db_nba_stats_h = {              
                                                        # id_stats             
                                                        'is_home': 1,                 
                                                        'total_points': None,                 
                                                        'q1': None,                  
                                                        'q2': None,                  
                                                        'q3': None,                  
                                                        'q4': None,  
                                                        
                                                        'stats_q': {                                                                
                                                                        'stats_q1': {},
                                                                        'stats_q2': {},
                                                                        'stats_q3': {},
                                                                        'stats_q4': {},
                                                                        # 'stats_q1': { 'Free throws': None, },                                                                        
                                                        },
                                                        
                                                        'top_players': {
                                                                                'player_1': {'name_player': None, 'position': None, 'points': None, 
                                                                                              'rebounds': None, 'assists': None,
                                                                                            },    
                                                                                'player_2': {'name_player': None, 'position': None, 'points': None, 
                                                                                              'rebounds': None, 'assists': None,
                                                                                            },    
                                                                                'player_3': {'name_player': None, 'position': None, 'points': None, 
                                                                                              'rebounds': None, 'assists': None,
                                                                                            },    
                                                        },              
                } 


                # Estadísticas equipo visitante
                self.dict_db_nba_stats_a = self.dict_db_nba_stats_h

                # 
                self.dict_db_nba_match_original = self.dict_db_nba_match
                self.dict_db_nba_stats_h_original = self.dict_db_nba_stats_h
                self.dict_db_nba_stats_a_original = self.dict_db_nba_stats_a


        def restart_dict_db_nba_match(self):
                self.dict_db_nba_match = self.dict_db_nba_match_original

        def restart_dict_db_nba_stats(self):
                self.dict_db_nba_stats_h = self.dict_db_nba_stats_h_original
                self.dict_db_nba_stats_a = self.dict_db_nba_stats_a_original



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
                        for file, data in self.dict_db_nba['matches'].items():
                                df = pd.DataFrame(data)
                                # Nombre del archivo a crear
                                folder_path_file = os.path.join(folder_path, f'{file}.csv')
                                df.to_csv(folder_path_file, index=False, encoding='utf-8')

                        print('Se han creado con exito los archivos .csv actuales')


                except Exception as e:
                        print('\nActivated EXCEPTIONE: ¿Data Frame vacío?...!')

        

                
def set_info_players_in_dict_team():
        pass

def get_dict_teams():
        pass
