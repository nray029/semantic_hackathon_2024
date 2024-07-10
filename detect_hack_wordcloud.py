#!/usr/bin/python

#this is used to generate wordcloud by calculating the frequencies of the words in  "word" list and the number of fulltext articles. 

import xlrd2
import xlsxwriter
import re
from colour import Color
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np


file_handle1=xlsxwriter.Workbook("states_final.xlsx") 
sheet1=file_handle1.add_worksheet()

file_handle2=xlsxwriter.Workbook("states_frequency.xlsx")
sheet2=file_handle2.add_worksheet()
words=['Andhra Pradesh', 'Arunachal Pradesh', ' Assam ', ' Bihar ', 'Chhattisgarh', ' Goa ', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala ', 'Maharashtra', 'Madhya Pradesh', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha ', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Telangana', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Andaman ', ' Nicobar', 'Chandigarh', 'Dadra ',  'Nagar Haveli', ' Daman ' ' Diu ', 'Delhi ', 'Jammu', ' Kashmir', 'Ladakh ', 'Lakshadweep', 'Puducherry']

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
for d in di.keys():
	d_key=di[d]
	for p in words:
		p=p.lower()
		if p in d:
							

						#for p in words:

			if d not in lines:				
							#if p in i:
				count=count+1				#count=count+1
				print(p, d)					#if uni_id not in listing:
									#listing.append(uni_id)
				sheet1.write(count,0,p)
				sheet1.write(count,1,d_key)
				sheet1.write(count,2,d)
				lines.append(d)
				if p not in word_listing.keys():
					word_listing[p]=1.0
				else:
					word_listing[p]=word_listing[p]+1.0
				if p not in word_color.keys():
					word_color[p]=[]
				if d_key not in word_color[p]:
					word_color[p].append(d_key)
				
file_handle1.close()
word_coloring={}
abstract=[]
for j in word_color.keys():
	word_coloring[j]=len(word_color[j])
	if len(word_color[j]) not in abstract:
		abstract.append(len(word_color[j]))

max_abs=max(abstract)
min_abs=min(abstract)
max_min=max_abs-min_abs+1
white=Color("black")
red=Color("red")
color_towords={}	
colors=list(red.range_to(white,max_min))
for words, abst in word_coloring.items():
	abst=int(abst)-min_abs
	color=str(colors[abst])
	color_towords[words]=color	
print ("color", color_towords)

word_list1={}

w_count=0
sheet2.write(0,0,'word')
sheet2.write(0,1,'frequency')
sheet2.write(0,2,'abstract')
sheet2.write(0,3,'average')
for j in word_listing.keys():
	w_count=w_count+1
	a=word_listing[j]
	b=word_coloring[j]
	c=a/b
	c=round(c,0)
	word_list1[j]=c
	sheet2.write(w_count,0,j)
	sheet2.write(w_count,1,a)
	sheet2.write(w_count,2,b)
	sheet2.write(w_count,3,c)
print(word_coloring, word_list1)

def cloud(sample):
	print ("sample", sample)
	plt.figure()
	plt.ion()
	plt.imshow(sample, interpolation="bilinear")
	plt.margins(x=0, y=0)
	plt.axis('off')
	plt.tight_layout(pad=0)
	plt.ioff()	
	plt.show()
					
class Colouring_function(object):
	 
    def __init__(self, color_towords):
        self.word_to_color = {}
			#word: color
                         #     for (color, words) in color_towords.items()
                          #    for word in words}
        for color,words in color_towords.items():
            for word in words:
                self.word_to_color[word]=color
       # print ("wprd_to_color", self.word_to_color)

    def __call__(self, word, **kwargs):
        #print ("self.word_to_color",self.word_to_color, word, type(word))
       
        return self.word_to_color.get(word)

def setListOfcolor_func(word=None, font_size=None,  
                     position=None, orientation=None,  
                     font_path=None, random_state=None):  
    #define the list of set colors  
    color_list = ["red", "#FFFFFF", "#000000", "skyblue", "yellow"]  
    #print(color_towords, word)	
    #return a random color in the list  
    return color_towords[word] 
def function_generate_wordcloud(quad, color_towords):
	wc = WordCloud(background_color="white",width=1000,height=1000,colormap="copper", relative_scaling=0.5, normalize_plurals=False, color_func=setListOfcolor_func).generate_from_frequencies(quad)
	#print("++++++++++++", color_towords)
	grouped_color_func=Colouring_function(color_towords)
	#wc.recolor(color_func=grouped_color_func)
	cloud(wc)
function_generate_wordcloud(word_list1, color_towords)
file_handle2.close()
