'''
    Created on Sep 6, 2015

    @author: Wayne Nolen

    This class provides functions for creating and maintaining an inventory
    of stars visible from any point on earth, as well as characteristics that
    can be used to locate those stars.
'''
import math
class StarCatalog(object):
    '''
    Constructor
    '''
    def __init__(self): pass
    
    
    def loadCatalog(self, starFile=None):
        self.catalog = {}
        self.dimmest = -999999999999999.9
        self.brightest = 999999999999999.9
        starCount = 0
        try: 
            openFile = open(starFile)
        
        except Exception:
            raise ValueError("""StarCatalog.loadCatalog:  Error opening file. 
            Please verify that the file exists and is properly named.""")
        try:
            for line in openFile:
                tokenLine = line.split()
                if tokenLine[0] in self.catalog.keys():
                    raise ValueError("StarCatalog.loadCatalog:  Duplicate keys in file.")
                self.catalog[tokenLine[0]]=tokenLine[1:4]
                floatValue = float(tokenLine[1])
                if floatValue > self.dimmest:
                    self.dimmest = floatValue
                if floatValue < self.brightest:
                    self.brightest=floatValue
                starCount=starCount+1
                
        except Exception:
            raise
        
        return starCount
            
            
    def emptyCatalog(self):
        numStars = len(self.catalog)
        self.catalog.clear()
        return numStars
    
    def getStarCount(self, lowerMagnitude=None, upperMagnitude=None):
        self.count = 0
        if lowerMagnitude==None:
            lowerMagnitude=self.brightest
        if upperMagnitude==None:
            upperMagnitude=self.dimmest
        if lowerMagnitude > upperMagnitude:
            raise ValueError("StarCatalog.getStarCount:  Lower magnitude must be less than upper magnitude.")
        if upperMagnitude < 0:
            raise ValueError("StarCatalog.getStarCount:  Upper magnitude must be greater than zero.") 
        try:
            for value in self.catalog.itervalues():
                if float(value[0]) >= lowerMagnitude and float(value[0]) <= upperMagnitude:
                    self.count=self.count+1
        except Exception:
            raise ValueError("StarCatalog.getStarCount:  Problem finding stars. Please double-check values.");
        return self.count
    
    def getMagnitude(self, rightAscentionCenterPoint=None,
                     declinationCenterPoint=None,
                     fieldOfView=None):
        found = False
        magnitude = 999999999.9
        
        if rightAscentionCenterPoint < 0 or rightAscentionCenterPoint >= 2*math.pi:
            raise ValueError("StarCatalog.getMagnitude: Input value not in range.")
        if declinationCenterPoint <= -math.pi/2 or declinationCenterPoint >= math.pi/2:
            raise ValueError("StarCatalog.getMagnitude: Input value not in range.")
        try:    
            for value in self.catalog.itervalues():
                if abs(float(value[1])-float(rightAscentionCenterPoint)) < fieldOfView*0.5:
                    if abs(float(value[2])-float(declinationCenterPoint)) < fieldOfView*0.5:
                        found = True
                        if float(value[0]) < magnitude:
                            magnitude = float(value[0])
                            
            if found:
                return magnitude
            else: 
                return None
                        
        except Exception:
            raise ValueError("StarCatalog.getMagnitude:  Error getting the magnitude.")
        
        
        
        
        
        
        
        
        
        
        