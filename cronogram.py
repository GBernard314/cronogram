import telegram_send
import sys
import os
import time

cron_job_name = sys.argv[len(sys.argv)-1]

#getting the execution time of the 1st argument
start = time.time()
os.system('python3 ' + cron_job_name)
end = time.time()
duration = float(time.time() - start)

#for displaying a human readable message
hours = int(duration / 60 / 60)
minutes = int((duration / 60 % 60))
seconds = int(((duration % 3600) %60))
string = '[ DONE ] ' + cron_job_name + ' [ ' + str(hours) + ' h '+ str(minutes) + ' min '+ str(seconds) + ' sec ]'

#send the message
telegram_send.send(messages=[string])
