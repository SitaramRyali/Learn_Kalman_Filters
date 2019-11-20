# KF_Basics_practice

class kf:        
    def __init__(self,data,params):
        self.data = data
        self.dimx = len(data)
        self.est = params[0]
        self.eest = params[1]
        self.mea = params[2]
        self.emea = params[3]
        if data == []:
            self.dimx = 0
    def kg(self):
        val =  self.eest/(self.eest+self.emea)
        return val
    def est_f(self):
        val = self.est + self.kg()*(self.mea -self.est)
        self.est = val
        return val
    def eest_f(self):
        val =  (1-self.kg())*(self.eest)
        self.eest = val
        return val
    
        
data_input = [72]
params = [68,2,0,4]
mea_data = [75,71,70,71,73,80]
my_kf = kf(data_input,params)
for i in range(len(mea_data)):
    my_kf.mea = mea_data[i]
    print('iteration {} values are'.format(i+1))
    print('kg:',my_kf.kg())
    print('current estimation:',my_kf.est_f())
    print('current estimation error:',my_kf.eest_f())
    print('\n')
    



