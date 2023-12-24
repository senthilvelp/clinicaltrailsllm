from service.clinicaltrialservice import ClinicalTrailService

sentence = 'what is type 2 diabetics'

def fetch_ANN(sentence:str):
    service = ClinicalTrailService()
    ctone = service.getOne(sentence)
    print(ctone)


fetch_ANN(sentence)