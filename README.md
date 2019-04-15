# PDI-TweetMaster

>Thanks taking your time in finding TweetMaster!
>
>This RESTful API is a college's project, so expect mediocre code and a lot of to-do's.
>
>Autors: Federico Calonge, Juan David, Gabriel Torrandella
>
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

To add a _cron job_ first execute **crontab -e**. This will open a text editor.
Append at the end the following line:
```
*/5 * * * * cd {path to TweetMaster root} && PYTHONPATH Scheduler/scheduler.py
```

Where:
 * "path to TweetMaster root" is the path from root to the TweetMaster's root directory
   * /dir1/dir2/dir3/TweetMaster
 * PYTHONPATH is the Python 3 interpreter's path
   * If you are _not_ using a virtual enviroment, replace this with _python3_
   * If you _are_ using a virtual enviroment, get the path executing **which python3** when working on the enviroment.

### Optional: Setting up the Swagger tool

There is a Swagger documentation for TweetMaster. It's a server bundled with the app.  
To run the server, please execute the following from the root directory:

```
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/FedericoCalonge/TweetMaster/1.0.0/ui/
