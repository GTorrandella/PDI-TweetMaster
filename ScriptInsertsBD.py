#Script para insertar Campaigns y Tweets de prueba:
import json
from Manager import manager
from DataBaseConnector import configTables

#Insercion de 8 Campaigns:
userCampaignInput1= '{"email":"activa@gmail.com",' \
                    '"hashtags": ["#noBorrrar", "#412"], ' \
                    '"mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], ' \
                    '"startDate":"2018-12-20 18:22:00", ' \
                    '"endDate":"2020-12-20 18:22:00"}'
campaignFields1 = json.loads(userCampaignInput1)
manager.Manager().insertCampaign(campaignFields1)

userCampaignInput2= '{"email":"activaConTw@gmail.com",' \
                    '"hashtags": ["#tieneTw", "#noBorrarNada", "#412"], ' \
                    '"mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], ' \
                    '"startDate":"2018-12-20 18:22:00", ' \
                    '"endDate":"2020-12-20 18:22:00"}'
campaignFields2 = json.loads(userCampaignInput2)
manager.Manager().insertCampaign(campaignFields2)

userCampaignInput3= '{"email":"finalizadaConTw@gmail.com",' \
                    '"hashtags": ["#tieneTw", "#borrarTodo", "#200"], ' \
                    '"mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], ' \
                    '"startDate":"2018-12-20 18:22:00", ' \
                    '"endDate":"2019-03-20 18:22:00"}'
campaignFields3 = json.loads(userCampaignInput3)
manager.Manager().insertCampaign(campaignFields3)

userCampaignInput4= '{"email":"noEmpezada@gmail.com",' \
                    '"hashtags": ["#borrar", "#200"], ' \
                    '"mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], ' \
                    '"startDate":"2020-11-20 18:22:00", ' \
                    '"endDate":"2020-12-20 18:22:00"}'
campaignFields4 = json.loads(userCampaignInput4)
manager.Manager().insertCampaign(campaignFields4)

userCampaignInput5= '{"email":"finalizada@gmail.com",' \
                    '"hashtags": ["#borrar", "#200"], ' \
                    '"mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], ' \
                    '"startDate":"2018-12-20 18:22:00", ' \
                    '"endDate":"2019-03-20 18:22:00"}'
campaignFields5 = json.loads(userCampaignInput5) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields5)

userCampaignInput6= '{"email":"noEmpezadaConTw@gmail.com",' \
                    '"hashtags": ["#tieneTw", "#borrarTodo", "#200"], ' \
                    '"mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], ' \
                    '"startDate":"2020-11-20 18:22:00", ' \
                    '"endDate":"2020-12-20 18:22:00"}'
campaignFields6 = json.loads(userCampaignInput6) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields6)

userCampaignInput7= '{"email":"activaConTw@gmail.com",' \
                    '"hashtags": ["#tieneTw", "#noBorrarNada", "#412"], ' \
                    '"mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], ' \
                    '"startDate":"2018-12-20 18:22:00", ' \
                    '"endDate":"2020-12-20 18:22:00"}'
campaignFields7 = json.loads(userCampaignInput7) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
manager.Manager().insertCampaign(campaignFields7)

userCampaignInput8= '{"email":"finalizadaConTw@gmail.com",' \
                    '"hashtags": ["#tieneTw", "#borrarTodo", "#200"], ' \
                    '"mentions": ["@fedecalongeOK", "@mauriciomacriOKkk"], ' \
                    '"startDate":"2018-12-20 18:22:00", ' \
                    '"endDate":"2019-03-20 18:22:00"}'
campaignFields8 = json.loads(userCampaignInput8)
manager.Manager().insertCampaign(campaignFields8)

#Insercion de 6 Tweets:

#Inserción de Tweets en campaña 4:
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
manager.Manager().insertTweets(tweetsJson, 4)

#Inserción de Tweets en campaña 5:
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
manager.Manager().insertTweets(tweetsJson, 5)

#INserción de Tweets en campaña 8:
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
manager.Manager().insertTweets(tweetsJson, 8)

