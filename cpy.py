def crange(start = 1, end = 'null', step = 1):
    """A better range function, returns list"""
    name = crange.__name__                         ###
    testing = False                         ###
    if testing: error = FileNotFoundError
    else: error = Exception
    try:
        
        if end == 'null':
            end = start
            start = 0
        returnlist = []
        while start < end: 
            returnlist.append(start)
            start += step
        return returnlist
    
        if testing: print()
    
    
    except error as err:
        print(name, err, err.args)
        
def czip(list1, list2):
    """A better zip function, iterate through two lists at once!"""

    name = czip.__name__                         ###
    testing = False                         ###
    if testing: error = FileNotFoundError
    else: error = Exception
    try:
        
        if len(list1) == len(list2):
            newlist = []
            for x in range(len(list1)):
                newlist.append([list1[x], list2[x]])
            return newlist
        else: 
            print("Lengths incorrect")
    
    except error as err:
        print(name, err, err.args)
        
        
class crandom:
    """This is a random number generator I developed to mimic the random package. It uses more than just time for entropy"""
    def __init__(self, cnum1 = 12):
        self._author = "This class was authored by C"

        
        
    @classmethod
    def crandomfloat(cls, x = None):
        '''generates one random number between 0 and 1 of 8 digits. x is an optional random digit between 0-9'''                        ###
        testing = 0 
        import psutil 
        from datetime import datetime as dt
        import time
        import statistics

        #sets variables
        now = dt.now()
        n1 = int(str(now.microsecond)[-1])
        n2 = int(str(psutil.cpu_stats().ctx_switches)[-1])
        n3 = int(str(psutil.cpu_stats().interrupts)[-1])
        n4 = int(str(psutil.cpu_stats().syscalls)[-1])
        n5 = int(str(time.time())[-1])

        #mathmatically achievied variables
        n6 = int(str(n3 + n5)[-1])
        n7 = int(str(n1 + n4)[-1])
        n8 = int(str(n1 + n4 + n3 + n5 + n2)[-1])

        #adds extra complexity
        if n1%2 == 0: n6 = int(str(n6 + n8)[-1]) 
        if n8%2 == 0: n2 = int(str(n7-n2)[-1]) 
        if x:
            if n3 > 4: n4 = int(str(n4-n3)[-1])
            else: n3 = int(str(n3-n4)[-1])

        #generates random float
        num1 = float("." + str(n6) + str(n2) + str(n3) + str(n4) + str(n7) + str(n1) + str(n8) + str(n5))

        if testing: print(num1)
        return num1

    @classmethod
    def randomint(cls, x = None):
        '''Use 'randint' generally. This generates one random number between 0 and 9. x is an optional random digit between 0-9'''                        ###
        testing = 0 
        import psutil 
        from datetime import datetime as dt
        import time
        
        #makes a list of somewhat random variables from several sources
        numlist = []
        for x in range(2):
            now = dt.now()
            n1 = int(str(now.microsecond)[-1])
            n2 = int(str(psutil.cpu_stats().ctx_switches)[-1])
            n3 = int(str(psutil.cpu_stats().interrupts)[-1])
            n4 = int(str(psutil.cpu_stats().syscalls)[-1])
            n5 = int(str(time.time())[-1])

            numlist.extend([n1, n2, n3, n4, n5])
        
        #mathematically added variables
        n6 = int(str(n3 + n5)[-1])
        n7 = int(str(n1 + n4)[-1])

        #chooses an item from the above list based on a somewhat random number
        if x:
            rnum = numlist[x]
        else:
            if n4%3 == 2:
                if n2 > 4:
                    rnum = numlist[n6]
                else: 
                    rnum = numlist[n7]
            else:
                if n3 < 5:
                    rnum = numlist[n1]
                else: 
                    rnum = numlist[n4]

        if testing: print(rnum)
        return rnum

    @classmethod
    def randint(cls, mini = 0, maxi = None):
        '''generates one random number between mini and maxi.'''                        ###
        testing = 0 

        import psutil 
        from datetime import datetime as dt
        import time

        #allows one to input just the maximum number and leave the minimum number blank
        if mini != 0 and maxi == None: 
            maxi = mini
            mini = 0
        elif maxi == None: 
            maxi = 10
        
        #sets starting variables
        length = len(str(maxi - 1))
        st_top = maxi + 1
        st_bot = -1

        #finds random number within mini and maxi
        while st_top >= maxi and st_bot < mini:
            st_top = ''
            for x in range(length):
                st_top += str(crandom.randomint())
            st_top = int(st_top)
            st_bot = st_bot

        if testing: print(st_top)
        return st_top
    
    @classmethod
    def randomgeneratortester(cls, functioninstring):
        """used to test a functin that provides random numbers""" 
        import statistics
        MyList = []
        
        #gets 1000 random numbers from function
        for x in range(1000):
            exec(f"MyList.append({functioninstring}())")

        #gets some statistics on such numbers
        for item in [MyList]:
            print("---------------")
            print(f"stdev: {statistics.pstdev(item)} | mean:{statistics.mean(item)} | count of highest: {item.count(statistics.mode(item))}")

            my_dict = {i:item.count(i) for i in item}
            for x in range(max(MyList)+1):
                try:
                    print(x, ":", my_dict[x], end = " |    ")
                except: pass
            print("-------------")
    
    @classmethod
    def choice(cls, lista):
        """Used to make a random choice from a list"""
        #chooses an index value at random
        index = crandom.randint(len(lista))
        return lista[index]
    
    @classmethod
    def shuffle(cls, lista):
        """Used to shuffle a list randomly"""
        maxi = len(lista)
        #changes one random index with another random index value
        for x in range(len(lista)):
            tempindex1 = crandom.randint(len(lista))
            tempindex2 = crandom.randint(len(lista))
            tempvalue = lista[tempindex1]
            lista[tempindex1] = lista[tempindex2]
            lista[tempindex2] = tempvalue
            
        return lista
        
