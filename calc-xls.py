#!/usr/bin/python3

#
# Calculate the averages 
#

import csv
import sys
import argparse
import xlsxwriter

parser = argparse.ArgumentParser()
parser.add_argument("threat", help = "virus ;  ips ;  botnet ; app", type=str)
args = parser.parse_args()

def extract_sig_name(input_str):
    for char in input_str:
        if char in " ['":
            input_str = input_str.replace(char,'')
    
    return input_str

def extract_nbr(input_str):
    if input_str is None or input_str == '':
        return 0

    out_number = ''
    for ele in input_str:
        if ele.isdigit():
            out_number += ele

    return float(out_number) 

if args.threat == "av" or args.threat == "virus":
    workbook = xlsxwriter.Workbook('av_growth_compared.xls')
    worksheet24 = workbook.add_worksheet('Last 24hs')
    worksheet7 = workbook.add_worksheet('Last 7days')
    worksheet30 = workbook.add_worksheet('Last 30days')
    file1 = open('av_last_24_hours', 'r')    
    file7 = open('av_last_7_days', 'r')
    file30 = open('av_last_30_days', 'r')

if args.threat == "ips":
    workbook = xlsxwriter.Workbook('ips_growth_compared.xls')
    worksheet24 = workbook.add_worksheet('Last 24hs')
    worksheet7 = workbook.add_worksheet('Last 7days')
    worksheet30 = workbook.add_worksheet('Last 30days')
    file1 = open('ips_last_24_hours', 'r')    
    file7 = open('ips_last_7_days', 'r')
    file30 = open('ips_last_30_days', 'r')

if args.threat == "botnet":
    workbook = xlsxwriter.Workbook('botnet_growth_compared.xls')
    worksheet24 = workbook.add_worksheet('Last 24hs')
    worksheet7 = workbook.add_worksheet('Last 7days')
    worksheet30 = workbook.add_worksheet('Last 30days')
    file1 = open('botnet_last_24_hours', 'r')    
    file7 = open('botnet_last_7_days', 'r')
    file30 = open('botnet_last_30_days', 'r')


hash1 = {}
hash7 = {}
hash30 = {}

worksheet24.set_column('A:A', 40)
worksheet24.write_string('A1', '----- Last 24 Hours -----')
worksheet24.write_string('A2', 'Name')
worksheet24.write_string('B2', 'Total')
worksheet24.write_string('C2', 'AVG / Day')
reader = csv.reader(file1, delimiter=',', quotechar="|")
n = 3 
for row in reader:
    row_name = 'A' + str(n)
    row_cnt = 'B' + str(n)
    row_avg = 'C' + str(n)
    string = str(row)
    hash1['name'], hash1['cnt'] = string.split(",")
    hash1['name'] = extract_sig_name(hash1['name'])
    cnt = extract_nbr(hash1['cnt']) 
    hash1['cnt'] = float(cnt) 
    hash1['avg'] = float(cnt)
    worksheet24.write_string(row_name, hash1['name'])    
    worksheet24.write_string(row_cnt, str(hash1['cnt']))    
    worksheet24.write_string(row_avg, str(hash1['avg']))    
    cnt = 0 
    n = n + 1

worksheet7.set_column('A:A', 40)
worksheet7.write_string('A1', '----- Last 7 days -----')
reader = csv.reader(file7, delimiter=',', quotechar="|")
worksheet7.write_string('A2', 'Name')
worksheet7.write_string('B2', 'Total')
worksheet7.write_string('C2', 'AVG / Day')
n = 3 
for row in reader:
    row_name = 'A' + str(n)
    row_cnt = 'B' + str(n)
    row_avg = 'C' + str(n)
    string = str(row)
    hash7['name'], hash7['cnt'] = string.split(",")
    hash7['name'] = extract_sig_name(hash7['name'])
    cnt7 = extract_nbr(hash7['cnt']) 
    hash7['cnt'] = float(cnt7) 
    hash7['avg'] = float(cnt7 / 7)
    worksheet7.write_string(row_name, hash7['name'])
    worksheet7.write_string(row_cnt, str(hash7['cnt']))
    worksheet7.write_string(row_avg, str(hash7['avg']))
    cnt7 = 0 
    n = n + 1

worksheet30.set_column('A:A', 40)
worksheet30.write_string('A1', '----- Last 30 days -----')
worksheet30.write_string('A2', 'Name')
worksheet30.write_string('B2', 'Total')
worksheet30.write_string('C2', 'AVG / Day')
reader = csv.reader(file30, delimiter=',', quotechar="|")
n = 3 
for row in reader: 
    row_name = 'A' + str(n)
    row_cnt = 'B' + str(n)
    row_avg = 'C' + str(n)
    string = str(row)
    hash30['name'], hash30['cnt'] = string.split(",")
    hash30['name'] = extract_sig_name(hash30['name'])
    cnt30 = extract_nbr(hash30['cnt'])
    hash30['cnt'] = hash30['cnt'].lstrip()
    hash30['cnt'] = float(cnt30) 
    hash30['avg'] = float(cnt30 / 30)
    worksheet30.write_string(row_name, hash30['name'])
    worksheet30.write_string(row_cnt, str(hash30['cnt']))
    worksheet30.write_string(row_avg, str(hash30['avg']))
    cnt30 = 0
    n = n + 1

  

file1.close()
file7.close()
file30.close()
workbook.close()
