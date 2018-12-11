# PDI-TweetMaster



### Setting up the database

TweetMaster uses a MySQL datebase during operations.  
Fortunately, the necesary set-up is controlled by the app during it's first execution.  
Worry no more!

### Setting up the scheduler

The Scheduler is a small Python module accessed once every 5 minutes.  
To do that, it is necesary to create a _cron job_ that executes the module every 5 minutes.

First, look up the Python 3 path using **which**. If you are using a virtual enviroment, executute this command while working on it.  
>which python3

This will return your Python 3 path.

Now add a the next cron job. (To add a cron job, use **crontab -e**):  
>*/5 * * * * PYTHONPATH {path to scheduler.py}/scheduler.py
