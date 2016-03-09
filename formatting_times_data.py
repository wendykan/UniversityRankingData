
#Rank    Title
#Teaching
#International Outlook
#Research
#Citations
#Industry Income
#Overall


import os, string
import pandas as pd

filename = 'ranking2011.txt'
textfile = open(filename, 'r')


lines = textfile.readlines()

ranks = []
title = []
country = []
Teaching = []
International = []
Research = []
Citations = []
Income = []
Overall = []


school_index = 0

for (line_index, line) in enumerate(lines):

    words = line.split('\t')

    if line_index % 3 == 0:
        ranks.append(words[0])
        title.append(words[1])
    elif line_index % 3 ==1:
        country.append(words[0])
    elif line_index % 3 ==2:
        Teaching.append(words[0])
        International.append(words[1])
        Research.append(words[2])
        Citations.append(words[3])
        Income.append(words[4])
        Overall.append(words[5])


data = pd.DataFrame([ranks,title,country,Teaching, International, Research, Citations, Income, Overall]).transpose()
data.columns = ['times_rank', 'school_name', 'country', 'times_teaching', 'times_international', 'times_research', 'times_citations','times_income', 'times_overall']

data = data.replace({'\n': ''}, regex=True)
print data
