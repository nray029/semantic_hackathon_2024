#!/usr/bin/python


#the script is used to generate networks among the keywords mentioned in "word" list in all the files in "file_name". 


import xlrd2
import xlsxwriter
import re
from colour import Color
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import plurals_new

import networkx as nx

file_handle1=xlsxwriter.Workbook("states_fulltext_8jul.xlsx") 
sheet1=file_handle1.add_worksheet()


word=['delhi ', 'west bengal', ' assam ', ' kashmir', 'himachal pradesh', 'arunachal pradesh', 'jammu', 'uttarakhand', 'gujarat', 'sikkim', 'kerala ', 'tamil nadu', 'punjab', ' bihar ', 'haryana', 'andaman ',  'andhra pradesh', 'karnataka', 'telangana', 'mizoram', 'rajasthan', 'maharashtra', 'chhattisgarh', 'jharkhand', 'madhya pradesh', 'uttar pradesh', 'chandigarh', 'odisha ', ' goa ', 'puducherry', 'manipur']


words=[]
for r in word:
	r=r.strip()
	r=r.lower()
	if r not in words:
		words.append(r)


print(len(words))
file_name=['Effect_of_climate_change_in_precipitation_fulltext', 'Increased_rainfall_in_India_fulltext', 'Agriculture_on_different_types_of_soils_in_India_fulltext', 'Plant_effect_fulltext', 'Precipitation_in_India_fulltext', 'Nitrogen_cycle_fulltext', 'IPCC_SR15_fulltext', 'Precipitation_on_India_agriculture_fulltext', 'IPCC_wg2_fulltext', 'Phosphorus_cycle_fulltext', 'Effects_of_disturbed_precipitation_on_different_soils_fulltext', 'Ecosystem_effects_fulltext', 'Microbes_effect_fulltext', 'Different_types_of_soil_in_India_fulltext', 'Decreased_rainfall_in_India_fulltext', 'IPCC_wg1_fulltext']





line=''
count_pm=0
di={}
tag=0
listing=[]

for t in file_name:		
	file_n="/home/manisha/nikita_19mar2020/Nikita/Proseq/"+t+".txt"
	file_open=open(file_n,"r")		
	for y in file_open:
		y=y.lower()
		findpm=re.findall("^start----",y)
		y=y.strip()
		y=y+" "
		line=line+y
		if findpm:
			pm_list=y.split(" ")
			pm_id=pm_list[1]
			pm_id=pm_id.strip()
			count_pm=count_pm+1
			line_list=line.split(". ")

			uid=pm_id
								
		
		
				
			for l in line_list:
				di[l]=uid+str(count_pm)
	
			line=''
		

#for r in range(sheet0.nrows):
	#if r>0  and r<6:	
	#	listing=[]
	#	uni_id=sheet0.cell_value(r,0)
	#	uni_id=uni_id.strip()
	#	pro_name=sheet0.cell_value(r,1)
	#	pro_name=pro_name.strip()
	#	pro_name=pro_name.lower()
	#	org_name=sheet0.cell_value(r,4)
	#	org_name=org_name.strip()
	#	org_name=org_name.lower()
	#	org_list=org_name.split(" (")
	#	o=0
	#	print(uni_id, pro_name)
	#	c_pm=0
	#	for k in org_list:
	#		o=o+1
	#		if o>1:
	#			k=k[:-1]

			
			
	#		count=0

	
			
word_listing={}	
word_color={}		
count=0			
lines=[]
p_list={}
t_list={}				
for d in di.keys():
	d_key=di[d]
	for p in words:
		tag1=0
		p=p.lower()
		for t in words:
			t=t.lower()
			tag2=0
			if t!=p:
				if (p in d) and (t in d):
					if p not in p_list.keys():
						p_list[p]=[]
					if d_key not in p_list[p]:
						p_list[p].append(d_key)
			
					if t not in t_list.keys():
						t_list[t]=[]
					if d_key not in t_list[t]:
						t_list[t].append(d_key)

for p in words:	
	p=p.lower()
	if p in p_list.keys():
		p_l=p_list[p]
		for t in words:
			t=t.lower()
			if t in t_list.keys():
				t_l=t_list[t]
				for p_val in p_l:
					if p_val in t_l:			
				
						if p not in word_listing.keys():
							word_listing[p]={}
							if t not in word_listing[p].keys():
								word_listing[p][t]=1
							else:
								word_listing[p][t]+=1
						else:
							if t not in word_listing[p].keys():
								word_listing[p][t]=1
							else:
								word_listing[p][t]+=1
		





file_handle1.close()



print(word_listing)
connect_list=[]
G = nx.Graph()
for j in word_listing.keys():
	for r in word_listing[j].keys():
		pairing=j+"_"+r
		pairing2=r+"_"+j
		if (pairing not in connect_list) and pairing2 not in connect_list:
			
			wei=word_listing[j][r]
			if wei>5:
				G.add_edge(j,r,weight=wei)
				connect_list.append(pairing)

			print(j, r, wei)
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] >10]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 10]

pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='peachpuff')

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=2, edge_color='r')
nx.draw_networkx_edges(G, pos, edgelist=esmall, width=2, alpha=0.5, edge_color="b")

# node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", font_color='k')
# edge weight labels
#edge_labels = nx.get_edge_attributes(G, "weight")
#nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
