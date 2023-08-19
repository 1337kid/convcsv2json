import json,csv,sys,os

class csv2json:
    dict_data={}
    
    def __init__(self,in_file,intend=None,numbered=False):
        assert type(intend) in [type(None),int], 'Value of intend should be either None or an integer'
        self.in_file = in_file
        self.intend = intend
        self.numbered = numbered

    def __convtodict(self):
        if os.path.exists(self.in_file)==0:
            raise Exception(f'File "{self.in_file}" is not present in the current directory')
        with open(self.in_file) as f:
            data=list(csv.DictReader(f))
        if self.numbered==True:
            for i in range(len(data)):
                self.dict_data[i+1]=data[i]
        else:
            self.dict_data=data
        return self.dict_data
        
    def conv(self):
        data = csv2json.__convtodict(self)
        if self.intend!=None: return json.dumps(data,indent=self.intend)
        else: return json.dumps(data)
    
    def export(self,out_file):
        data = csv2json.__convtodict(self)
        with open(out_file,'w') as f:
            if self.intend!=None: json.dump(data,f,indent=self.intend)
            else: json.dump(data,f)