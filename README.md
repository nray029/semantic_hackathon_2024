**File_convert_on_drive.py**-
The script can be used to convert .pdf files to readable text files on google drive through Google Colab. The Script incorporates one of the semantic climate tool **Pyamihtmlx** which helps to convert these PMC files to HTML.

**all_abstract_info.xlsx**-
This contains two spreadsheets. One with list of all the abstracts from the PubMed which were used to extract tokens while the another with list of all PMC ids for fulltext analaysis

**detect_hack_network.py**- This is a script to analyse the connection networks between two sets of tokens. The tokens are provided into separate python lists while the name of text files are also provided all together through another list
It also has *Matplotlib* module of Python which helps to generate the network graphs.

**detect_hack_wordcloud.py**- This Python script helps to generate wordclouds based on the tokens provided in the python list from the fulltext document. It calculates the number of occurrence of the words and number of articles.
The wordcloud is generated show *font* size as "average frequency" (calculated by Number of occurrence divided by number of articles for the token) and color gradient from *red to black* as number of articles from low to high

**draw_heatmap_analysis.py**- The python script is used to get data from the spreadsheets already listing the results of co-occurrence data of two tokens. It is used along with another module *draw_heatmap.py* which helps to plot the heatmaps.

**draw_heatmap.py**- the python script is used to generate heatmaps using *Matplotlib* module of the python. Heatmaps data can be provided by using *draw_heatmap_analysis.py*

**heatmap_results.xlsx**- The spreadsheets contain data used to generate heatmaps with the name of the type of token as description of the sheet.

**keywords_frequency.xlsx**- The spreadsheets contains the information of the token such as *number of occurrence, average frequency* and *number of articles* which is used to generate wordclouds. 


