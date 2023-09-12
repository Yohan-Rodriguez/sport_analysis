
def get_key_value(xpath_temp, key_rx, i_match):
    
    dict_xpath_s = None
    xpath_temp = xpath_temp

    if xpath_temp == 0:
        dict_xpath_s = {   
                        'ft':       f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/div/span[1]/span',
                        'date':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/span',
                        'home':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[1]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[1]/div/span[1]',                                    
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[2]/div/span[1]',
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[4]/div/span[1]',
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[1]/span[1]',
                        'away':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[2]/div',                                    
                        'q1_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[1]/div/span[1]',
                        'q2_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[2]/div/span[1]',
                        'q3_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[3]/div/span[1]',
                        'q4_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[4]/div/span[1]',
                        'total_a':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[2]/span[1]',
                    }  
                        
    elif xpath_temp == 1:
        dict_xpath_s = {   
                        'ft':       f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/div/span[1]/span',
                        'date':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/span',  
                        'home':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[1]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[1]/div/span[1]',
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[2]/div/span[1]',
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[4]/div/span[1]',
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[1]/span[1]',
                        'away':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[2]/div',
                        'q1_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[1]/div/span[1]',
                        'q2_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[2]/div/span[1]',
                        'q3_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[3]/div/span[1]',
                        'q4_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[4]/div/span[1]',
                        'total_a':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[2]/span[1]',
                    }
                        
        
    elif xpath_temp == 2:
        dict_xpath_s = {   
                        'ft':       f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/div/span[1]/span',
                        'date':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/span',  
                        'home':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[1]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[1]/div/span[1]',
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[2]/div/span[1]',  
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[4]/div/span[1]',  
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[1]/span[1]',
                        'away':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[2]/div',
                        'q1_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[1]/div/span[1]',
                        'q2_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[2]/div/span[1]',
                        'q3_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[3]/div/span[1]',  
                        'q4_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[4]/div/span[1]',  
                        'total_a':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[2]/span[1]',
                    }
    
    elif xpath_temp == 3:
        dict_xpath_s = {   
                        'ft':       f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/div/span[1]/span',
                        'date':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/span',  
                        'home':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[1]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[1]/div/span[1]',
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[2]/div/span[1]',  
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[4]/div/span[1]',  
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[1]/span[1]',
                        'away':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[2]/div',
                        'q1_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[1]/div/span[1]',
                        'q2_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[2]/div/span[1]',  
                        'q3_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[3]/div/span[1]',
                        'q4_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[4]/div/span[1]',  
                        'total_a':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[2]/span[1]',
                    }
        
    elif xpath_temp == 4:
        dict_xpath_s = {
                        'ft':       f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[6]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/div/span[1]/span',
                        'date':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[6]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/span',
                        'home':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[1]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[1]/div/span[1]',
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[2]/div/span[1]',
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[4]/div/span[1]',
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[1]/span[1]',
                        'away':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[2]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[1]/div/span[1]',
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[2]/div/span[1]',
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[4]/div/span[1]',
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[2]/span[1]',
                       }
        
    elif xpath_temp == 5:
        dict_xpath_s = {
                        'ft':       f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/div/span[1]/span',
                        'date':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/span',
                        'home':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[1]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[1]/div/span[1]',                                      
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[2]/div/span[1]',
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[4]/div/span[1]',
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[1]/span[1]',
                        'away':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[2]/div',
                        'q1_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[1]/div/span[1]',
                        'q2_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[2]/div/span[1]',
                        'q3_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[3]/div/span[1]',
                        'q4_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[4]/div/span[1]',
                        'total_a':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[2]/span[1]',
                       }
    
    elif xpath_temp == 6:
        dict_xpath_s = {
                        'ft':       f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/div/span[1]/span',
                        'date':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/span',
                        'home':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[1]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[1]/div/span[1]',
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[2]/div/span[1]',
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[4]/div/span[1]',
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[1]/span[1]',
                        'away':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[2]/div',
                        'q1_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[1]/div/span[1]',
                        'q2_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[2]/div/span[1]',
                        'q3_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[3]/div/span[1]',
                        'q4_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[4]/div/span[1]',
                        'total_a':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[2]/span[1]',
                       }
    
    elif xpath_temp == 7:
        dict_xpath_s = {
                        'ft':       f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/div/span[1]/span',
                        'date':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/span',
                        'home':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[1]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[1]/div/span[1]',
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[2]/div/span[1]',
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[4]/div/span[1]',
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[1]/span[1]',
                        'away':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[2]/div',
                        'q1_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[1]/div/span[1]',
                        'q2_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[2]/div/span[1]',
                        'q3_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[3]/div/span[1]',
                        'q4_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[4]/div/span[1]',
                        'total_a':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[2]/span[1]',
                       }
    
    elif xpath_temp == 8:
        dict_xpath_s = {
                        'ft':       f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[2]/div/span[1]/span',
                        'date':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[2]/span',
                        'home':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[1]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[1]/div/span[1]',
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[2]/div/span[1]',
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[4]/div/span[1]',
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[1]/span[1]',
                        'away':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[2]/div',
                        'q1_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[1]/div/span[1]',
                        'q2_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[2]/div/span[1]',
                        'q3_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[3]/div/span[1]',
                        'q4_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[4]/div/span[1]',
                        'total_a':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[2]/span[1]',
                       }
    
    elif xpath_temp == 9:
        dict_xpath_s = {
                        'ft':       f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/div/span[1]/span',
                        'date':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/span',
                        'home':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[1]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[1]/div/span[1]',
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[2]/div/span[1]',
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[4]/div/span[1]',
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[1]/span[1]',
                        'away':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[2]/div',
                        'q1_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[1]/div/span[1]',
                        'q2_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[2]/div/span[1]',
                        'q3_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[3]/div/span[1]',
                        'q4_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[4]/div/span[1]',
                        'total_a':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[2]/span[1]',
                       }
    
    elif xpath_temp == 10:
        dict_xpath_s = {
                        'ft':       f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/div/span[1]/span',
                        'date':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/span',
                        'home':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[1]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[1]/div/span[1]',
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[2]/div/span[1]',
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[1]/div[4]/div/span[1]',
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[1]/span[1]',
                        'away':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[1]/div[2]/div',
                        'q1_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[1]/div/span[1]',
                        'q2_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[2]/div/span[1]',
                        'q3_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[3]/div/span[1]',
                        'q4_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[3]/div[2]/div[4]/div/span[1]',
                        'total_a':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[4]/div/div[4]/div[2]/span[1]',
                       }
    
    elif xpath_temp == 11:
        dict_xpath_s = {
                        'ft':       f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/div/span[1]/span',
                        'date':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[{i_match}]/a/div/div/div[2]/span',
                        'home':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[4]/div/div[1]/div[1]/div',
                        'q1_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[4]/div/div[3]/div[1]/div[1]/div/span[1]',
                        'q2_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[4]/div/div[3]/div[1]/div[2]/div/span[1]',
                        'q3_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[4]/div/div[3]/div[1]/div[3]/div/span[1]',
                        'q4_h':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[4]/div/div[3]/div[1]/div[4]/div/span[1]',
                        'total_h':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[4]/div/div[4]/div[1]/span[1]',
                        'away':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[4]/div/div[1]/div[2]/div',
                        'q1_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[4]/div/div[3]/div[2]/div[1]/div/span[1]',
                        'q2_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[4]/div/div[3]/div[2]/div[2]/div/span[1]',
                        'q3_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[4]/div/div[3]/div[2]/div[3]/div/span[1]',
                        'q4_a':     f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[4]/div/div[3]/div[2]/div[4]/div/span[1]',
                        'total_a':  f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[4]/div/div[4]/div[2]/span[1]',
                       }        
        
    else:
        dict_xpath_s = {key_rx: None}
    
    return dict_xpath_s[key_rx]



def get_xpath_button_previous():
    xpath_previous =    [
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[7]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[8]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[16]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[6]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[15]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[10]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/button',
                        ]
    
    return xpath_previous



def get_div_container_button_season():
    list_xpath_div = [
                        '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div',
                     ] 
    
    return list_xpath_div
