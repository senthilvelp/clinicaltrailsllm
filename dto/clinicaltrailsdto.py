

class ClinicalTrailsDTO(object):
    def __init__(_self):
        pass


    def seq(_self):
        return (_self._id, _self._lineno, _self._url, _self._title, _self._description, _self._embeddings)

    @property
    def id(_self):
        return _self._id
    
    @property
    def lineno(_self) -> int:
        return _self._lineno
    
    @property
    def url(_self) -> str:
        return _self._url
    
    @property
    def title(_self) -> str:
        return _self._title
    
    @property
    def description(_self) -> str:
        return _self._description
    
    @property
    def similairty(_self) -> float:
        return _self._similairty
    
    @property
    def embeddings(_self):
        return _self._embeddings
    
    @id.setter
    def id(_self,id:str):
        _self._id = id

    @lineno.setter
    def lineno(_self,lineno:int):
        _self._lineno = lineno

    @url.setter
    def url(_self,url:str):
        _self._url = url

    @title.setter
    def title(_self,title:str):
        _self._title = title

    @description.setter
    def description(_self,description:str):
        _self._description = description

    @similairty.setter
    def similairty(_self, similariti:float):
        _self._similairty = similariti

    @embeddings.setter
    def embeddings(_self, vectors:[float]):
        _self._embeddings = vectors

