# Chatbot
Creating a chatbot(In-Progress task)
I am framing this readme file in form of notes with step by step info about the process for creating chatbots and using its different functions.We will start from very basic and would be using python chatterbot package to create a functioning chatbot.

#first step would be to import chatterbot.For installation purpose, you can directly use 'pip install chatterbot'. Refer for more details on : http://chatterbot.readthedocs.io/en/stable/tutorial.html


#So lets get started with importing the chatbot first

    from chatterbot import ChatBot   #importing ChatBot class

#Creating an instance for this ChatBot 

    bot = ChatBot()                  # this will be the instance of chatbot class and with this we can utilize its inbuilt functions.

#While creating instance , we can give pass various arguements to it like below:
  
  #only name as arguement
         
     bot = ChatBot('Norman')       # name of chatbot --- Ques- Where do we see this name after execution of code?
  
 #OR
  
  #name and storage adapter as arguements
  
    bot = ChatBot(
                  'Norman',
                   storage_adapter='chatterbot.storage.SQLStorageAdapter',    # tells chatbot to connect to SQL database
                  database='./database.sqlite3'                               # path of that database 
                   ) 
#We could have used MongoDB Storage Adapter as well. So depending on available database, we can connect our chatbot to respective          databases. For Mongo DB, write your code like this 'chatterbot.storage.MongoDatabaseAdapter'

  #OR
    
  #name,storage adapters and Input/Output adapters
 
     bot = ChatBot(
                    'Norman',
                    storage_adapter='chatterbot.storage.SQLStorageAdapter',
                    database='./database.sqlite3',
                    input_adapter='chatterbot.input.TerminalAdapter',           #From where the chatbot should get input i.e from 
                                                                                #console input or from a variable
                    output_adapter='chatterbot.output.TerminalAdapter'          # where to display the output
                    )

   #OR 
    
   #name, storage adapters,Input/Output adapters and Logical adapters 
       
       bot = ChatBot(
                      'Norman',
                      storage_adapter='chatterbot.storage.SQLStorageAdapter',
                      database='./database.sqlite3',
                      input_adapter='chatterbot.input.TerminalAdapter',           
                      output_adapter='chatterbot.output.TerminalAdapter',
                      logic_adapters=[                                          #perform logical opertions          
                                      'chatterbot.logic.MathematicalEvaluation', # returns sum/product etc of numbers
                                       'chatterbot.logic.TimeLogicAdapter'       # returns the system time
                                     ]
                        )

 #We have other logical operators as well like Best Match logical operator. It will return the best response to the input message. 
    
 
#Traning your chatbot
#You can train your chatbot using a list trainer. List trainer will take the traning data in form of a list of string/sentences/conversation
#First set the trainer and then provide the data

    bot.set_trainer(ListTrainer)
    bot.train([
                'How are you?',
                'I am good.',
                'That is good to hear.',
                'Thank you',
                'You are welcome.',
            ])
 
 
#Once initialization and traning is done, You can start the conversation i.e recieving input from user and providing response to it with the below simple while loop:-

      while True:
          try:
           message = input('You :')
           bot_response = bot.get_response(message)
           print(bot_response) 
          except(KeyboardInterrupt, EOFError, SystemExit):
              break




