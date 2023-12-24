class ClinicalTrials:

    def __init__(_self,id:str,lineno:int,url:str,title:str,description:str):
        _self._id = id
        _self._lineno = lineno
        _self._url = url
        _self._title = title
        _self._description = description
        _self._similarity = 0.0
        _self._embeddings = None
      
    def __str__(_self):
        return f"ID:{_self._id}\n Line No : {_self._lineno}\n URL:{_self._url}\n Title:{_self._title}\n Description:{_self._description}\n Simiality:{_self._similarity}\n"

    def __iter__(_self):
        return _self
    
    def __next__(_self):
        return _self._id, _self._lineno, _self._url, _self._title, _self._description, _self._similarity
    
    def seq(_self):
        return (_self._id, _self._lineno, _self._url, _self._title, _self._description,)
    
    @property
    def nctid(_self) -> str:
        return _self._id
       
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
    def similarity(_self) -> str:
        return _self._similarity
    
    @property
    def embeddings(_self) -> str:
        return _self._embeddings
    
    @property
    def lineno(_self) -> int:
        return _self._lineno
    
    @similarity.setter
    def similarity(_self,similaiti:float):
        _self._similarity = similaiti

    @embeddings.setter
    def embeddings(_self, vectors:list):
        _self._embeddings = vectors

