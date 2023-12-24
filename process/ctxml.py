import xml.etree.ElementTree as et

class CTXml(object):

    def __init__(_self,text:str):
        _self._id, _self._url, _self._title, _self._desc = CTXml.__process(text)

    def __str__(_self):
        return _self._id, _self._url, _self._title, _self._desc
    
    @property
    def id(_self) -> str:
        return _self._id
    
    @property
    def url(_self) -> str:
        return _self._url
    
    @property
    def title(_self) -> str:
        return _self._title
    
    @property
    def description(_self) -> str:
        return _self._desc


    @classmethod
    def __process(_self,xml_data:str):
        xml = et.XML(xml_data)
        nct_id = xml.findtext('.//nct_id')
        url = xml.findtext('.//url')
        title = xml.findtext('.//official_title')
        if title is None:
            title = xml.findtext('.//brief_title')
        desc = xml.findtext('.//detailed_description/textblock')
        if desc is None:
            desc = xml.findtext('.//brief_summary/textblock')
        return nct_id, url, title, desc
