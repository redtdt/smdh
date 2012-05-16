# -*- coding: cp1252 -*-

tableChars={}
origChars = 'áéíóúñübz'
substChars =  'AEIOUNUVS'
i=0
for c in origChars:
    tableChars[c]=substChars[i]
    i += 1

def strtr(string):
    if string:
        s1=string
        n=len(s1)
        for i in range(n):
             if s1[i] in tableChars:
                 s1=s1[:i]+tableChars[s1[i]]+s1[i+1:]
        return s1
    else:
        return ''
def spanish_metaphone(string):
  
   #initialize metaphone key string
   meta_key   = ""
   
   #set maximum metaphone key size   
   key_length   = 6
   
   #set current position to the beginning
   current_pos   =  0
   
   #get string  length
   string_length   = len(string);
   
   #set to  the end of the string
   end_of_string_pos     = string_length - 1
   original_string = string + "    "

   #Let's replace some spanish characters  easily confused
   original_string = strtr(original_string)
   
   #convert string to uppercase
   original_string = original_string.upper()
   
   
   # main loop
   while (len(meta_key) < key_length): 
   
         
      #break out of the loop if greater or equal than the length
      if (current_pos >= string_length):
         break;
      
        
      #get character from the string
      current_char = original_string[current_pos]
      
      #if it is a vowel, and it is at the begining of the string,
      #set it as part of the meta key        
      if (is_vowel(original_string,current_pos)  \
                            and (current_pos == 0)):
      
         meta_key   += current_char
         current_pos += 1            
    
      #Let's check for consonants  that have a single sound 
      #or already have been replaced  because they share the same
      #sound like 'B' for 'V' and 'S' for 'Z'
      else:
         if (string_at(original_string, current_pos, 1, 
              ['D','F','J','K','M','N','P','R','S','T','V','L'])) :
      
            meta_key   += current_char
         
            #increment by two if a repeated letter is found
            if (substr(original_string, current_pos + 1,1) == current_char):
                                 
               current_pos += 2       
                 
            
            else: # increment only by one                 
               current_pos += 1            
      
         else:  #check consonants with similar confusing sounds
      
         
           
            if current_char == 'C':  
               #special case 'macho', chato,etc.      
               if (substr(original_string, current_pos + 1,1)== 'H'):
                                                       
                  current_pos += 2
                     
               #special case 'acción', 'reacción',etc.      
               elif (substr(original_string, current_pos + 1,1)== 'C'):
                                                        
                     
                  meta_key   += 'X'          
                  current_pos += 2
                  
                         
               # special case 'cesar', 'cien', 'cid', 'conciencia'
               elif (string_at(original_string, current_pos, 2, 
                         ['CE','CI'])) :
               
                  meta_key   += 'S'
                  current_pos += 2
                  
               
               else:
                  meta_key   += 'K';                   
                  current_pos += 1;            
               
               
            elif current_char == 'G':
               # special case 'gente', 'ecologia',etc 
               if (string_at(original_string, current_pos, 2, 
                         ['GE','GI'])):
               
                  meta_key   += 'J'            
                  current_pos += 2
                  
               
               else:
                 meta_key   += 'G';                   
                 current_pos += 1;            
               
          
            #since the letter 'h' is silent in spanish, 
            #let's set the meta key to the vowel after the letter 'h'
            elif current_char =='H':                
               if (is_vowel(original_string, current_pos + 1)):
               
                  meta_key += original_string[current_pos + 1]
                  current_pos += 2
                  
               
                      
               else:
                 meta_key   += 'H'
                 current_pos += 1            
               
               
            elif current_char == 'Q':
               if (substr(original_string, current_pos + 1,1) == 'U'):
               
                  current_pos += 2
               
               else: 
               
                  current_pos += 1
               
            
               meta_key   += 'K'          
               
               
            elif current_char == 'W':          
               meta_key   += 'U'            
               current_pos += 2
               
               
            elif current_char == 'X': 
               #some mexican spanish words like'Xochimilco','xochitl'         
               if (current_pos == 0):
                                   
                  meta_key   += 'S'
                  current_pos += 2 
                            
               else: 
                          
                  meta_key   += 'X'
                  current_pos += 1 
               
               
            else:
               current_pos += 1
               
         
            
         
          
        
      
      #Commented code *** for debugging purposes only ***
      #/*
      #printf("<br>ORIGINAL STRING:    '%s'\n", $original_string);
      #printf("<br>CURRENT POSITION:   '%s'\n", $current_pos);
      #intf("<br>META KEY STRING:    '%s'\n", $meta_key);
      #*/
      
   
       
    
   #trim any blank characters
   meta_key = meta_key.strip()
   
   #return the final meta key string
   return meta_key;
   

# ====== End of spanish_metaphone function =======================

  
#***** helper functions *******************************************
#****************************************************************** 

#/*=================================================================*\
  # Name:      string_at($string, $start, $string_length, $list)
  # Return:	   Bool
#\*=================================================================*/
  
def string_at(string, start, string_length, lista):

   if ((start <0) or (start >= len(string))):
      return 0
   for expr in lista:
       if string.find(expr, start, start + string_length) != -1:
           return 1
        
   #for i in range(len(lista)): 
   #   if (lista[i] == substr(string, start, string_length)):
   #       return 1
    
   return 0

def substr(string, start, string_length):
    v = string[start:start + string_length]
    return v
  


#/*=================================================================*\
  # Name:      is_vowel($string, $pos)
  # Return:    Bool
#\*=================================================================*/

def is_vowel(string, pos):
    return string[pos] in ['A','E','I','O','U'] 


