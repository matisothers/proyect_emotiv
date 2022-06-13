from ast import keyword
from cortex import Cortex
import json

class Query():

    def __init__(self):
        self.c = Cortex(user, debug_mode=True)


    def authorize(self):
        self.c.authorize()


    def do_query(self,query,order_by,limit=0):
        """
        To do a query to records
        query: object with at least one parameter
            licenseId, applicationId, keyword, startDatetime, modifiedDatetime, duration
        order_by: array of objects with a single attribute
        
        Returns
        -------
        """
        return self.c.query_records(query,order_by,limit)




    def export_record(self, folder, types, format, version, ids):
        self.c.export_record(folder,types, format, version, ids)


    def export_by_query(self,query, order_by=[{'startDatetime': 'ASC'}], limit=0,folder='\\record-emotiv',\
                                types=['PM', 'BP'], format='CSV', version = 'V2'):

        result = self.do_query(query,order_by,limit)
        ids = []
        for record in result['records']:
            ids.append(record['uuid'])

        self.export_record(folder,types, format, version,ids)




user = {
    "client_id" : "KD7TAk1pdrSLO42V3XrYJhxv6d15zgmyRsVwRT98",
    "client_secret" : "vwBoZJiw0fWgKHMweEBRRDkRjGcfk9TK0X95lUcgOuEd2enAqKnYt9T9nsfdaDOtUwd5nie1XFw1wjuQtF7HzATBRbB09L35yHcHRWhAVAFd318ZNrtN7yfEU4sjm6nX",
    "debit" : 100
}

q = Query()
q.authorize()
query = {'keyword':'example for recording'}
# result = q.do_query(query,[{"startDatetime":"DESC"}],limit=2)
q.export_by_query(query,folder="\\record-emotiv", limit=1)

# ids = []
# for record in result['records']:
#     ids.append(record['uuid'])

# q.c.request_download(ids)
