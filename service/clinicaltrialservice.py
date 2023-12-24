from dao.clinicaltrialsdao import ClinicalTrialsDAO
from model.clinicaltrials import ClinicalTrials
from vectors.vector import CTVector
from dto.clinicaltrailsdto import ClinicalTrailsDTO

class ClinicalTrailService(object):

    def __init__(_self):
        pass

    def add(_self, id:str, url:str,title:str,description:str):
        ct = ClinicalTrailService.__convertToModel(id=id,lineno=0,url=url,title=title,description=description)
        vector = CTVector(description)
        ct.embeddings = vector.embeddings
        sentences = vector.sentences
        vectors = ct.embeddings
        params = []
        for i, sentence in enumerate(sentences):
            dto = ClinicalTrailsDTO()
            dto.id = id
            dto.lineno = i+1
            dto.url = url
            dto.title =title
            dto.description = sentence
            dto.embeddings = vectors[i]
            params.append(dto.seq())
 
        dao = ClinicalTrialsDAO(ct)
        dao.storeBulk(params)

    def update(_self, id:str, lineno:int, url:str,title:str,description:str):
        ct = ClinicalTrailService.__convertToModel(id=id,lineno=lineno,url=url,title=title,description=description)
        vector = CTVector(description)
        ct.embeddings = vector.embeddings
        dao = ClinicalTrialsDAO(ct)
        dao.update()

    def delete(_self,id:str):
        ct = ClinicalTrailService.__convertToModel(id=id,url='',title='',description='')
        dao = ClinicalTrialsDAO(ct)
        dao.delete()

    def getOne(_self,search:str):
        vector = CTVector(search)
        ct = ClinicalTrailService.__convertToModel(id='1',lineno=0,url='',title='title',description=search)
        ct.embeddings = vector.embeddings[0]
        dao = ClinicalTrialsDAO(ct)
        ctone = dao.getOne(ct.embeddings)
        return ctone

    @classmethod
    def __convertToDto(_self,id:str,lineno:int,url:str,title:str,description:str, simiality:float) -> ClinicalTrials:
        dto = ClinicalTrailsDTO()
        dto.description = description
        dto.id = id
        dto.lineno = lineno
        dto.similairty = simiality
        dto.title = title
        dto.url = url
        return dto


    @classmethod
    def __convertToModel(_self,id:str,lineno:int,url:str,title:str,description:str) -> ClinicalTrials:
        return ClinicalTrials(id=id,lineno=lineno,url=url,title=title,description=description)

    