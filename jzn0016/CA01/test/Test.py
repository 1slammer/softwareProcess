'''
Created on Sep 6, 2015

@author: jw
'''
from CA01.prod import StarCatalog

if __name__ == '__main__':
    
    myCatalog = StarCatalog.StarCatalog()
    try:
        print myCatalog.loadCatalog("/Users/jw/Desktop/stars.txt")
    except Exception as e:
        print e.args[0]
    print myCatalog.catalog["68953"]
    
    try:
        print myCatalog.getStarCount(lowerMagnitude=4.9, upperMagnitude=3.2)
    except Exception as e:
        print e.args[0]
    
    try:
        print myCatalog.getMagnitude(rightAscentionCenterPoint=10.0, declinationCenterPoint=-1.11, fieldOfView=0.9)
    except Exception as e:
        print e.args[0]
    brightest = 100
    for value in myCatalog.catalog.itervalues():
        if float(value[0]) < brightest:
            brightest = float(value[0])
            
    print brightest
    
    print(myCatalog.emptyCatalog())
    