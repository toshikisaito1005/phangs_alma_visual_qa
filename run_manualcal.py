import os
import sys
import glob
import shutil

### identify flagtemplates
flagtemplates = glob.glob("./file_flagtemplate/science_goal.*/member.*/*.txt")

filename_flag = []
for i in range(len(flagtemplates)):
    filename_flag.append(flagtemplates[i].split("/")[4])
    location_flag = "../" + flagtemplates[i].split("/")[2] + "/*/" \
                    + flagtemplates[i].split("/")[3] + "/raw/"
    shutil.copy(flagtemplates[i], location_flag)

print(TBE.)

