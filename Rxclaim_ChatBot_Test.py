# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:18:54 2018

@author: akansal2
"""
class RxClaim_chatbot():
    
    
    #from Rxclaim_ChaBot import processing
    
    
    def bot_reply(self,message):
        from chatterbot import ChatBot
        from chatterbot.trainers import ListTrainer
        
        path = 'C:/A_stuff/Learning/Machine Learning/ML_Experimental_Learning/ChatterBot/Rxclaim_ChatBot/Version 2.0/Rxclaim_ChatBot_V2.0/'
        bot = ChatBot("Rxclaim_Wiki",
                      read_only=True,
                      preprocessors=[
                                   'chatterbot.preprocessors.TB_Correction'
                                    ],
                     input_adapter="chatterbot.input.VariableInputTypeAdapter",
                     logic_adapters = [
                             {
                             'import_path' : 'chatterbot.logic.BestMatch',  
                             'statement_comparision_function' : 'chatterbot.comparisions.levenshtein_distance',
                              'response_selection_method' : 'chatterbot.response_selection.get_first_response'
                              },
                             {
                        'import_path' : 'chatterbot.logic.LowConfidenceAdapter',
                        'threshold': 0.65,
                        'default_response': 'I am sorry, but I do not understand.Can you please rephrase your statement.'
                        },
                             ],
                             #filters=["chatterbot.filters.RepetitiveResponseFilter"],
                       storage_adapter = 'chatterbot.storage.SQLStorageAdapter',  
                       
                        database = path + 'Rxclaim_databaseV1.0.sqlite3'  #SQLIite is SQL  light weight SQL database
                      )
        
        
        bot.set_trainer(ListTrainer)
        
        
        
        reply = bot.get_response(message)
            
        return str(reply)
        
        



