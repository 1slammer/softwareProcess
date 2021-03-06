import math
class DataSet(object):

    def __init__(self):
        pass
        
    def gamma(self, x):
        if(x == 1):
            return 1
        if(x == 0.5):
            return math.sqrt(math.pi)
        return (x - 1) * self.gamma(x - 1)
    
    def LHP(self, n):
        n = float(n)
        numerator = self.gamma((n + 1.0) / 2.0)
        denominator = self.gamma(n / 2.0) * math.sqrt(n * math.pi)
        result = numerator / denominator
        return result
    
    def f(self, u, n):
        n = float(n)
        base = (1 + (u ** 2) / n)
        exponent = -(n + 1.0) / 2.0
        result = base ** exponent
        return result
    
    def p(self, t=None, n=None, tails=None):
        if(t == None):
            raise ValueError
        if(not(isinstance(t, float))):
            raise ValueError
        if(t < 0.0):
            raise ValueError
        
        if(tails == None):
            raise ValueError
        if(not(isinstance(tails, int))):
            raise ValueError
        if((tails != 1) & (tails != 2)):
            raise ValueError
        
        if(n == None):
            raise ValueError
        if(not(isinstance(n, int))):
            raise ValueError
        if(n < 3):
            raise ValueError
        
        self.n = n
        
        constant = self.LHP(n)
        integration = self.RHP(t, n, self.f)
        if(tails == 1):
            result = constant * integration + 0.5
        else:
            result = constant * integration * 2
            
        if(result > 1.0):
            raise ValueError
        
        return result
    
    def RHP(self, t=None, n=None, f=None):
        if(t == None):
            raise ValueError
        if(not(isinstance(t, float))):
            raise ValueError
        if(t < 0.0):
            raise ValueError
        
        if(n == None):
            raise ValueError
        if(not(isinstance(n, int))):
            raise ValueError
        if(n < 3):
            raise ValueError
        
        if(f == None):
            raise ValueError
        
        epsilon = 0.001
        simpsonOld = 0
        simpsonNew = epsilon
        s = 4
        while (abs((simpsonNew - simpsonOld ) / simpsonNew) > epsilon):
            simpsonOld = simpsonNew
            w=t/s
            interCal = 0
            for x in range(0, s+1):
                if x == 0:
                    interCal = interCal + f(0, n)
                elif x == s:
                    interCal = interCal + f(t, n)
                elif (x % 2 == 0):
                    interCal = interCal + 2*f((x+1) * w, n)
                elif (x % 2 == 1):
                    interCal = interCal + 4*f((x+1) * w, n)
            simpsonNew = interCal * (w/3)
            s = s*2
        return simpsonNew
        
    
        
            
        
