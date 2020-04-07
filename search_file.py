import pandas as pd
import re
import os

def excel_file_extract():
    excel_pat = re.compile(r'(^Alstom.+\.xl.+)')
    for file in os.listdir('./'):
        if excel_pat.match(file):
            excel_result = excel_pat.match(file).group()
    return os.path.join(os.path.abspath('./'),excel_result)


df = pd.read_excel(excel_file_extract(),sheet_name='Master Database')

def site_extract(location):
	output = df[df['SITE ID'].str.contains(location) |df['SITE ID'].str.startswith(location) ]
	return output['SITE ID'].values.tolist()

def ip_extract(location):
    df_local = df.set_index("SITE ID")
    site_ip = []
    sites = site_extract(location)
    for site in sites:
        site_ip.append((site,df_local.loc[site,'CEMGMTLo']))
    print("=="*80)
    for data, ip in site_ip:
        print(data, ip)
    print()

if __name__ == '__main__':
	
	while True:
		loc = input("Enter Site ID or press Enter to Exit: ").upper()
		if loc != "":
			ip_extract(loc)
		else:
			break

