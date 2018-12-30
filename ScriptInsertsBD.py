#Script para insertar Campaigns y Tweets de prueba:
import json
from Manager import manager

#Insercion de 10 Campaigns:
userCampaignInput1= '{"email":"activa@gmail.com","hashtags": ["#noBorrrar", "#412"], "mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], "startDate":"16 12 2018 18:22:00", "endDate":"10 01 2019 18:22:00"}'
campaignFields1 = json.loads(userCampaignInput1) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields1)

userCampaignInput2= '{"email":"activaConTw@gmail.com","hashtags": ["#tieneTw", "#noBorrarNada", "#412"], "mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], "startDate":"22 12 2018 18:22:00", "endDate":"10 01 2019 18:22:00"}'
campaignFields2 = json.loads(userCampaignInput2) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields2)

userCampaignInput3= '{"email":"finalizadaConTw@gmail.com","hashtags": ["#tieneTw", "#borrarTodo", "#200"], "mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], "startDate":"16 12 2018 18:22:00", "endDate":"28 12 2018 18:22:00"}'
campaignFields3 = json.loads(userCampaignInput3) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields3)

userCampaignInput4= '{"email":"noEmpezada@gmail.com","hashtags": ["#borrar", "#200"], "mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], "startDate":"10 01 2019 18:22:00", "endDate":"20 01 2019 18:22:00"}'
campaignFields4 = json.loads(userCampaignInput4) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields4)

userCampaignInput5= '{"email":"finalizada@gmail.com","hashtags": ["#borrar", "#200"], "mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], "startDate":"24 12 2018 18:22:00", "endDate":"25 12 2018 18:22:00"}'
campaignFields5 = json.loads(userCampaignInput5) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields5)

userCampaignInput6= '{"email":"noEmpezadaConTw@gmail.com","hashtags": ["#tieneTw", "#borrarTodo", "#200"], "mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], "startDate":"10 01 2019 18:22:00", "endDate":"20 01 2019 18:22:00"}'
campaignFields6 = json.loads(userCampaignInput6) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields6)

userCampaignInput7= '{"email":"activaConTw@gmail.com","hashtags": ["#tieneTw", "#noBorrarNada", "#412"], "mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], "startDate":"22 12 2018 18:22:00", "endDate":"10 01 2019 18:22:00"}'
campaignFields7 = json.loads(userCampaignInput7) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields7)

userCampaignInput8= '{"email":"finalizadaConTw@gmail.com","hashtags": ["#tieneTw", "#borrarTodo", "#200"], "mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], "startDate":"16 12 2018 18:22:00", "endDate":"28 12 2018 18:22:00"}'
campaignFields8 = json.loads(userCampaignInput8) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields8)

userCampaignInput9= '{"email":"mezclada@gmail.com","hashtags": ["#borrar", "#200"], "mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], "startDate":"24 12 2018 18:22:00", "endDate":"25 12 2018 18:22:00"}'
campaignFields9 = json.loads(userCampaignInput9) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields9)

userCampaignInput10= '{"email":"mezclada@gmail.com","hashtags": ["#noBorrrar", "#412"], "mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], "startDate":"16 12 2018 18:22:00", "endDate":"10 01 2019 18:22:00"}'
campaignFields10 = json.loads(userCampaignInput10) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields10)

#Insercion de 10 Tweets:

#Inserción de Tweets en campaña 2:
tweet1 = {
    "id_str" : "223",
    "user" : {"name" : "NASAOk", "id_str" : "789456"},
    "entities" : {"hashtags" : ["#mars","#venus","#earth"],"user_mentions" : ["@NASA", "@planets"]},
    "created_at" : "Sun Mar 20 15:11:01 +0000 2018"
}

tweet2 = {
    "id_str" : "224",
    "user" : {"name" : "MiauricioOK", "id_str" : "451325"},
    "entities" : {"hashtags" : ["#DonaldNoMeDejes"],"user_mentions" : ["@donaldTrump", "@G20"]},
    "created_at" : "Sun Mar 20 21:08:01 +0000 2018"
}

tweetsJson = [json.dumps(tweet1),json.dumps(tweet2)]
manager.Manager().insertTweets(tweetsJson, 2)

#Inserción de Tweets en campaña 3:
tweet3 = {
    "id_str" : "323",
    "user" : {"name" : "NASAOk", "id_str" : "789456"},
    "entities" : {"hashtags" : ["#mars", "#venus", "#earth"],"user_mentions" : ["@NASA", "@planets"]},
    "created_at" : "Sun Mar 20 15:11:01 +0000 2018"
}

tweet4 = {
    "id_str" : "324",
    "user" : {"name" : "MiauricioOK", "id_str" : "451325"},
    "entities" : {"hashtags" : ["#DonaldNoMeDejes"],"user_mentions" : ["@donaldTrump", "@G20"]},
    "created_at" : "Sun Mar 20 21:08:01 +0000 2018"
}

tweetsJson = [json.dumps(tweet3),json.dumps(tweet4)]
manager.Manager().insertTweets(tweetsJson, 3)

#INserción de Tweets en campaña 6:
tweet5 = {
    "id_str" : "623",
    "user" : {"name" : "NASAOk", "id_str" : "789456"},
    "entities" : {"hashtags" : ["#mars", "#venus", "#earth"],"user_mentions" : ["@NASA", "@planets"]},
    "created_at" : "Sun Mar 20 21:08:01 +0000 2018"
}

tweet6 = {
    "id_str" : "624",
    "user" : {"name" : "MiauricioOK", "id_str" : "451325"},
    "entities" : {"hashtags" : ["#DonaldNoMeDejes"],"user_mentions" : ["@donaldTrump", "@G20"]},
    "created_at" : "Sun Mar 20 21:08:01 +0000 2018"
}

tweetsJson = [json.dumps(tweet5),json.dumps(tweet6)]
manager.Manager().insertTweets(tweetsJson, 6)

#Inserción de Tweets en campaña 7:
tweet7 = {
    "id_str" : "724",
    "user" : {"name" : "MiauricioOK", "id_str" : "451325"},
    "entities" : {"hashtags" : ["#DonaldNoMeDejes"],"user_mentions" : ["@donaldTrump", "@G20"]},
    "created_at" : "Sun Mar 20 21:08:01 +0000 2018"
}

tweet8 = {
    "id_str" : "732",
    "user" : {"name" : "MiauricioOK", "id_str" : "451325"},
    "entities" : {"hashtags" : ["#mars", "#venus", "#earth"],"user_mentions" : ["@NASA", "@planets"]},
    "created_at" : "Sun Mar 20 21:08:01 +0000 2018"
}

tweetsJson = [json.dumps(tweet7),json.dumps(tweet8)]
manager.Manager().insertTweets(tweetsJson, 7)

#INserción de Tweets en campaña 8:
tweet9 = {
    "id_str" : "845",
    "user" : {"name" : "NASAOk", "id_str" : "451325"},
    "entities" : {"hashtags" : ["#DonaldNoMeDejes"],"user_mentions" : ["@donaldTrump", "@G20"]},
    "created_at" : "Sun Mar 20 21:08:01 +0000 2018"
}

tweet10 = {
    "id_str" : "895",
    "user" : {"name" : "MiauricioOK", "id_str" : "789456"},
    "entities" : {"hashtags" : ["#mars", "#venus", "#earth"],"user_mentions" : ["@NASA", "@planets"]},
    "created_at" : "Sun Mar 20 21:08:01 +0000 2018"
}

tweetsJson = [json.dumps(tweet9),json.dumps(tweet10)]
manager.Manager().insertTweets(tweetsJson, 8)
