import xmltodict as xd
data=[]    

filename='KE15_g20p800-000.xml'

with open(filename,'r') as f:
    dict_data= xd.parse(f)
    
for i in dict_data['PVScan'][u'Sequence']:

    for j in i['Frame']:
        d=[]
        #print j['File']['@filename'], 
        d.append(j['File']['@filename'])
        if j['PVStateShard'] is not None:
            for k in j['PVStateShard']['PVStateValue']['SubindexedValues']:
                #print k['SubindexedValue']['@value'],','
                d.append(k['SubindexedValue']['@value'])
        else:
            for j1 in i['PVStateShard']['PVStateValue']:
                if 'SubindexedValues' in j1.keys():
                    for k in j1['SubindexedValues']:
                        #print k['SubindexedValue']['@value'],',',
                        d.append(k['SubindexedValue']['@value'])
            
        #print 
        data.append(d)
		
data_str=[]
for line in data:
    d='\n'
    for col in line:
        d=d+str(col)+'\t'        
    data_str.append(d)
                
with open('tile2.txt','w') as fid:
    for line in data_str:
        fid.write(line)
        
