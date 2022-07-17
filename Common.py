from msilib.schema import Class


import os.path
class Common:
   
    def SalvarArquivo(Nome,Path,Texto):
        fullPath = Path + "/" + Nome
        if not os.path.exists(fullPath):
            with open(Nome, 'w') as f: 
                f.write(Texto)
            