
import os 

JPREFIX  = 'DATA'
JSUFFIX  = '.json'      

########################################################
########################################################

# Makes Output Lines for Saving a JSON File:
def MakeJLines(Obj,Spaces=4):
    S = str(Obj).replace("'",'"')
    Rows = []
    I = [0] # Indentation List
    Struct  = []
    row     = ''
    for ch in S:
        if not str(row+ch).strip(): continue
        if   ch=='[':
            I.append(len(row)+1)
            Struct.append('L')
        elif ch=='{':
            I.append(len(row)+1)
            Struct.append('D')
        elif ch==']':
            x = I.pop()
            x = Struct.pop()
        elif ch=='}':
            x = I.pop()
            x = Struct.pop()  
        elif ch==',':
            row = row+ch
            Rows.append(row)
            row = ' '*I[-1]
            continue
        row += ch
    Rows.append(row)
    return Rows      
        
# 'Read()' takes all the lines of a text file,
# converts them to strings, and returns a list of these strings.
# File must be named explicitly: '/Users/jarolfsen/Desktop/WLT.txt'
def Read(FILE):
    rawfilelist = open(FILE,'rt').readlines()
    filelist = [i[:-1].strip() for i in rawfilelist]
    return filelist

# 'WriteOver()' overwrites a whole file with a list.
def Write(FILE,LIST):
    path = GetPath(FILE)
    if path: EnsurePath(path) 
    List = [str(i)+'\n' for i in LIST]
    open(FILE,'wt').writelines(List) 
    
def read_json(fn):
    Lines = Read(fn)
    String = ''.join(Lines)
    return eval(String) 

def write_json(fn,data):
    Write(fn,MakeJLines(data)) 


########################################################
########################################################

def GetPath(String):  
    if '/' not in String: 
        if '.' in String: return ''
        else: return String 
    L = String.split('/')
    if '.' not in L[-1]: 
        if '/' != String[-1]: return String+'/'
        else: return String
    String2 = '/'.join(L[:-1]) + '/'
    return String2 

# Create a path if it doesn't exist:
def EnsurePath(path):
    if not os.path.exists(path):
        os.makedirs(path)
    

########################################################
########################################################

def PullFromAPI(ThingID):
    return {}  

def PullFromDir(thing_id,dirname='',suffix=''):
    if not suffix: suffix = JSUFFIX
    if not dirname: dirname = JPREFIX
    if dirname and dirname[-1] != '/': dirname+='/'
    fn = dirname+thing+suffix 
    return read_json(fn) 

def ConditionalPull(thing_id,dirname=''):  
    try:    J = PullFromDir(thing,suffix,dirname)
    except: J = PullFromAPI(thing)
    return  J  

def ThingIsThere(Thing,There):
    path = GetPath(There)+Thing  
    return os.path.exists(path)  

def PullOverwrite():
    pass

def PullAdd():
    pass
        
########################################################
########################################################



