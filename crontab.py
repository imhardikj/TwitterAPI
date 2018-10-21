from crontab import CronTab

cron = CronTab(tabfile='filename.tab') 
job = cron.new(command='trnds.py')  
job.minute.every(1)

cron.write()

