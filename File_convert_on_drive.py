import os
import shutil


os.chdir('/content/drive/MyDrive/hackathon_mriirs/Plant_effect')

listing=os.listdir()
file2= open("Plant_effect_fulltext.txt","w")
print(listing)
list_count=0
for k in listing:

  k1="/content/drive/MyDrive/hackathon_mriirs/Plant_effect/"+k+"/fulltext.pdf"
  k2="/content/drive/MyDrive/hackathon_mriirs/Plant_effect/fulltext.pdf"
  try:
    shutil.copyfile(k1, k2)
    !pyamihtmlx PDF --infile /content/drive/MyDrive/hackathon_mriirs/Plant_effect/fulltext.pdf --outdir /content/drive/MyDrive/hackathon_mriirs/Plant_effect
    file1=open("raw.html","r")
    list_count=list_count+1
    list_start="start----"+str(list_count)
    file2.write("\n")
    file2.write(list_start)
    file2.write("\n")
    for r in file1:
      file2.write(r)
  except:
    "no file"

list_count=list_count+1
list_start="start----"+str(list_count)
file2.write("\n")
file2.write(list_start)




