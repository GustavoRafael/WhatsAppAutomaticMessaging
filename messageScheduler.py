from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from wAppMessage import whatsAppMsg


sched = BlockingScheduler()

# Schedule job_function to be called every 30s seconds
# the interval can be: seconds(int), minutes(int), 
# hours(int), days(int) and weeks(int)
sched.add_job(whatsAppMsg, 'interval', seconds=30)
sched.start()