### START 1: href_list link creation
# Using 'BeautifulSoup', a local html file is parsed using lxml.
# 'BeautifulSoup' iterates and stores in variable 'href_list' all of the 'a' tags containing the 'href' attribute.
# Variable 'href_list' is reconstructed with 'duplicates', 'NoneTypes', and items not containing the 'https://www.youtube.com/watch?v=' value removed.
import lxml
from bs4 import BeautifulSoup

with open('E:/Videos/Projects/canitruncrysis/application/Linus Tech Tips - YouTube.html', 'r', encoding='UTF-8') as f:
    href_list = []
    for i in BeautifulSoup(f.read(),'lxml').findAll('a'):
        href_list.append(i.get('href'))
"""
href_list = [i for n, i in enumerate(href_list) if i not in href_list[:n]]
href_list = [i for i in href_list if i]
href_list = [i for i in href_list if i.startswith('https://www.youtube.com/watch?v=')]
"""
# below is the above code, but combined for simplicity: (useless explanatory comments for future me)
href_list = [i for i in [i for i in [i for n, i in enumerate(href_list) if i not in href_list[:n]] if i] if i.startswith('https://www.youtube.com/watch?v=')]

# DEBUG 1:
# I oped to use pandas both for personal practice and for better loading time on module 2.
import pandas, os
debug_1 = 'DEBUG 1:'
href_list_counter = 0
for i in href_list:
    print('{} {}'.format(debug_1, i))
    href_list_counter += 1
print('{} Quantity of videos: {}'.format(debug_1, href_list_counter))
export_filename = '1-href_list.csv'
if os.path.exists(export_filename):
    os.remove(export_filename)
    print('{} {} OVERWRITTEN'.format(debug_1, export_filename))
else:
    print('{} {} CREATED'.format(debug_1, export_filename))
pandas.DataFrame(href_list, columns=['Links']).to_csv(export_filename)
debug_pause = input('{} Press [RETURN] to quit.'.format(debug_1))
### END 1: href_list link creation

