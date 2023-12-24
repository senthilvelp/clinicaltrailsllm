import uuid
from db.astradb import AstraDB

class LLMTest(object):

    def __init__(self):
        self.data:str = None
        self.db = AstraDB()

    def setText(self, text:str):
        self.data = text.replace("'","''")

    def setId(self, uid):
        self.uid = uid

    def save(self):
        uid = uuid.uuid4()
        if self.data is None:
            raise NotImplementedError
        if self.db is None:
            raise NotImplementedError
        insert_sql = f"INSERT INTO llm_test (id, data) values ({uid}, '{self.data}')"
        result = self.db.session.execute(insert_sql)
        if result is None:
            raise NotImplemented
        else:
            print('Inserted')

    def save(self, text:str):
        if self.db is None:
            raise NotImplementedError
        uid = uuid.uuid4()
        data = text.replace("'","''")
        insert_sql = f"INSERT INTO llm_test (id, data) values ({uid}, '{data}')"
        result = self.db.session.execute(insert_sql)
        if result is None:
            raise NotImplemented
        else:
            print('Inserted')

    def getOne(self):
        if self.db is None:
            raise NotImplementedError
        query_sql = f"SELECT id, data from llm_test LIMIT 1"
        result = self.db.session.execute(query_sql)
        if result is None:
            raise NotImplemented
        else:
            for row in result:
                llmtest = LLMTest()
                llmtest.uid = row.id
        return llmtest
    
    def getTop10(self):
        if self.db is None:
            raise NotImplementedError
        query_sql = f"SELECT id, data from llm_test LIMIT 10"
        result = self.db.session.execute(query_sql)
        if result is None:
            raise NotImplemented
        else:
            llmlist = []
            for row in result:
                llmtest = LLMTest()
                llmtest.setId(row.id)
                llmtest.setText(row.data)
                llmlist.append(llmtest)
        return llmlist
    
    def __str__(self) -> str:
        return f"ID : {self.uid}, data : {self.data}"
