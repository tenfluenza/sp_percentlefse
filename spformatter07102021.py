#all the important libraries uwu
from ete3 import NCBITaxa
ncbi = NCBITaxa()
import re
import csv
import pandas as pd
import numpy as np


#paste file paths here vvv
input_file = "/Users/trinitychen/Desktop/wormdata/inbox_outbox/sppercent.csv"
output_file = "/Users/trinitychen/Desktop/wormdata/inbox_outbox/spoutput.csv"
#DO NOT FORGET TO CONVERT TO .TXT (TAB) SEPARATELY OR IT WILL NOT WORK


#PART 1: convert organism names to names and pipes

def sp_formatter(input_file, output_file):
    df = pd.read_csv(input_file)

    list_organisms = df["treatment"] #lists the columns of organisms (no treatment columns)
    #print(list_organisms)

    #go down the lineages and find k_, p_, c_, o_, f_, g_, and collect it in a variable + format
    #concat the variables and replace the cell
    #win
    for x in range(2, len(list_organisms)):
        # finds the corresponding rank symbol in the string and extracts the name only
        # TODO: concat the columns, replace the first column with it, and delete the placeholder columns as you go
        df['f_kingdom'] = list_organisms.str.extract("k__(.*?);", expand=False).str.strip()
        df['f_kingdom'] = df['f_kingdom'].str.replace("(","")

        df['f_phylum'] = list_organisms.str.extract("p__(.*?);", expand=False).str.strip()
        df['f_phylum'] = df['f_phylum'].str.replace("(","")

        df['f_order'] = list_organisms.str.extract("o__(.*?);", expand=False).str.strip()
        df['f_order'] = df['f_order'].str.replace("(","")

        df['f_family'] = list_organisms.str.extract("f__(.*?);", expand=False).str.strip()
        df['f_family'] = df['f_family'].str.replace("(","")

        df['f_class'] = list_organisms.str.extract("c__(.*?);", expand=False).str.strip()
        df['f_class'] = df['f_class'].str.replace("(","")

        df['f_genus'] = list_organisms.str.extract("g__(.*?);", expand=False).str.strip()
        df['f_genus'] = df['f_genus'].str.replace("(","")

        df['f_species'] = list_organisms.str.extract("s__(.*?);", expand=False).str.strip()
        df['f_species'] = df['f_species'].str.replace("(","")

        #capitalizes the names
        df['f_kingdom'] = df['f_kingdom'].astype(str)
        df['f_kingdom'] = df['f_kingdom'].str.capitalize()

        df['f_phylum'] = df['f_phylum'].astype(str)
        df['f_phylum'] = df['f_phylum'].str.capitalize()

        df['f_class'] = df['f_class'].astype(str)
        df['f_class'] = df['f_class'].str.capitalize()

        df['f_order'] = df['f_order'].astype(str)
        df['f_order'] = df['f_order'].str.capitalize()

        df['f_family'] = df['f_family'].astype(str)
        df['f_family'] = df['f_family'].str.capitalize()

        df['f_genus'] = df['f_genus'].astype(str)
        df['f_genus'] = df['f_genus'].str.capitalize()

        df['f_species'] = df['f_species'].astype(str)
        df['f_species'] = df['f_species'].str.capitalize()


        df['f_lineage'] = df[['f_kingdom','f_phylum', 'f_class', 'f_order', 'f_family', 'f_genus', 'f_species']].apply(lambda x: '|'.join(x), axis=1)

        #delete the last columns and paste the f_lineage column to replace the names

    df.to_csv(output_file)

sp_formatter(input_file, output_file)

#PART 2: use species name to find tax ID's and then lineages

#PART 3: later task, use lineages and make a "tree" of lineages
#PART 3.1: convert to .txt file





