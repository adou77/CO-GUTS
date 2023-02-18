def military_time(s):
    #the values(not keys) for these 2 dictionaries were pasted, I did now want to write the whole thing 
    num2words = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
                 10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"
                 ,20:"twenty",21:"twenty one",22:"twenty two",23:"twenty three",24:"twenty four",25:"twenty five",26:"twenty six",27:"twenty seven",28:"twenty eight",29:"twenty nine"
                 ,30:"thirty",31:"thirty one",32:"thirty two",33:"thirty three",34:"thirty four",35:"thirty five",36:"thirty six",37:"thirty seven",38:"thirty eight",39:"thirty nine",
                 40:"forty",41:"forty one",42:"forty two",43:"forty three",44:"forty four",45:"forty five",46:"forty six",47:"forty seven",48:"forty eight",49:"forty nine"
                 ,50:"fifty",51:"fifty one",52:"fifty two",53:"fifty three",54:"fifty four",55:"fifty five",56:"fifty six",57:"fifty seven",58:"fifty eight",59:"fifty nine"
                 ,60:"sixty", "00": "hundred hours"}
    
    num2wordsh= {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
                 10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"
                 ,20:"twenty",21:"twenty-one",22:"twenty-two",23:"twenty-three",24:"twenty-four"}
    
    time = s
    
    #finding the index that seperates the hours and minutes
    if ":" in s:
        index_n = s.index(":")
        value_n = int(s[:index_n])
        time = s.replace(":","")    
    else:
        index_n = len(s) - 2
        value_n = int(s[:index_n])
    
    #Adjusting the hours based on if they are AM or PM
    if "AM" in s:
        time = time.replace("AM","")
        
        #12 is the only complete unique case in terms of hours
        if value_n == 12:
            time = "".join(["0"] + time[index_n:].split())
        elif value_n < 10:
            time = "".join(["0"] +[str(value_n)] +time[index_n:].split())
        
    else:            
        time = time.replace("PM","")
        
        #also a special case
        if value_n == 12:
            time = "".join(["12"] + time[index_n:].split())
            
        #adds 12 hours to the time
        else:    
            time = "".join([str(value_n + 12)]+ [str(time)[index_n:]])
    
    #if time is without minutes add "00" so it can be returned as xx hundred hours
    
    if len(time) < 3 and time != "0":
    # adds "00" based on if the number was AM and if the time it was bigger or smaller than 10
        if index_n < 1:
            time = "".join([time[1:]]+["00"])
        else:
            time = "".join([time]+["00"])
            
    # final adjusters based on: if time is (xx:0x XX)or (0x:xx XX), if time is specifically 12 am, if time is in hours only,and else           
    if time != "0" and time[-2] == "0" and time[-2] != time[-1]:
        if time[0] == "0":
             time_str = "".join([num2words[int(time[0])]] +[" "]+ [num2words[int(time[1:-2])]] +[" "] + [num2words[int(time[-2])]] + [" "] +[num2words[int(time[-1])]])
        else:
            time_str = "".join([num2wordsh[int(time[:-2])]] +[" "] + [num2words[int(time[-2])]] + [" "] +[num2words[int(time[-1])]])
    elif time == "0":
        time_str = "".join([num2wordsh[int(time)]] +[" "] + [num2words["00"]])
    elif time[-2] == "0" and time[-2] == time[-1]:
        time_str = "".join([num2wordsh[int(time[:-2])]] +[" "] + [num2words["00"]])
    elif time[0] == "0":
        time_str = "".join([num2wordsh[int(time[0])]] +[" "]+ [num2wordsh[int(time[1:-2])]]+ [" "] + [num2words[int(time[-2:])]])
    else:
        time_str = "".join([num2wordsh[int(time[:-2])]] +[" "] + [num2words[int(time[-2:])]])
        
                        
    return time_str
