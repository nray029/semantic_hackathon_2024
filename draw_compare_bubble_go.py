#!/usr/bin/python


import xlrd2
import xlsxwriter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import draw_heatmap

final_x1=[]
final_y1=[]
list_list={}

book1= xlrd2.open_workbook("/home/manisha/nikita_19mar2020/Nikita/Proseq/heatmap_states_keyword_new.xlsx")
sheet1=book1.sheet_by_index(0)


x=[]
y=[]
z=[]
a=[]
final_x=[]
final_y=[]
listing_1=[]

for r in range(sheet1.nrows):
	if r>0:
		listing2=[]
		for t in range(sheet1.ncols):
			if t>0:
				
				
				x_val=sheet1.cell_value(r,0)
				x_val=x_val.strip()
				if x_val not in final_x:
					final_x.append(x_val)
				if x_val not in list_list.keys():
					list_list[x_val]=[]
					final_x1.append(x_val)
				
				y_val=sheet1.cell_value(0,t)
				y_val=str(y_val)
				y_val=y_val.strip()
				if y_val not in final_y:
					final_y.append(y_val)
				y_value=y_val
				if y_value not in final_y1:
					final_y1.append(y_value)
				
				c_val=sheet1.cell_value(r,t)
				#c_val=(c_val/n_val)*100
				
				listing2.append(c_val)
				list_list[x_val].append(c_val)
				if c_val!=0:
					
						
					z_val=c_val*30
					z_val=int(z_val)
					x.append(x_val)
					y.append(y_val)
					z.append(z_val)
					#a.append()
		
		listing_1.append(listing2)
listing=np.array(listing_1)
np.transpose(listing)
print("listing",listing)
draw_heatmap.plot_heatmap(listing, final_x, final_y, "YlGn", "Number of families", "States and keyword sentences ")
	
plt.xlabel("")
plt.ylabel("cluster")
c_top="N-terminal families distribution in "
plt.title(c_top)
	#plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")


# show the graph
#plt.show()
