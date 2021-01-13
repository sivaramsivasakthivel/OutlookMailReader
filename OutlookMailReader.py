import win32com.client
import twilio_Sms_send
outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")
inbox = mapi.GetDefaultFolder(6)
unread=0
finalMsg = ""
for  message in inbox.Items:
    if message.UnRead == True:
        unread=unread+1 
        
print ("Number of unread mails: {} ".format(unread) )       
for  message in inbox.Items:  
    if (unread == 1) and (message.UnRead):        
        msgSubject=message.Subject
        msgSender=message.Sender
        finalMsg= "Received a new mail with Subject: {} from {}.Please check.".format(msgSubject,msgSender)
        twilio_Sms_send.send_twil_msg(finalMsg)
        print (finalMsg)    
    
if unread > 1 :  
        finalMsg = "Total number of unread mails is {}.Please check".format(unread)
        print (finalMsg)
        

    