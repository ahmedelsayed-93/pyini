import collections

class pyini:
    
    __file_content = collections.OrderedDict()

    def __init__(self):
        pass
     
    def read(self, File):
	
        pyini.__file_content.clear()        
        with open(File, 'r+') as f:
            lines = [x.strip() for x in f]
            
        for item in lines:
            try:
                if item[0] == '[' and item[len(item)-1] == ']':
                    currentSection = item[1:-1]
                    pyini.__file_content[currentSection] = collections.OrderedDict()
                else:
                    item = item.split('=')
                    pyini.__file_content[currentSection][item[0]] = item[1]
            except:
                pass
      
    def addSection(self,sectionName, *args):
        if self.isSectionExist(sectionName):
            raise SectionAlreadyExists,(sectionName)
        else: 
            try:
                pyini.__file_content[sectionName] = collections.OrderedDict()
                for i in range(0,len(args), 2):
                      pyini.__file_content[sectionName][args[i]] = args[i+1]
            except IndexError:
                 print "Error : Wrong number of arguments"

    def renameSection(self,old_sectionName,new_sectionName):
        if self.isSectionExist(old_sectionName):
            if self.isSectionExist(new_sectionName):
                raise SectionAlreadyExists,(new_sectionName)
            else:
                pyini.__file_content[new_sectionName] = pyini.__file_content.pop(old_sectionName)
        else:
            raise SectionNotExists, (old_sectionName)
            
    def deleteSection(self,sectionName):
        if self.isSectionExist(sectionName):
            del pyini.__file_content[sectionName]
        else:
            raise SectionNotExists, (sectionName)
        
    def isSectionExist(self, sectionName):
            return pyini.__file_content.has_key(sectionName)
            
    def sectionCount(self):
            return len(pyini.__file_content)


    def addKey(self,sectionName,keyName,value):
        if self.isSectionExist(sectionName):
            if self.isKeyExist(sectionName,keyName):
                raise KeyAlreadyExists, (keyName)
            else:
                pyini.__file_content[sectionName][keyName] = str(value)  
        else:
             raise SectionNotExists, (sectionName)
            
    def renameKey(self,sectionName,old_keyName,new_keyName):
        if self.isSectionExist(sectionName):
            if self.isKeyExist(sectionName,old_keyName):
                if self.isKeyExist(sectionName, new_keyName):
                    raise KeyAlreadyExists, new_keyName
                else:
                     pyini.__file_content[sectionName][new_keyName] = pyini.__file_content[sectionName].pop(old_keyName)
            else:
                raise KeyNotExists, (old_keyName)          
        else:
            raise SectionNotExists, (sectionName)
                       

    def deleteKey(self,sectionName,keyName):
        if self.isSectionExist(sectionName):
            if self.isKeyExist(sectionName,keyName):
                del pyini.__file_content[sectionName][keyName]
            else:
                raise KeyNotExists, (keyName)
        else:
            raise SectionNotExists, (sectionName)      

    def keyCount(self,sectionName):
        if self.isSectionExist(sectionName):
             return len(pyini.__file_content[sectionName])
        else:
            raise SectionNotExists, (sectionName)
    
    def isKeyExist(self, sectionName, keyName):
        if self.isSectionExist(sectionName):
             return pyini.__file_content[sectionName].has_key(keyName)
        else:
            raise SectionNotExists, (sectionName)

    def setValue(self, sectionName, keyName, value):
        if self.isSectionExist(sectionName):
            if self.isKeyExist(sectionName,keyName):
                pyini.__file_content[sectionName][keyName] = value
            else:
                raise KeyNotExists, (keyName)
        else:
            raise SectionNotExists, (sectionName)

    def getValue(self, sectionName, keyName):
        if self.isSectionExist(sectionName):
            if self.isKeyExist(sectionName,keyName):
                return pyini.__file_content[sectionName][keyName]
            else:
                raise KeyNotExists, (keyName)
        else:
            raise SectionNotExists, (sectionName)

    
    def sections(self):
        return pyini.__file_content.keys()

    def keys(self, sectionName):
        if self.isSectionExist(sectionName):
            return pyini.__file_content[sectionName].keys()
        else:
            raise SectionNotExists, (sectionName)
            
    def values(self, sectionName):
        if self.isSectionExist(sectionName):
            return pyini.__file_content[sectionName].values()
        else:
            raise SectionNotExists, (sectionName)

    def viewAll(self):
        content = list(pyini.__file_content.items())
        for section,keys in content:
            print '['+section+']'
            keys = keys.items()
            for key,value in keys:
                print key+"="+str(value)

    def clear(self):
        pyini.__file_content.clear()
        
        
    def save(self, File):        
        with open(File, 'w+') as f:
            content = list(pyini.__file_content.items())
            for section,keys in content:
                f.write('['+section+']\n')
                keys = keys.items()
                for key,value in keys:
                    f.write(key+"="+str(value)+'\n')

#Exceptions 
class SectionAlreadyExists(Exception):
    def __init__(self, sectionName):
        self.var = "Section \"" + sectionName + "\" already exists"
    def __str__(self):
        return repr(self.var)

class SectionNotExists(Exception):
    def __init__(self, sectionName):
        self.var = "Section \"" + sectionName + "\" does not exist"
    def __str__(self):
        return repr(self.var)

class KeyAlreadyExists(Exception):
    def __init__(self, keyName):
        self.var = "Key \"" + keyName + "\" already exists"
    def __str__(self):
        return repr(self.var)

class KeyNotExists(Exception):
    def __init__(self, keyName):
        self.var = "Key \"" + keyName + "\" does not exist"
    def __str__(self):
        return repr(self.var)