def findfile(file, path):
    """Used to find a file path"""
    name = findfile.__name__
    try:
        import os
        for root, dirs, files in os.walk(path):
            if file in files: 
                p = os.path.join(root, file)
                #print(p)
                return p 
        print("Error, file not found. Trying real path")
        from os import path
        if path.exists(file):
            return path.realpath(file)
        else: 
            print("No such file", file)
    except Exception as err:
        print(name, err)        

#a smart document opener
def copen(file, var = "r+", content = 0):
    """Used to find and open a file, but also does xml, jpg """
    name = copen2.__name__
    import os
    try:
        #finds file path
        path = findfile(file, os.getcwd())
        #print(path)
        if not path:
            path = findfile(file, "C:/")
        
        #checks filetype
        filetype = file.split(".")[1]
        if filetype == "txt" or filetype == "py":
            pass
        elif filetype == "jpg":
            if var != "rb" and var != "wb":
                if var == 'w':
                    var = "wb"
                else:
                    var = "rb"
        elif filetype == "xml":
            import xml.dom.minidom
            f = xml.dom.minidom.parse(file)
            print("Node Name is:", f.nodeName)
            print("First subnode is:", f.firstChild.tagName)
            return f
        elif filetype == "zip":
            print("zip")
            import zipfile
            f=zipfile.ZipFile(path, 'r')
            names = f.namelist()
            counter = 0
            for name in names:
                counter += 1
                print(str(counter), name)
            contin = input("Do you want to open a file? 1 = yes")
            if contin == "1":
                filenumber = int(input("Which file number?"))
                counter = 0
                for name in names:
                    counter += 1
                    if counter == filenumber:
                        zf =  f.open(name)
                return zf 
            
        if content:
            filecontent = []
            f = open(path, var)
            if filetype == "txt" or filetype == "py":
                buffersize = 50000
                buffer = f.read(buffersize)
                while len(buffer): #NEWWWWWWWWWWWWWWWW
                    filecontent.append(buffer)
                    buffer = f.read(buffersize)
                    return filecontent
        return open(path, var) 
    
    except Exception as err:
        print(name, err) #TIS reclassified as SC1 not SC2, posting SC1 next wed or thurs
        

