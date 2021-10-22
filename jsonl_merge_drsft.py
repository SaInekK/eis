# import json
# import sys
# import jsonlines
# import gc


# i, j = 0, 0
# path_to_log_1, path_to_log_2 = sys.argv[1:3]
# path_to_output = sys.argv[4]
# print(sys.argv)
# for e in sys.argv:
#     print(e)
# # print(path_to_log_1, path_to_log_2)
# with jsonlines.open(path_to_log_1) as reader_1:
#     list_1 = list(reader_1)
#     len_1 = len(list_1)
#     del reader_1

# with jsonlines.open(path_to_log_2) as reader_2:
#     list_2 = list(reader_2)
#     len_2 = len(list_2)
#     del reader_2
    
# gc.collect()

# with jsonlines.open(path_to_output, mode='w') as writer:
#     # while
#     res = []
#     while list_1 and list_2:
#         if list_1[0]['timestamp'] < list_2[0]['timestamp']:
#             res.append(list_1.pop(0))
#             # i += 1
    
#         else:
#             res.append(list_2.pop(0))
#             # j += 1
    
#     res.extend(list_1[i:])
#     res.extend(list_2[j:])
#     for e in res:
#         # print(e)
#         writer.write(e)

# import json
'''import sys
import jsonlines
import gc
import ijson

i, j = 0, 0
path_to_log_1, path_to_log_2 = sys.argv[1:3]
path_to_output = sys.argv[4]

print(sys.argv)
for e in sys.argv:
    print(e)
with jsonlines.open(path_to_log_1) as reader_1:
    list_1 = list(reader_1)
    len_1 = len(list_1)
    del reader_1

with jsonlines.open(path_to_log_2) as reader_2:
    list_2 = list(reader_2)
    len_2 = len(list_2)
    del reader_2
gc.collect()

with jsonlines.open(path_to_output, mode='w') as writer:
    # while
    res = []
    while i < len_1 and j < len_2:
        if list_1[i]['timestamp'] < list_2[j]['timestamp']:
            res.append(list_1[i])
            i += 1
    
        else:
            res.append(list_2[j])
            j += 1
    
    res.extend(list_1[i:])
    res.extend(list_2[j:])
    for e in res:
        # print(e)
        writer.write(e)'''

# with open('test1.jsonl', 'r') as f:
#     parser = ijson.parse(f)
#     for prefix, event, value in parser:
#         print(prefix, event, value)


# import csv
# with open('test1.jsonl', newline='\n') as f:
#     jsonreader = csv.reader(f, delimiter=': ', quotechar='"')
#     for row in jsonreader:
#         print(', '.join(row))
#     # for e in f.read():
#     #     print(e)

import sys
import jsonlines
import gc
import ijson

i, j = 0, 0
path_to_log_1, path_to_log_2 = sys.argv[1:3]
path_to_output = sys.argv[4]


with jsonlines.open(path_to_log_1) as reader_1:
    with jsonlines.open(path_to_log_2) as reader_2:
        with jsonlines.open(path_to_output, mode='w') as writer:
            e1 = reader_1.read()
            e2 = reader_2.read()
            while True:
                if e1['timestamp'] < e2['timestamp']:
                    writer.write(e1)
                    try:
                        e1 = reader_1.read()
                    except EOFError:
                        ended = 1
                        break
                else:
                    writer.write(e2)
                    try:
                        e2 = reader_2.read()
                    except EOFError:
                        ended = 2
                        break
            if ended == 1:
                writer.write(e2)
                while True:
                    try:
                        writer.write(reader_2.read())
                    except EOFError:
                        break
                    
            if ended == 2:
                writer.write(e1)
                while True:
                    try:
                        writer.write(reader_1.read())
                    except EOFError:
                        break
            # for e in reader_2:
            #     print(e)



# with jsonlines.open(path_to_output, mode='w') as writer:
#     # while
#     res = []
#     while i < len_1 and j < len_2:
#         if list_1[i]['timestamp'] < list_2[j]['timestamp']:
#             res.append(list_1[i])
#             i += 1
    
#         else:
#             res.append(list_2[j])
#             j += 1
    
#     res.extend(list_1[i:])
#     res.extend(list_2[j:])
#     for e in res:
#         # print(e)
#         writer.write(e)