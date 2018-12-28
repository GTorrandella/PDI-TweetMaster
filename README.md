# PDI-TweetMaster

>Thanks thanking your time in finding TweetMaster!
>
>This RESTful API is a college's project, so expect mediocre code and a lot of to-do's.
>
>Autors: Federico Calonge, Juan David, Gabriel Torrandella
>Professor: Juan Lagostena

## Setting Up TweetMaster

### Requirements

Python 3.5.2+

Install the packages in here. The easiest way is using **pip3**:

```
pip3 install -r requirements.txt
```

### Setting up the database

TweetMaster uses a MySQL database during operations.  
Fortunately, the necesary set-up is controlled by the app during it's first execution.  
Worry no more!

### Setting up the servers

Execute in diferent terminals _start_manager_, _start_fetcher_ and _start_reporter_, from TweetMaster's root directory.  
The order is indistint.

The servers will live in:  
 * Manger:   127.0.0.1/5000
 * Fetcher:  127.0.0.1/5001
 * Reporter: 127.0.0.1/5002
 
### Setting up the scheduler

The Scheduler is a small Python module accessed once every 5 minutes.  
To do that, it is necesary to create a _cron job_ that executes the module every 5 minutes.

First, look up the Python 3 path using **which**. If you are using a virtual enviroment, executute this command while working on it.  
```
which python3
```
This will return your Python 3 path.

Now add a the next cron job. (To add a cron job, use **crontab -e**):  
```
*/5 * * * * PYTHONPATH {path to scheduler.py}/scheduler.py
```
*/5 * * * * /usr/bin/python3 /Scheduler/scheduler.py 

### Optional: Setting up the Swagger tool

There is a Swagger documentation for TweetMaster. It's a server bundled with the app.  
To run the server, please execute the following from the root directory:

```
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/FedericoCalonge/TweetMaster/1.0.0/ui/
