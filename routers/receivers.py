from flask import Blueprint
from controllers.receivers import *
from flask import render_template ,Flask , redirect, url_for ,request
from models.receiverModel import * 
receiver = Blueprint("receivers" , __name__, static_folder="static", template_folder="template")

@receiver.route("/", methods = ["GET"])
def generalInfo():
   return generalReceiverInformation()



@receiver.route("/addReceiver" , methods=["GET" , "POST"])
def receiver_add_page():
    if request.method == "POST":
       form_receiverId = request.form["receiverId"]
       form_playId = request.form["playId"]
       form_teamId = request.form["teamId"]
       form_playerId = request.form["playerId"]
       form_recPosition = request.form["recPosition"]
       form_recYards = request.form["recYards"]
       form_rec = request.form["rec"]
       form_recYac = request.form["recYac"]
       form_rec1Down = request.form["rec1Down"]
       form_recFumble= request.form["recFumble"]
       form_recPassDef = request.form["recPassDef"]
       form_recPassInt = request.form["recPassInt"]
       form_recEn = request.form["recEn"]
       
       new_receiver = Receiver(form_receiverId,form_playId,form_teamId,form_playerId,form_recPosition,form_recYards,form_rec,form_recYac,form_rec1Down,form_recFumble,form_recPassDef,form_recPassInt,form_recEn)
       receiverAdder(new_receiver)
       return redirect("/stats/receivers")
    else :
       return render_template("addReceiver.html")
       
@receiver.route("/deleteReceiver" , methods = ["GET" , "POST"])
def receiver_delete(): 
    if request.method == 'POST':
        form_receiverId=request.form['receiverId']
        receiverDelete(form_receiverId)
        return redirect("/stats/receivers")
    else: 
        return render_template("deleteReceiver.html")
        
@receiver.route("/updateReceiver" , methods=["GET" , "POST"])
def receiver_update():
    if request.method == "POST":
        form_receiverId = request.form["receiverId"]
        form_playId = request.form["playId"]
        form_teamId = request.form["teamId"]
        form_playerId = request.form["playerId"]
        form_recPosition = request.form["recPosition"]
        form_recYards = request.form["recYards"]
        form_rec = request.form["rec"]
        form_recYac = request.form["recYac"]
        form_rec1Down = request.form["rec1Down"]
        form_recFumble= request.form["recFumble"]
        form_recPassDef = request.form["recPassDef"]
        form_recPassInt = request.form["recPassInt"]
        form_recEn = request.form["recEn"]
        
        formObject = Receiver(form_receiverId,form_playId,form_teamId,form_playerId,form_recPosition,form_recYards,form_rec,form_recYac,form_rec1Down,form_recFumble,form_recPassDef,form_recPassInt,form_recEn)
        receiverList = getQuery(form_receiverId)
        print(receiverList)
        
        oldRowObject = Receiver(receiverList[0][0],receiverList [0][1],receiverList[0][2],receiverList[0][3],receiverList[0][4],receiverList[0][5],receiverList[0][6],receiverList[0][7],receiverList[0][8],receiverList[0][9],receiverList[0][10],receiverList[0][11],receiverList[0][12])

        if formObject.receiverId  != "":
            oldRowObject.receiverId=formObject.receiverId
        if formObject.playId  != "":
            oldRowObject.playId=formObject.playId
        if formObject.teamId != "":
            oldRowObject.teamId=formObject.teamId
        if formObject.playerId  != "":
            oldRowObject.playerId=formObject.playerId
        if formObject.recPosition  != "":
            oldRowObject.recPosition=formObject.recPosition
        if formObject.recYards  != "":
            oldRowObject.recYards=formObject.recYards
        if formObject.rec  != "":
            oldRowObject.rec=formObject.rec
        if formObject.recYac  != "":
            oldRowObject.recYac=formObject.recYac
        if formObject.rec1Down != "":
            oldRowObject.rec1Down=formObject.rec1Down    
        if formObject.recFumble  != "":
            oldRowObject.recFumble=formObject.recFumble
        if formObject.recPassDef  != "":
            oldRowObject.recPassDef=formObject.recPassDef    
        if formObject.recPassInt  != "":
            oldRowObject.recPassInt=formObject.recPassInt    
        if formObject.recEn  != "":
            oldRowObject.recEn=formObject.recEn   
        
        receiverUpdate(oldRowObject)
                
          
            
            
            
            
                
        '''
        dataArray = []
        form_receiverId = request.form["receiverId"]
        if form_receiverId == "":
            dataArray.append(-69)
        else:   
            dataArray.append(form_receiverId)  
            form_playId = request.form["playId"]
        if form_playId ==  "":
            dataArray.append(-69)
        else:    
            dataArray.append(form_playId)
        form_teamId = request.form["teamId"]
        if form_teamId ==  "":
            dataArray.append(-69)
        else: 
            dataArray.append(form_teamId)
        form_playerId = request.form["playerId"]
        if form_playerId ==  ""  :
             dataArray.append(-69)
        else: 
            dataArray.append(form_playerId)
        form_recPosition = request.form["recPosition"]
        if form_recPosition ==  "" :
             dataArray.append(-69)
        else: 
            dataArray.append(form_recPosition)
        form_recYards = request.form["recYards"]
        if form_recYards ==  "" :
             dataArray.append(-69)
        else: 
            dataArray.append(form_recYards)
        form_rec = request.form["rec"]
        if form_rec ==  "" :
             dataArray.append(-69)
        else: 
            dataArray.append(form_rec)
        form_recYac = request.form["recYac"]
        if form_recYac ==  "" :
             dataArray.append(-69)
        else: 
            dataArray.append(form_recYac)
        form_rec1Down = request.form["rec1Down"]
        if form_rec1Down ==  "" :
             dataArray.append(-69)
        else: 
            dataArray.append(form_rec1Down)
        form_recFumble= request.form["recFumble"]
        if form_recFumble ==  "" :
             dataArray.append(-69)
        else: 
            dataArray.append(form_recFumble)
        form_recPassDef = request.form["recPassDef"]
        if form_recPassDef ==  "" :
             dataArray.append(-69)
        else: 
            dataArray.append(form_recPassDef)
        form_recPassInt = request.form["recPassInt"]
        if form_recPassInt ==  "" :
             dataArray.append(-69)
        else: 
            dataArray.append(form_recPassInt)
        form_recEn = request.form["recEn"]
        if form_recEn ==  "" :
            dataArray.append(-69)
        else: 
            dataArray.append(form_recEn)
    
       
       
        print(dataArray)
        #form_receiver = Receiver(form_receiverId,form_playId,form_teamId,form_playerId,form_recPosition,form_recYards,form_rec,form_recYac,form_rec1Down,form_recFumble,form_recPassDef,form_recPassInt,form_recEn)
        oldRowList = getQuery(form_receiverId)
        oldRowList=json.loads(oldRowList)
        finalList = []
        
        for i in range (len(dataArray)):
           # finalList.append(dataArray)
            if dataArray[i] == -69:
               finalList.append(oldRowList[i])
            else: 
               finalList.append(dataArray[i])  
        
        updateReceiver(finalList)
      # new_receiver = Receiver(form_receiverId,form_playId,form_teamId,form_playerId,form_recPosition,form_recYards,form_rec,form_recYac,form_rec1Down,form_recFumble,form_recPassDef,form_recPassInt,form_recEn)
       '''
        return redirect("/stats/receivers")
    else:
        return render_template("updateReceiver.html")