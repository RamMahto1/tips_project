import os
import sys
import pickle
from src.logger import logging
from src.exception import CustomException



def save_object(file_path,obj):
    """
    this saves the object to a file unsing pickle.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
    
    
    def load_object(file_path):
        try:
            with open(file_path,'rb') as file_obj:
                return pickle.load(file_obj)
        except Exception as e:
            raise CustomException(e, sys)
        
    if __name__ == "__main__":
        save_object()
        