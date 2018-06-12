
import falcon
import json

from db_client import *

class NoteResource:
 
    def on_get(self, req, resp):
        if req.get_param("id"):
            result = {'user': r.db(PROJECT_DB).table(PROJECT_TABLE). get(req.get_param("id")).run(db_connection)}
        else:
            user_cursor = r.db(PROJECT_DB).table(PROJECT_TABLE).run(db_connection)
            result = {'users': [i for i in user_cursor]}
        resp.body = json.dumps(result)

    def on_post(self, req, resp):
         try:
             raw_json = req.stream.read()
         except Exception as ex:
             raise falcon.HTTPError(falcon.HTTP_400,'Error',ex.message)

         try:
             result = json.loads(raw_json, encoding='utf-8')
             sid =  r.db(PROJECT_DB).table(PROJECT_TABLE).insert({'name':result['name']}).run(db_connection)
             resp.body = json.dumps(sid)
         except ValueError:
             raise falcon.HTTPError(falcon.HTTP_400,'Invalid JSON','Could not decode the request body. The ''JSON was incorrect.')

    def on_put(self, req, resp):
         try:
             raw_json = req.stream.read()
         except Exception as ex:
             raise falcon.HTTPError(falcon.HTTP_400,'Error',ex.message)

         try:
             result = json.loads(raw_json, encoding='utf-8')
             sid =  r.db(PROJECT_DB).table(PROJECT_TABLE).filter(r.row['id'] == req.get_param("id")).update({'name':result['name']}).run(db_connection)
             resp.body = json.dumps(result)
         except ValueError:
             raise falcon.HTTPError(falcon.HTTP_400,'Invalid JSON','Could not decode the request body. The ''JSON was incorrect.')
    
    def on_delete(self, req, resp):
        res = r.db(PROJECT_DB).table(PROJECT_TABLE).filter( r.row["id"] == req.get_param("id") ).delete().run(db_connection)
        resp.body = json.dumps(res)

api = falcon.API()
api.add_route('/users', NoteResource())
        
