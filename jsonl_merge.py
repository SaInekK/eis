import sys
import jsonlines

path_to_log_1, path_to_log_2 = sys.argv[1:3]
path_to_output = sys.argv[4]

reader_1 = jsonlines.open(path_to_log_1)
reader_2 = jsonlines.open(path_to_log_2)
writer = jsonlines.open(path_to_output, mode='w')

try:
    e1 = reader_1.read()
except EOFError:
    e1 = {'timestamp': ''}
    
try:
    e2 = reader_2.read()
except EOFError:
    e2 = {'timestamp': ''}

while e1['timestamp'] or e2['timestamp']:
    if e1['timestamp'] <= e2['timestamp'] and e1['timestamp'] or not e2['timestamp']:
        writer.write(e1)
        try:
            e1 = reader_1.read()
        except EOFError:
            e1 = {'timestamp': ''}

    else: # elif e1['timestamp'] > e2['timestamp'] and e2['timestamp'] != '' or e1['timestamp'] == '':
        writer.write(e2)
        try:
            e2 = reader_2.read()
        except EOFError:
            e2 = {'timestamp': ''}

reader_1.close()
reader_2.close()
writer.close()