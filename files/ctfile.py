import os
import sys
import zipfile
import asyncio
import multiprocessing.pool


class CTFile(object):

    def __init__(_self, xmlzipfile:str):
        _self._z = None
        try:
            _self._z = zipfile.ZipFile(xmlzipfile, mode="r")
        except FileNotFoundError:
            print('File '+ xmlzipfile + ' is not found')
        except:
            print('Some exception has occured')

    def __del__(_self):
        if _self._z is not None:
            print('closing the zipfile')
            _self._z.close()

    def __iter__(_self) -> str:
       eventloop = asyncio.get_event_loop()
       for filename in _self._z.namelist():
            if not os.path.isdir(filename):
                if filename != 'Contents.txt':
                    # read the file with multiprocessing
                    xmlContent = eventloop.run_until_complete(CTFile.__getXmlData(_self._z,filename))
                    yield xmlContent
    
    @classmethod
    async def __getXmlData(_self,z:zipfile.ZipFile,filename:str):
        xml = list()
        for line in z.open(filename, mode="r"):
            xml.append(line.decode('utf-8'))
        return ' '.join(xml)
       
    