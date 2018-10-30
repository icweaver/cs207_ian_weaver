class Markov:
    def __init__(self):
        pass
        
    def load_data(self, array):
        self.data = array
    
    def get_prob(self, previous_day, following_day):
        weather_names = {'sunny':0, 'cloudy':1, 'rainy':2, 
                 'snowy':3, 'windy':4, 'hailing':5}
        before_idx = weather_names[previous_day]
        after_idx = weather_names[following_day]
        return self.data[before_idx][after_idx]
