from datetime import datetime
from DataBaseConnector import configTables
from Campaign.Campaign import Campaign

CONDITION_FOR_ACTIVE_CAMPAIGN = 'configTables.Campaign.startDate < datetime.now() < configTables.Campaign.endDate'

class Connector():

    def __init__(self, context='standar'):
        if context == 'test':
            self.database = configTables.MySQLConfiguration(context='test')
        else:
            self.database = configTables.MySQLConfiguration()
            
    def insertCampaign(self, campaignReceived):
        campaignToInsert = configTables.Campaign(startDate=campaignReceived.startDate, finDate=campaignReceived.finDate,
                                              email=(campaignReceived.emailDueño), hashtags=(campaignReceived.hashtags),
                                              mentions=(campaignReceived.mentions))
        self.database.session.add(campaignToInsert)
        self.database.session.dirty
        self.database.session.commit()  # Para que los cambios se efectivicen en la BD
        return campaignToInsert.id

    def selectCampaignsInProgress(self):
        listaCampaignsBD = self.database.session.query(configTables.Campaign).filter(
            configTables.Campaign.startDate < datetime.now(),
            configTables.Campaign.finDate > datetime.now()).all()
        listaCampaigns = self.campaignsBDListToCampaignsList(listaCampaignsBD)
        return listaCampaigns

    def selectCampaignsByEmail(self, user_email):
        campaignsBD = self.database.session.query(configTables.Campaign).filter_by(email=user_email).all()
        campaigns = self.campaignsBDListToCampaignsList(campaignsBD)
        return campaigns
    
    # Transforma lista de campaigns en formato de sqlalchemy a lista de campaigns
    def campaignsBDListToCampaignsList(self, campaignsBDList):
        campaigns = []
        for cBD in campaignsBDList:
            c = Campaign(cBD.id, cBD.email, cBD.hashtags, cBD.mentions, cBD.startDate, cBD.finDate)
            campaigns.append(c)
        return campaigns
    
    def deleteTweetsByIDC(self, idC):
        tweets = self.database.session.query(configTables.Tweet).filter_by(idCampaign=idC).all()
        for t in tweets:
            self.database.session.delete(t)
        self.database.session.commit()
    
    #OK 200, 412
    def deleteCampaignByID(self, idC):
        campaignABorrar = self.database.session.query(configTables.Campaign).get(idC)
        self.database.session.delete(campaignABorrar)
        self.database.session.commit()
    
    # OK
    def selectCampaign(self, idC):
        campaignEspecifica = self.database.session.query(configTables.Campaign).get(idC)
        if campaignEspecifica is None:
            return []
        return Campaign(campaignEspecifica.id, campaignEspecifica.email, campaignEspecifica.hashtags,
                        campaignEspecifica.mentions, campaignEspecifica.startDate, campaignEspecifica.finDate)
    
    # OK: 200 (falla con inputUser muy largo)
    def updateCampaign(self, idC, inputColumn, inputUser):
        campaignEspecifica = self.database.session.query(configTables.Campaign).get(idC)
        wasModified = False  # Flag que indica si fue modificado
        if inputColumn == "email":
            campaignEspecifica.email = inputUser
            self.database.session.commit()
            wasModified = True
    
        elif inputColumn == "startDate":
            campaignEspecifica.startDate = inputUser
            self.database.session.commit()
            wasModified = True
    
        elif inputColumn == "finDate":
            campaignEspecifica.finDate = inputUser
            self.database.session.commit()
            wasModified = True
    
        elif inputColumn == "hashtags":
            campaignEspecifica.hashtags = self.listaAString(inputUser)
            self.database.session.commit()
            wasModified = True
    
        elif inputColumn == "mentions":
            campaignEspecifica.mentions = self.listaAString(inputUser)
            self.database.session.commit()
            wasModified = True
    
        return wasModified

    
    def insertTweet(self, TweetInput, idC):
        # Insertamos fecha publicacion, autor, mensaje y macheo en la tabla Tweet de la BD:
        stringHashtag = self.listaAString(TweetInput.hashtags)  # #donaldTrump-#G20
        stringMention = self.listaAString(TweetInput.mentions)  # @donaldTrump-@miauricioOK
        # print(TweetInput.ID, TweetInput.userName, TweetInput.userID, TweetInput.hashtags ,TweetInput.mentions, TweetInput.date)
        IDTweet = (TweetInput.ID)
        if self.selectTweetByIDT(IDTweet):
            print("Tweet ya ingresado")
        else:
            UserName = (TweetInput.userName).encode('utf8mb4',
                                                    errors='ignore')  # Hacemos esto por si hay caracteres especiales o emoticonos en el nombre de usuario.
            new_TweetBD = configTables.Tweet(idCampaign=(idC), ID=(IDTweet), userName=(UserName),
                                             userid=(TweetInput.userID), hashtags=(stringHashtag), mentions=(stringMention),
                                             date=(TweetInput.date))
            self.database.session.add(new_TweetBD)
            # Y finalmente las agregamos a la BD con estas 3 lineas:
            self.database.session.new
            self.database.session.dirty
            self.database.session.commit()
    
    
    def selectTweetByIDT(self, idT):
        tweetEspecifico = self.database.session.query(configTables.Tweet).get(idT)
        return tweetEspecifico
    
    
    def selectTweetsByIDC(self, IDC):
        tweetsBD = self.database.session.query(configTables.Tweet).filter_by(idCampaign=IDC).all()
        # tweetsBD es una lista de Tweets en el formato de Tweet de ConfigTables:
        # [<Tweets(ID='112112', userName='MiauricioOK',userid='451325',hashtags='#DonaldNoMeDejes',mentions='@donaldTrump-@G20',date='2018-03-20 21:08:01',idCampaign='3')>,
        # <Tweets(ID='123456', userName='NASAOk',userid='789456',hashtags='#mars-#venus-#earth',mentions='@NASA-@planets',date='2018-03-20 15:11:01',idCampaign='3')>]
    
        # Tenemos que separar los tweets y crear objetos tweets. Y hacerles el to json.
        # Y hacer una lista de esos to json.
        tweets = []
        for t in tweetsBD:
            dictionary = {
                "id_str": t.ID,
                "user": {"name": t.userName, "id_str": t.userid},
                "entities": {"hashtags": t.hashtags, "user_mentions": t.mentions},
                "created_at": t.date,
            }
            tweets.append(dictionary)
        return tweets
    
    
    def listaAString(self, lista):
        string = "-".join(lista)
        return string
