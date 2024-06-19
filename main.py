
import audio as audio
import openai_stxt as a
import actiondetection  as b
#import t
#import test3 as b

text=a.aud_text()
print("Transcribed Text:",text)
output_dic = b.parse_text(text)
#print(c)
print(output_dic)
