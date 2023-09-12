

dict_teams = {
          'Team': {
                      # Lista de jugadores (Nombre, posición y edad)
                      'Players': [{'Name': None, 'Position': None, 'Age': None},
                                  {'Name': None, 'Position': None, 'Age': None},
                                  {'Name': None, 'Position': None, 'Age': None}],

                      # Lista de jugadores sobresalientes en:
                      # Points: Avg puntos por partidos,
                      # Rebounds: Avg de rebotes por partido,
                      # Assisrs: Avg de asistencias por partido.
                      # Minutes_Per_Game: Avg de minutos jugados por partido
                      'Top_Players': [{'Points': None, 'Rebounds': None, 'Assists': None, 'Minutes_Per_Game': None,},
                                      {'Points': None, 'Rebounds': None, 'Assists': None, 'Minutes_Per_Game': None,},
                                      {'Points': None, 'Rebounds': None, 'Assists': None, 'Minutes_Per_Game': None,}],

                      # Puntos de los equipos de cada partido
                      'Matches': [{'Date': None, 'Is_Home': None, 'Name_Vs': None, 'Q1_H': None,'Q2_H': None,'Q3_H': None,
                                   'Q4_H': None, 'Final_Points_H': None, 'Q1_A': None,'Q2_A': None,'Q3_A': None,
                                   'Q4_A': None, 'Final_Points_A': None, 'OT': None, 'Is_Win': None, 'Id_Statistics_Match': None}]
                  },
      }

dict_statistics_matches = {
                        # Id de las estadisticas para asociarlo a los dos equipos correspondintes del partido
                        'Id_Statistics_Match': None,

                        'Points_Per_Minute_Quarter': {
                                                        'FT': [{'min:seg': None, 'Points_H': None, 'Points_A': None}],
                                                        'Q3': [{'min:seg': None, 'Points_H': None, 'Points_A': None}],
                                                        'Q2': [{'min:seg': None, 'Points_H': None, 'Points_A': None}],
                                                        'Q1': [{'min:seg': None, 'Points_H': None, 'Points_A': None}],
                                                     },

                        'Statistics': {
                                        'All': {'Free_Throws': None, '2_Pointers': None, '3_Pointers': None, 'Field_Goals': None,
                                                'Rebounds': None, 'Defensive_Rebounds': None, 'Offensive_Rebounds': None,
                                                'Assists': None, 'Turnovers': None, 'Steals': None, 'Blocks': None, 'Fouls': None,
                                                'Max_Points_In_A_Raw': None, 'Time spent in lead': None, 'Biggest_Lead': None},

                                        'Q1': {'Free_Throws': None, '2_Pointers': None, '3_Pointers': None, 'Field_Goals': None,
                                                'Rebounds': None, 'Defensive_Rebounds': None, 'Offensive_Rebounds': None,
                                                'Assists': None, 'Turnovers': None, 'Steals': None, 'Blocks': None, 'Fouls': None,
                                                'Time_Spent_In_Lead': None, 'Biggest_Lead': None},

                                        'Q2': {'Free_Throws': None, '2_Pointers': None, '3_Pointers': None, 'Field_Goals': None,
                                                'Rebounds': None, 'Defensive_Rebounds': None, 'Offensive_Rebounds': None,
                                                'Assists': None, 'Turnovers': None, 'Steals': None, 'Blocks': None, 'Fouls': None,
                                                'Time_Spent_In_Lead': None, 'Biggest_Lead': None},

                                        'Q3': {'Free_Throws': None, '2_Pointers': None, '3_Pointers': None, 'Field_Goals': None,
                                                'Rebounds': None, 'Defensive_Rebounds': None, 'Offensive_Rebounds': None,
                                                'Assists': None, 'Turnovers': None, 'Steals': None, 'Blocks': None, 'Fouls': None,
                                                'Time_Spent_In_Lead': None, 'Biggest_Lead': None},

                                        'Q4': {'Free_Throws': None, '2_Pointers': None, '3_Pointers': None, 'Field_Goals': None,
                                                'Rebounds': None, 'Defensive_Rebounds': None, 'Offensive_Rebounds': None,
                                                'Assists': None, 'Turnovers': None, 'Steals': None, 'Blocks': None, 'Fouls': None,
                                                'Time_Spent_In_Lead': None, 'Biggest_Lead': None},
                                      },
                      }


def set_name_dict_team(name_team):
    
    #
    dict_teams[name_team] = {'Players': [], 'Top_Players': [], 'Matches': []}


def set_info_players_in_dict_team(name_team, dict_info_player, key_dict):
    
    #
    dict_teams[name_team][key_dict].append(dict_info_player)


def get_dict_teams():
    return dict_teams