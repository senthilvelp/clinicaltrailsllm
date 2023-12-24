from cassandra.cluster import Cluster
from cassandra.concurrent import execute_concurrent, execute_concurrent_with_args
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import RetryPolicy, DCAwareRoundRobinPolicy
import os
from dotenv import load_dotenv


class AstraDB(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance') or not cls.instance:
          cls.instance = super().__new__(cls)
        return cls.instance
        
    def __init__(_self) -> None:
        load_dotenv()
        SECURE_CONNECT_BUNDLE = os.environ['SECURE_CONNECT_BUNDLE']
        CLIENT_ID = os.environ['CLIENT_ID']
        CLIENT_SECRET = os.environ['CLIENT_SECRET']
        KEYSPACE = os.environ['KEYSPACE']
        current_dir = os.getcwd()
        bundle_zip = current_dir + os.sep + SECURE_CONNECT_BUNDLE
        cloud_config = {
            'secure_connect_bundle': bundle_zip,
            'use_default_tempdir': True
        }
        auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
        policy = DCAwareRoundRobinPolicy()
        retryPolicy = RetryPolicy()
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider,load_balancing_policy=policy,default_retry_policy=retryPolicy)
        _self._session = cluster.connect()
        if _self._session is None:
            raise NotImplementedError
        else:
            _self._session.set_keyspace(KEYSPACE)
            _self._session.default_timeout = 60

    def add2db(_self,sql:str):
        result = AstraDB.__executeSQL(_self._session,sql)
        if result is None:
            raise NotImplemented
        else:
            print('Row Inserted')

    def addbulk2db(_self,stmt:str,params:list):
        #results = execute_concurrent(session=_self._session,statements_and_parameters=stmt_params,concurrency=size,raise_on_first_error=True,results_generator=False)
        prepare_stmt = _self._session.prepare(stmt)
        results = execute_concurrent_with_args(_self._session,statement=prepare_stmt,parameters=params,concurrency=50)
        i = 0
        for (success, result) in results:
            if not success:
                print('Error inserting row')
                raise NotImplemented  # result will be an Exception
            else:
                print('Inserted')

    def update2db(_self,sql:str):
        result = AstraDB.__executeSQL(_self._session,sql)
        if result is None:
            raise NotImplemented
        else:
            print('Row Updated')
    
    def getOne(_self, sql:str):
        onesql = sql + ' LIMIT 1'
        result = AstraDB.__executeSQL(_self._session,onesql)
        if result is None:
            raise NotImplemented
        else:
            return result
        
    def getTop10(_self,sql:str):
        top10SQL = sql + ' LIMIT 10'
        result = AstraDB.__executeSQL(_self._session,top10SQL)
        if result is None:
            raise NotImplemented
        else:
            return result
        
    def delete(_self,sql:str):
        result = AstraDB.__executeSQL(_self._session,sql)
        if result is None:
            raise NotImplemented
        else:
            print('Row Deleted')

    @classmethod    
    def __executeSQL(_self,session:any,sql:str):
        return session.execute(sql)
        
    
