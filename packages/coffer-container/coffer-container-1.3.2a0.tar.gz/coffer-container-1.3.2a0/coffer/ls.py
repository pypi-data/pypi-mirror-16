import os
from coffer.utils import getRootDir, text

def ls():
    print (text.availableEnvironments)
    check = os.listdir(getRootDir.getEnvsDir())
    if len(check) == 0:
        print (text.noEnvs)
    else:
        print ('\n'.join(check) + "\n")
