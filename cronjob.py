from crontab import CronTab

cron   = CronTab()

job  = cron.new(command='/usr/bin/echo')

job.minute.every(10)
