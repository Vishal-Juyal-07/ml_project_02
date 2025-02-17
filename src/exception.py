import sys

def error_message_details(error,error_detail:sys):
    _,_,exc_info=error_detail.exc_info()
    filename=exc_info.tb_frame.f_code.co_filename
    error_message="Error occured in python script [{0}] at line number [{1}] and error message is [{2}].".format(filename,exc_info.tb_lineno,str(error)
                                                                                                                 )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)    
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message    