import os
import pandas as pd


class TemplateInfoToSendToDB():

        def __init__(self):
                
                # Obtener la ruta a la carpeta "NBA" en el escritorio del pc. Este es un atributo "privado"
                self.__desktop_nba_path = os.path.join(os.path.expanduser("~"), "Desktop/NBA")

                # Referencia el número del archivo .csv ha crear
                self.num_folder = None

                # Plantilla del formato para guardar temporalmente la información
                self.dict_db_nba = {
                                        # Table "teams" de la database
                                        'teams': {
                                                        # 'idteams': [],          # Primaty Key principal de toda la db
                                                        'name_team': [],
                                                 },
                                        # Table "matches" de la database
                                        'matches': {                                                        
                                                        # 'idmatches': [],        # Primaty Key secundaria de toda la db
                                                        'season': None, 
                                                        'date_match': [], 
                                                        'is_overtime': [], 
                                                        # 'teams_idteams': None,  # teams_idteams = teams.idteams
                                                   },
                                        # Table "top_players" de la database
                                        'top_players': {
                                                                'name_player': [],
                                                                'position': [],
                                                                'points': [],
                                                                'rebounds': [],
                                                                'assists': [],
                                                                # 'team_stats_matches_idmatches': None,   # team_stats_matches_idmatches = matches.idmatches
                                                                # 'team_stats_matches_teams_idteams': None,   # team_stats_Zmatches_teams_idteams = teams.idteams
                                                        },              
                                        # Table "team_stats" de la database
                                        'team_stats': {                
                                                                'name_team': [],                 
                                                                'is_home': [],                 
                                                                'total_points': [],                 
                                                                'q1': [],                  
                                                                'q2': [],                  
                                                                'q3': [],                  
                                                                'q4': [],  
                                                                # 'matches_idmatches': None,  # matches_idmatches = matches.idmatches
                                                                # 'matches_teams_idteams': None,  # matches_teams_idteams = teams.idteams
                                                     },              
                                        # Table "stats_per_quarter" de la database
                                        'stats_per_quarter':{                  
                                                                        'num_q': (1, 2, 3, 4),      # 4 cuartos de juego   
                                                                        # ...
                                                                        # 'Free throws': [],                  
                                                                        # ...
                                                                        # 'team_stats_matches_idmatches': None,   # team_stats_matches_idmatches = matches.idmatches
                                                                        # 'team_stats_matches_teams_idteams': None,   # team_stats_matches_teams_idteams = teams idteams
                                                            }
                                        }



def create_folder_and_csv(self):

        try:
                # Nombre de la carpeta a crear si no existe
                folder_name_1 = f'season {self.dict_db_nba["matches"]["season"][0]}'
                folder_name_complete = folder_name_1 + f'/{self.num_folder}'
                
                list_folders = list(folder_name_1, folder_name_complete)

                for i_create_folder in range(2):
                        # Ruta completa de la carpeta
                        folder_path = os.path.join(self.__desktop_nba_path, list_folders[i_create_folder])

                        # Verificar si la carpeta ya existe
                        if not os.path.exists(folder_path):
                                # Crear la carpeta si no existe
                                os.makedirs(folder_path)
                                print(f"Folder '{folder_name_1}' created on Desktop.")
                        else:
                                print(f"There is a folder '{folder_name_1}' on Desktop.")
                
                folder_path_complete = os.path.join(self.__desktop_nba_path, folder_name_complete)

        except:
                print('\nActivated EXCEPTIONE: Problema al crear folder...!')

        try:
                # Iterar sobre las claves del diccionario y crea un archivo CSV por cada sub-diccionario
                # file = claves del diccionario
                # data = valores del diccionario
                for file, data in self.dict_db_nba.items():
                        df = pd.DataFrame(data)
                        folder_path_file = os.path.join(folder_path_complete, f'{file}.csv')
                        df.to_csv(folder_path_file, index=False,encoding='utf-8')

                print('Se han creado con exito los archivos .csv actuales')


        except Exception as e:
                print('\nActivated EXCEPTIONE: ¿Data Frame vacío?...!')

        

                
def set_info_players_in_dict_team():
        pass

def get_dict_teams():
        pass
