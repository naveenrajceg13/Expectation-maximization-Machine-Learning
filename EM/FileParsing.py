from ctypes.wintypes import DOUBLE


def parse_file(files,values):
    data=[]
    count=0
    min=0
    max=0
    with open(files,'r') as my_file:
                try:
                    s=my_file.read()
                except:
                    pass
                data.append(s)
    
    for i in data:
        val=i.split()
        for j in val:
            count=count+1
            if(count==1):
                min=float(j)
                max=float(j)
            else:
                if(min>float(j)):
                    min=float(j)
                if(max<float(j)):
                    max=float(j)
            values.append(float(j))
    return values,min,max
