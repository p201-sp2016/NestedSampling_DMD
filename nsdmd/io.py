import pandas as  pd
import os

def get_example_data_file_path(filename, data_dir='data'):
    # __file__ is the location of the source file currently in use (so
    # in this case io.py). We can use it as base path to construct
    # other paths from that should end up correct on other machines or
    # when the package is installed
    start = os.path.abspath(__file__)
    start_dir = os.path.dirname(start)
    # If you need to go up another directory (for example if you have
    # this function in your tests directory and your data is in the
    # package directory one level up) you can use
    # up_dir = os.path.split(start_dir)[0]
    data_dir = os.path.join(start_dir, data_dir)
    return os.path.join(start_dir, data_dir, filename)

def load_data(data_file):
    '''
    Loads the data file from the data_file arg, which requires full path and filename
    Use io.get_example_data_file_path to construct data_file arg easily
    '''
    df =pd.read_csv(data_file)
    
    data_x = df['r'].values
    data_xerr = 0
    data_y = df['v'].values
    data_yerr = df['dv'].values
    
    return  data_x, data_xerr ,  data_y ,data_yerr 

def load_data2(data_file):
    '''
    Loads the data file from the data_file arg, which requires full path and filename
    Use io.get_example_data_file_path to construct data_file arg easily
    '''
    df =pd.read_csv(data_file)
    
    data_x = df['r'].values
    data_xerr = df['dr'].values
    data_y = df['v'].values
    data_yerr = df['dv'].values
    
    return  data_x, data_xerr ,  data_y ,data_yerr 