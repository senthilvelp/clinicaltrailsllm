from nltk.tokenize import word_tokenize, sent_tokenize
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, models
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

class CTVector(object):

    def __init__(_self,text:str):
        #_self._embeddings = CTVector.__embeddings(text)
        _self._embeddings = _self.__embeddings(text)
 
    
    #Mean Pooling - Take attention mask into account for correct averaging
    @classmethod
    def __mean_pooling(_self,model_output, attention_mask):
        token_embeddings = model_output[0] #First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
        sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
        return sum_embeddings / sum_mask

    @classmethod
    def __max_pooling(_self,model_output, attention_mask):
        token_embeddings = model_output[0] #First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        token_embeddings[input_mask_expanded == 0] = -1e9  # Set padding tokens to large negative value
        return torch.max(token_embeddings, 1)[0]
    
    def __preprocess(_self,text:str):
        soup = BeautifulSoup(text, features="lxml")
        processedText = soup.get_text().lower().replace('\r\n','').replace('&#xD;','\n').replace('\n','')
        return processedText;

    
    def __embeddings(_self, text:str):
        processedText = _self.__preprocess(text)
        sentences = sent_tokenize(processedText)
        _self._sentences = sentences
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        sentence_embeddings = model.encode(sentences)
        return sentence_embeddings.tolist()

    @classmethod
    def __embeddings1(_self,text:str):
        processedText = CTVector.__preprocess(text)
        sentences = sent_tokenize(processedText)
        _self._sentences = sentences
        word_embedding_model = models.Transformer('bert-base-uncased', max_seq_length=256)
        pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
        from torch import nn
        dense_model = models.Dense(in_features=pooling_model.get_sentence_embedding_dimension(), out_features=768, activation_function=nn.Tanh())
        model = SentenceTransformer(modules=[word_embedding_model, pooling_model, dense_model])
        sentence_embeddings = model.encode(sentences=sentences,convert_to_numpy=True,device='cpu',normalize_embeddings=True)
        return sentence_embeddings.tolist()
    
    @classmethod
    def __oldEmbeddings(_self,text:str):
        processedText = CTVector.__preprocess(text)
        """
        #model = SentenceTransformer("medicalai/ClinicalBERT")
        #model.max_seq_length = 1024 * 1024
        #text_embeddings = model.encode([processedText],convert_to_numpy=True,normalize_embeddings=True)
        #return text_embeddings[0].tolist()
        """
        #
        #Load AutoModel from huggingface model repository
        #
        #tokenizer = AutoTokenizer.from_pretrained("medicalai/ClinicalBERT")
        #model = AutoModel.from_pretrained("medicalai/ClinicalBERT")

        #Tokenize sentences
        sentences = sent_tokenize(processedText)
        _self._sentences = sentences
        #encoded_input = tokenizer(sentences, padding=True, truncation=True, max_length=1024*1024, return_tensors='pt', add_special_tokens=True)

        #Compute token embedding
        #with torch.no_grad():
        #    model_output = model(**encoded_input)

        #perform pooling. In this case, mean pooling
        #sentence_embeddings = CTVector.__mean_pooling(model_output, encoded_input['attention_mask'])
        #return sentence_embeddings.flatten().tolist()
        #sentence_embeddings = F.normalize(sentence_embeddings,p=2,dim=0)
        #numpy = F.conv1d(sentence_embeddings)
        #return numpy.tolist()
        #model = SentenceTransformer('medicalai/ClinicalBERT')
        model = SentenceTransformer('all-MiniLM-L6-v2')
        sentence_embeddings =  model.encode(sentences,convert_to_numpy=True, normalize_embeddings=True)
        return sentence_embeddings.tolist()

    @property
    def embeddings(_self):
        return _self._embeddings
    
    @property
    def sentences(_self):
        return _self._sentences

    @classmethod
    def __preprocess(_self,text:str):
        soup = BeautifulSoup(text, features="lxml")
        processedText = soup.get_text().lower().replace('\r\n','').replace('&#xD;','\n').replace('\n','')
        return processedText;

    