import numpy as np
import json

class Stats:
    def __init__(self, elevation_range, height_matrix):
        self.elevation = self.__get_elevation_data_from(elevation_range, height_matrix)

    def __get_elevation_data_from(self, elevation_range, height_matrix):
        # randomize elevation
        range_ = self.__get_rand_range(elevation_range)

        # find min/max pos in heightmap
        min_pos = np.unravel_index(height_matrix.argmin(), height_matrix.shape)
        max_pos = np.unravel_index(height_matrix.argmax(), height_matrix.shape)

        elevation_dict = {
            'low': {
                'value': int(range_[0]),
                'location': str(min_pos)
            },
            'high': {
                'value': int(range_[1]),
                'location': str(max_pos)
            }
        }

        return elevation_dict

    def __get_rand_range(self, elevation_range):
        elev = np.random.uniform(elevation_range[0], elevation_range[1])
        scale_min = elev * 0.05
        scale = np.random.uniform(scale_min, scale_min * 2)
        range_ = np.random.normal(elev, scale, size=(2, 1))
        
        while range_[1]-range_[0] < scale_min: #ensure Max > min by some margin
            range_ = np.random.normal(elev, scale, size=(2, 1))
        
        return range_

    def _save_to(self, path):
        with open(path, 'w') as fp:
            #dump each data attribute
            json.dump(self.elevation, fp, indent=4)