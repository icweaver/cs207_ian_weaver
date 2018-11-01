class Markov:
    def __init__(self):
        self.data = None
        
    def load_data(self, array):
        self.data = array
    
    def get_prob(self, previous_day, following_day):
        weather_names = {
            'sunny': 0,
            'cloudy': 1,
            'rainy': 2,
            'snowy': 3,
            'windy': 4,
            'hailing': 5
        }

        before_idx = weather_names[previous_day]
        after_idx = weather_names[following_day]

        try:
            prob = self.data[before_idx][after_idx]
            return prob
        except TypeError: # catch if no data file loaded
            error_msg = 'please load data file first with load_data method'
            return error_msg
