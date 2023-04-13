import os, filecmp, shutil


class Dircmp:
    
  
    def dc(self, d):
        
        allFiles = []
        allDirs = []
        for root, subdirs, files in os.walk(d):
            for file in files:
                allFiles.append(os.path.join(root, file).split(d)[1])

            for subdir in subdirs:
                allDirs.append(os.path.join(root, subdir).split(d)[1])
                
        
        return allFiles, allDirs
    
    def onlys(self, list1, list2):
        
        only_in_list1 = []
        for item in list1:
            if item not in list2:
                only_in_list1.append(item)

        return only_in_list1
    
    

    def commons(self, list1, list2):
       

        comm_items = []
        for item in list1[:]:
            if item in list2[:]:
                comm_items.append(item)

        return comm_items
    
    

    def common_but(self):
        

        files = []
        join = os.path.join
        for file in self.comm_files[:]:
            if not filecmp.cmp(join(self.d1, file), join(self.d2, file), shallow = False):
                files.append( ( join ( self.d1, file ), join ( self.d2, file ) ) )
        self.funnies = files[:]
        return files
    
    