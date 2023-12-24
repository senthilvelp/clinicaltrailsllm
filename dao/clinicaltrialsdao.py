from db.astradb import AstraDB
from model.clinicaltrials import ClinicalTrials
from dto.clinicaltrailsdto import ClinicalTrailsDTO

class ClinicalTrialsDAO(object):
    def __init__(_self, entity:ClinicalTrials):
        _self._dbsession = AstraDB()
        _self._entity = entity

    def store(_self):
        nct_id = _self._entity.nctid
        url = _self._entity.url
        title = _self._entity.title
        description = _self._entity.description
        embeddings = _self._entity.embeddings

        sql = f"INSERT INTO clinical_trials(id, url, title, content, embeddings) values ('{nct_id}','{url}','{title}','{description}',{embeddings})"
        _self._dbsession.add2db(sql)

    def storeBulk(_self,params:list):
        stmt = f"INSERT INTO clinical_trials(id, lineno, url, title, content, embeddings) values (?,?,?,?,?,?)"
        _self._dbsession.addbulk2db(stmt,params)

    def update(_self):
        nct_id = _self._entity.nctid
        lineno = _self._entity.lineno
        url = _self._entity.url
        title = _self._entity.title
        description = _self._entity.description
        embeddings = _self._entity.embeddings

        sql = f"Update clinical_trials SET url = '{url}', title = '{title}', content = '{description}' , embeddings = {embeddings} WHERE id = '{nct_id}' and lineno = {lineno})"
        _self._dbsession.update2db(sql)

    def getOne(_self, embeddings:list):
        sql = f"SELECT id, lineno, url, title, content, similarity_cosine(embeddings, {embeddings}) as similarity FROM clinical_trials ORDER BY embeddings ANN of {embeddings}"
        result = _self._dbsession.getOne(sql=sql)
        if result is None:
            raise NotImplemented
        else:
            for row in result:
                ct = ClinicalTrials(row.id, row.lineno, row.url, row.title, row.content)
                ct.similarity = row.similarity
                return ct
    
    def getTop10(_self,embeddings:list):
        sql = f"SELECT id, lineno, url, title, content, similarity_cosine(embeddings, {embeddings}) as similarity FROM clinical_trials ORDER BY embeddings ANN of {embeddings}"
        result = _self._dbsession.getOne(sql=sql)
        if result is None:
            raise NotImplemented
        else:
            ctlist = []
            for row in result:
                ct = ClinicalTrials(row.id, row.lineno, row.url, row.title, row.content, row.similarity)
                ctlist.append(ct)
        return ct
    
    def remove2db(_self,id:str):
        id = _self._entity.nctid
        sql = "DELETE FROM clinical_trials WHERE id = '{id}'"
        _self._dbsession.delete(sql=sql)

    