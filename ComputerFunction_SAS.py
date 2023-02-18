#assuming that we are working with values up till (2^7 - 1)
def COMPUTERFUNCTION(x , y):
    bin_x = '{:0>8}'.format(str(bin(x))[2:])
    bin_y = '{:0>8}'.format(str(bin(y))[2:])
    bin_z = []
    
    i = 0
    
    while i < 8:
        if bin_x[i] == bin_y[i]:
            bin_z.append("0")
        elif bin_x[i] == "1" or bin_y[i] == "1":
            bin_z.append("1")
        i+=1
    
    final = "".join(bin_z)
    return(int(final,2))