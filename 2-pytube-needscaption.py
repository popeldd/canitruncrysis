# DEBUG pre2:
# If the csv is missing, do not forget to run module 1 indepedently.
# I oped to use pandas both for personal practice and for better loading time while slapping together this module.
import pandas, os, csv
debug_pre2 = 'DEBUG pre2:'

import_filename = '1-href_list.csv'
if os.path.exists(import_filename):
    csv_df = pandas.read_csv(import_filename, names=['Links'])
    href_list = csv_df['Links'].tolist()[1:] # Gosh darn 'List' string keeps plopping itself into my list, so I splitted them indecies :P
    print('{} {} IMPORTED'.format(debug_pre2, import_filename))
else:
    print('{} {} NONEXISTENT'.format(debug_pre2, import_filename))

### START 2: log if captions exist
# The 'pytube' library is unstable and crashes a lot.
# After modifying the original codebase in the pytube directory, I did encounter more stability, but there still are exceptions.
# So, as a workaround, all lines in this section commented with '# pytube workaround' are SLAPPED TOGETHER temporary fixes in releation to this issue.
#
import os, csv, time
from pytube import YouTube

export_caption = '2-caption_list.csv'               # pytube workaround savestate
if os.path.exists(export_caption):                  # pytube workaround savestate
    os.remove(export_caption)
    print('{} OVERWRITTEN'.format(export_caption))
else:                                               # pytube workaround savestate
    print('{} CREATED'.format(export_caption))
def addto_export_caption(i):                        # pytube workaround savestate
    csv.writer(open(export_caption, 'a'), lineterminator='\n').writerow(i)
needscaption_list = []
def search_needscaptions(n, i):
    if n == 4372 or n == 4600 or n == 4627:
        result = 'null'
    else:
        captions = YouTube(href_list[n]).captions
        if 'en' in captions:
            result = 'false'
        else:
            result = 'true'
    needscaption_list.append(result)
    result += ',{}'.format(i)                       # pytube workaround savestate
    addto_export_caption(result.split(','))         # pytube workaround savestate
for n, i in enumerate(href_list):
    try:                                            # pytube workaround
        search_needscaptions(n, i)
    except:                                         # pytube workaround
        try:                                        # pytube workaround
            search_needscaptions(n, i)
        except:                                     # pytube workaround
            try:                                    # pytube workaround
                search_needscaptions(n, i)
            except:                                 # pytube workaround
                try:                                    # pytube workaround
                    search_needscaptions(n, i)
                except:                                 # pytube workaround
                    print('{}: pytube EXCEPTION caught\t{}'.format(n, i))
                    time.sleep(5)
                    search_needscaptions(n, i)

# DEBUG 2:
import pandas
debug_2 = 'DEBUG 2:'

export_filename = '2-href_caption_list.csv'
if os.path.exists(export_filename):
    os.remove(export_filename)
    print('{} {} OVERWRITTEN'.format(debug_2, export_filename))
else:
    print('{} {} CREATED'.format(debug_2, export_filename))
pandas.DataFrame({'Links': href_list,'Needs Caption': needscaption_list}).to_csv(export_filename)
debug_pause = input('{} Press [RETURN] to quit.'.format(debug_2))
### END 2.2: log if captions exist