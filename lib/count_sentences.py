#!/usr/bin/env python3

class MyString:
  
 
  
  def __init__(self,value=""):
    self._value=value
  
  def get_value(self):
    return self._value
  
  def set_value(self,value):
    if(type(value)==str):
      self._value=value
    else:
      print("The value must be a string.")
      
  
  def is_sentence(self):
    return self._value.endswith(".")
  def is_question(self):
    return self._value.endswith("?")
  def is_exclamation(self):
    return self._value.endswith("!")
  def count_sentences(self):
        
        sentences = self._value.replace('...', '.').replace('!!', '!').replace('??', '?').split('.')
        
        sentences = [sentence for sentence in sentences if sentence]
        return len(sentences)
  
  value=property(get_value,set_value)
  
  