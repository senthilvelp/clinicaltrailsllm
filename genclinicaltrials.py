from service.clinicaltrialservice import ClinicalTrailService
import os
import sys
from files.ctfile import CTFile
from process.ctxml import CTXml
from service.clinicaltrialservice import ClinicalTrailService
from  concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio
import multiprocessing


#path = input("Enter the AllPublicXML.zip file path")
path = "C:\\Users\\vel\\Downloads"
if not os.path.exists:
    print('Path ' + path + ' is not found')
else:
    zipfile = path + '\\AllPublicXML.zip'

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)
    return wrapped

@background
def process(xmlContent:str):
    ctXml = CTXml(xmlContent)
    desc = ctXml.description
    desc = desc.replace("'","''")
    title = ctXml.title
    title = title.replace("'","''")
    service = ClinicalTrailService()
    service.add(id=ctXml.id,url=ctXml.url,title=title,description=desc)

ctfile = CTFile(zipfile)
for content in ctfile:
    process(content)
