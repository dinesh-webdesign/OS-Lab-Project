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
    
    