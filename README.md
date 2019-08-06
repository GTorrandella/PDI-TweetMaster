# PDI-TweetMaster

>Thanks taking your time in finding TweetMaster!
>
>This RESTful API is a college's project, so expect mediocre code and a lot of to-do's.
>
>Autors: Federico Calonge, Juan David, Gabriel Torrandella
>
>Professor: Juan Lagostena

## Description

TweetMaster is a little tweet feching service. The users can create "campaigns" based around any hashtag or Twitter user, and define a look-up period for each campaign. During the look-up period for each campaign, TweetMaster will collect all the tweets that have any of the campaign's hashtags, mention or originate from any of the campaign's user.

TweetMaster consist of 2 parts: the client facing API, which manages the client request and creates the reports; and the Twitter facing backend, which manage the tweet's recolection and storage.

## Setting Up TweetMaster

### Requirements

 * Docker, the comunity edition works
   * https://docs.docker.com/install/
 * Docker Compose version 1.24.0+
   * https://docs.docker.com/compose/install/

## Execution

On the project root folder, execute:
```
$ docker-compose up
```

## Testing

#### API Request with Postman
_MISSING_

#### Logger Interface
_MISSING_
