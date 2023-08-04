
def get_key_value(xpath_temp, key_rx, i_match):
    
    dict_xpath_s = None

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
                        'ft':       f'',
                        'date':     f'',
                        'home':     f'',
                        'q1_h':     f'',
                        'q2_h':     f'',
                        'q3_h':     f'',
                        'q4_h':     f'',
                        'total_h':  f'',
                        'away':     f'',
                        'q1_h':     f'',
                        'q2_h':     f'',
                        'q3_h':     f'',
                        'q4_h':     f'',
                        'total_h':  f'',
                       }

    else:
        dict_xpath_s = {key_rx: None}
    
    return dict_xpath_s[key_rx]



def get_div_container_button_season():
    list_xpath_div = [
                        '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div',
                     ] 
    
    return list_xpath_div



def get_xpath_button_previous():
    xpath_previous =    [
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div/div[2]/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div[1]/div[1]/button',
                            '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[9]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/button',                            
                        ]
    
    return xpath_previous


# FT
#__next > main > div > div.fresnel-container.fresnel-greaterThanOrEqual-mdMin > div > div.sc-fqkvVR.sc-dcJsrY.gBgQbz.hNspbb.sc-836c558d-1.iOpidl > div.sc-fqkvVR.eeeBnr.sc-836c558d-2.blpTeR > div:nth-child(5) > div > div.sc-jlZhew.kgghii > div > div > div.sc-fqkvVR.kXwmsa > div > div.sc-fqkvVR.clkedU > div:nth-child(10) > a > div > div > div.sc-fqkvVR.fEdaXl > div > span.sc-jEACwC.kUrmQh.currentScore > span
# //*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div[10]/a/div/div/div[2]/div/span[1]/span

#__next > main > div > div.fresnel-container.fresnel-greaterThanOrEqual-mdMin > div > div.sc-fqkvVR.sc-dcJsrY.gBgQbz.hNspbb.sc-836c558d-1.iOpidl > div.sc-fqkvVR.eeeBnr.sc-836c558d-2.blpTeR > div:nth-child(5) > div > div.sc-jlZhew.kgghii > div > div > div.sc-fqkvVR.kXwmsa > div > div.sc-fqkvVR.clkedU > div:nth-child(9) > a > div > div > div.sc-fqkvVR.fEdaXl > div > span.sc-jEACwC.kUrmQh.currentScore > span


# Date
#__next > main > div > div.fresnel-container.fresnel-greaterThanOrEqual-mdMin > div > div.sc-fqkvVR.sc-dcJsrY.gBgQbz.hNspbb.sc-836c558d-1.iOpidl > div.sc-fqkvVR.eeeBnr.sc-836c558d-2.blpTeR > div:nth-child(5) > div > div.sc-jlZhew.kgghii > div > div > div.sc-fqkvVR.kXwmsa > div > div.sc-fqkvVR.clkedU > div:nth-child(10) > a > div > div > div.sc-fqkvVR.fEdaXl > span
#__next > main > div > div.fresnel-container.fresnel-greaterThanOrEqual-mdMin > div > div.sc-fqkvVR.sc-dcJsrY.gBgQbz.hNspbb.sc-836c558d-1.iOpidl > div.sc-fqkvVR.eeeBnr.sc-836c558d-2.blpTeR > div:nth-child(5) > div > div.sc-jlZhew.kgghii > div > div > div.sc-fqkvVR.kXwmsa > div > div.sc-fqkvVR.clkedU > div:nth-child(9) > a > div > div > div.sc-fqkvVR.fEdaXl > span

# Home
#__next > main > div > div.fresnel-container.fresnel-greaterThanOrEqual-mdMin > div > div.sc-fqkvVR.sc-dcJsrY.gBgQbz.hNspbb.sc-836c558d-1.iOpidl > div.sc-fqkvVR.eeeBnr.sc-836c558d-2.blpTeR > div:nth-child(5) > div > div.sc-jlZhew.kgghii > div > div > div.sc-fqkvVR.kXwmsa > div > div.sc-fqkvVR.clkedU > div:nth-child(10) > a > div > div > div.sc-fqkvVR.dOBKtv > div > div.sc-fqkvVR.kiamWz > div.sc-fqkvVR.sc-dcJsrY.ljIAAI.fFmCDf > div

# Away
#__next > main > div > div.fresnel-container.fresnel-greaterThanOrEqual-mdMin > div > div.sc-fqkvVR.sc-dcJsrY.gBgQbz.hNspbb.sc-836c558d-1.iOpidl > div.sc-fqkvVR.eeeBnr.sc-836c558d-2.blpTeR > div:nth-child(5) > div > div.sc-jlZhew.kgghii > div > div > div.sc-fqkvVR.kXwmsa > div > div.sc-fqkvVR.clkedU > div:nth-child(10) > a > div > div > div.sc-fqkvVR.dOBKtv > div > div.sc-fqkvVR.kiamWz > div.sc-fqkvVR.sc-dcJsrY.gBgQbz.fFmCDf > div




# def store_css(css_temp, key_rx, i_match, str_change=''):
#    # Retornar el "value" de la key solicitada "key_rx"
#    this_dict_csss = get_dict(css_temp=css_temp, i_match=i_match, str_change=str_change)
#    return this_dict_csss[key_rx]



# def get_list_keys(i_match):
#    this_dict_csss = get_dict(i_match)
#
#    # Lista con las keys del diccionario "this_dict_csss"
#    list_keys_dict = list(this_dict_csss.keys())
#
#    return list_keys_dict



