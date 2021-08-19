####################################
# Author: "BALAVIGNESH"            #
# License: "MIT"                   #
# Date: "15/06/2021"               #
####################################

from ..exceptions.db_exception import DatabaseException
from ..exceptions.table_exception import TableNameException

class Tools:
    @classmethod
    def parse_same_key_list(cls, keylist=[]):
        need_l = {}
        for v in keylist:
            for key, value in v.items():
                need_l.setdefault(key, []).append(value)
        return need_l if need_l else keylist

    @classmethod
    def cast_col_vals(cls, types=None, val_l=None):
        pass

    @classmethod
    def id_parseser(cls, id_dict=[]):
        return dict(id_dict[0])['id']
    
    @classmethod
    def _check_valid_table(cls, tbname):
        tbdict = tbname.__dict__
        if '.' in tbname._name and not '_' in tbname._name:
            return True
        else:
            raise TableNameException("{clx} Table name should '[res.partner, sale.order] like this pattern'".format(clx=tbname.__name__))
        
    @classmethod
    def _check_tb_registry_rights(cls, tbname):
        if tbname:
            pass

