####################################
# Author: "BALAVIGNESH"            #
# License: "MIT"                   #
# Date: "15/06/2021"               #
####################################
class BaseException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "%s" % self.msg
    
class DatabaseException(BaseException):
    pass
    