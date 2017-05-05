import pandas as  pd
import os



def get_data_file_path(filename, data_dir='data'):
    # __file__ is the location of the source file currently in use (so
    # in this case io.py). We can use it as base path to construct
    # other paths from that should end up correct on other machines or
    # when the package is installed
    start = os.path.abspath(__file__)
    start_dir = os.path.dirname(os.path.dirname(start))
    # If you need to go up another directory (for example if you have
    # this function in your tests directory and your data is in the
    # package directory one level up) you can use
    # up_dir = os.path.split(start_dir)[0]
    data_dir = os.path.join(start_dir, data_dir)
    return os.path.join(start_dir, data_dir, filename)



def load_data(data_file):
    
    df =pd.read_csv(data_file)
    
    data_x = df['r'].values
    data_xerr = df['dr'].values
    data_y = df['v'].values
    data_yerr = df['dv'].values
    
    return  data_x, data_xerr ,  data_y ,data_yerr 
