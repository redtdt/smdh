import os

def path_postgres():
    # possible paths
    mypaths = ["c:\\program files\\postgresql","c:\\archivos de programa\\postgresql"]
    myversions = ["8.3","9.0","9.1"]
    thepath = ''
    theversion = ''
    resultado = ''
    for thispath in mypaths:
        candidate = thispath
        #print "checking ", candidate
        if os.path.exists(candidate):
            #print "got ",candidate
            thepath = thispath;
    if thepath:
        for thisversion in myversions:
            candidate = thepath+'\\'+thisversion+'\\bin'
            #print "checking ", candidate
            if os.path.exists(candidate):
                #print "got ",candidate
                theversion = thisversion
    if thepath and theversion:
        resultado =      thepath+'\\'+theversion       
    return resultado
            


if __name__ == '__main__':
    print path_postgres()
    pass # add a call to run your script here
