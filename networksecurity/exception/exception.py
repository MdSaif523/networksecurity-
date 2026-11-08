import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    """
    Custom exception class for Network Security.
    """
    def __init__(self, error_message,error_detail:sys):
        self.error_message=error_message
        _,_,exc_tb=error_detail.exc_info()

        self.line_number=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in script: [{self.file_name}] at line number: [{self.line_number}] error message: [{self.error_message}]"
        self.file_name,self.line_number,self.error_message

if __name__=="__main__":
    try:
        logger.logging.info("Enter the try block.")
        a=1/0 # we all know this will raise an exception, so print line doesnot execute 
        # and direct exception line will be executed.
        print("This will not be printed.")
    except Exception as e:
        raise NetworkSecurityException(e,sys)

    