import telegram_send
import sys
import os

cron_job_name = sys.argv[len(sys.argv)-1]

#saving the execution time in a temp file
os.system('{ time python3 ' + cron_job_name + ' ; } 2> .temp')

#getting the executiin time value out of the temp file
fd = os.open('.temp', os.O_RDONLY)
value = str(os.read(fd, os.path.getsize('.temp')))
value = value.split('elapsed')[0].split(':')[1]
value = float(value)

#for displaying a human readable message
hours = int(value / 60 / 60)
minutes = int((value / 60 % 60))
seconds = int(((value % 3600) %60))
string = '[ DONE ] ' + cron_job_name + ' [ ' + str(hours) + ' h '+ str(minutes) + ' min '+ str(seconds) + ' sec ]'

#deleting the temp file
os.system('rm .temp')

#send the message
telegram_send.send(messages=[string])
