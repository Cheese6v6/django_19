import googletrans
# print(googletrans.LANGUAGES)

from googletrans import Translator
 
text1 = "Hello welcome to my website!"
 
translator = Translator()
  
trans1 = translator.translate(text1, src='en', dest='ja') 
                                # src : 출발지 , dest : 목적지 , en, ja = 국가코드
 
print("English to Japanese: ", trans1.text)
