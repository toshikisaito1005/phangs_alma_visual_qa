import os
import sys
import glob
import shutil


###extract diagnostic plots from delivered calibrated visibility data for PHANGS galaxies
#2018-02-07: developed by tsaito
#2018-02-08: add ImageMajick commands (png2pdf)
#
#
###How to run
#Simply locate this script under */2017.1.00886.L/ directory where all science_* direcitories
#are located. This script will create visual_qa/ directory under */2017.1.00886.L/ which con-
#tains all png files. The name of the created sub-directories is same as the *.ms name. When
#you want to re-run this script for a certain ms (e.g., uid___A002_Xc55c89_X426c.ms), you 
#need to remove a sub-directory, visual_qa/uid___A002_Xc55c89_X426c/, in advance. Re-run for
# all ms, just remove visual_qa/ directory.


dir_ms = glob.glob("../science_*/group.*/member.*/calibrated/uid*.ms")
dir_current = os.getcwd()

done = glob.glob("../visual_qa/")
if not done:
    os.mkdir("../visual_qa/")

#plotms
for i in range(len(dir_ms)):
    dir_save = "../visual_qa/" + dir_ms[i].split("/")[4].replace(".ms", "") +"/"
    done = glob.glob(dir_save)
    if done:
        print("skip:   " + dir_ms[i].split("/")[4])
    if not done:
        print("PLOTMS: " + dir_ms[i].split("/")[4])
        msmd.open(dir_ms[i])
        field_intent = ["bpcal", "phcal"]
        field_name = [msmd.fieldsforintent("*BANDPASS*", True)[0], msmd.fieldsforintent("*PHASE*", True)[0]]
        field_id = [msmd.fieldsforintent("*BANDPASS*", False)[0], msmd.fieldsforintent("*PHASE*", False)[0]]
        msmd.done()
        os.mkdir(dir_save)
        for j in range(len(field_intent)):
            for yaxis in ["amp__", "phase"]:
                for xaxis in ["ant1__", "ant2__", "uvdist"]:
                    avgchannel = "1e8"
                    avgtime = "1e8"
                    avgscan = True
                    plotfile = dir_save + dir_ms[i].split("/")[4].replace(".ms", "") + "_" + yaxis + "_" + xaxis + "_" + field_intent[j] + "_avgtc.png"
                    plotms(vis = dir_ms[i], gridrows = 2, gridcols = 2, xaxis = xaxis.replace("__", ""), yaxis = yaxis.replace("__", ""), ydatacolumn = "corrected", field = field_name[j], spw = "16,18,20,22", averagedata = True, avgchannel = avgchannel, avgtime = avgtime, avgscan = avgscan, iteraxis = "spw", coloraxis = "corr", plotfile = plotfile, expformat = "png", overwrite = False, showgui = False, title = plotfile)
                    os.rename(plotfile.replace(".png", "_Spw16,18,20,22.png"), plotfile)
                for xaxis in ["ant1__", "ant2__", "uvdist", "time__"]:
                    avgchannel = "1e8"
                    avgtime = "1"
                    avgscan = False
                    plotfile = dir_save + dir_ms[i].split("/")[4].replace(".ms", "") + "_" + yaxis + "_" + xaxis + "_" + field_intent[j] + "_avg_c.png"
                    plotms(vis = dir_ms[i], gridrows = 2, gridcols = 2, xaxis = xaxis.replace("__", ""), yaxis = yaxis.replace("__", ""), ydatacolumn = "corrected", field = field_name[j], spw = "16,18,20,22", averagedata = True, avgchannel = avgchannel, avgtime = avgtime, avgscan = avgscan, iteraxis = "spw", coloraxis = "corr", plotfile = plotfile, expformat = "png", overwrite = False, showgui = False, title = plotfile)
                    os.rename(plotfile.replace(".png", "_Spw16,18,20,22.png"), plotfile)
                for xaxis in ["ant1__", "ant2__", "uvdist", "freq__"]:
                    avgchannel = "1"
                    avgtime = "1e8"
                    avgscan = True
                    plotfile = dir_save + dir_ms[i].split("/")[4].replace(".ms", "") + "_" + yaxis + "_" + xaxis + "_" + field_intent[j] + "_avgt_.png"
                    plotms(vis = dir_ms[i], gridrows = 2, gridcols = 2, xaxis = xaxis.replace("__", ""), yaxis = yaxis.replace("__", ""), ydatacolumn = "corrected", field = field_name[j], spw = "16,18,20,22", averagedata = True, avgchannel = avgchannel, avgtime = avgtime, avgscan = avgscan, iteraxis = "spw", coloraxis = "corr", plotfile = plotfile, expformat = "png", overwrite = False, showgui = False, title = plotfile)
                    os.rename(plotfile.replace(".png", "_Spw16,18,20,22.png"), plotfile)

#png2pdf
#for i in range(len(dir_ms)):
for i in [0,1]:
    msmd.open(dir_ms[i])
    field_intent = ["bpcal", "phcal"]
    field_name = [msmd.fieldsforintent("*BANDPASS*", True)[0], msmd.fieldsforintent("*PHASE*", True)[0]]
    field_id = [msmd.fieldsforintent("*BANDPASS*", False)[0], msmd.fieldsforintent("*PHASE*", False)[0]]
    msmd.done()
    dir_save = "../visual_qa/" + dir_ms[i].split("/")[4].replace(".ms", "") +"/"
    print("png2pdf: " + dir_ms[i].split("/")[4])
    dir_weblog = glob.glob(dir_ms[i].split("calibrated/")[0] + "qa/pipeline-*/")
    if not dir_weblog:
        tar_name = glob.glob(dir_ms[i].split("calibrated/")[0] + "qa/*.tgz")
        os.system("tar -zxvf " + tar_name[0] + " -C " + dir_ms[i].split("calibrated/")[0] + "qa/")
        dir_weblog = glob.glob(dir_ms[i].split("calibrated/")[0] + "qa/pipeline-*/")
    tsys_file = glob.glob(dir_weblog[0] + "html/stage7/tsys-" + dir_ms[i].split("/")[4] + "-summary.spw*.png")
    other_file = glob.glob(dir_weblog[0] + "html/sessionsession_*/" + dir_ms[i].split("/")[4] + "/*.png")
    for j in range(len(field_intent)):
        #png files from weblog
        os.system("m ntage " + other_file[0] + " " + other_file[1] + " " + other_file[2] + " " + other_file[3] + " " + other_file[4] + " " + other_file[5] + " " + other_file[6] + " " + other_file[7] + " "  + " " + tsys_file[0] + " " + tsys_file[1] + " " + tsys_file[2] + " " + tsys_file[3] + " " + other_file[8] + " -tile 2x2 -geometry 800x600 " + dir_save + dir_ms[i].split("/")[4].replace(".ms", "") + "_status.pdf")
        #plotms png files
        for m in ["bpcal", "phcal"]:
            for n in ["amp", "phase"]:
                #ant1
                im = sorted(glob.glob(dir_save + dir_ms[i].split("/")[4].replace(".ms", "") + "_" + n + "*ant1*" + m + "*.png"))
                os.system("convert -pointsize 20 label:'" + n + " vs. ant1@" + m + "\n1.avgc, 2.avgt, 3.avgct' " + dir_save + "name.png")
                im.append(dir_save + "name.png")
                os.system("montage " + im[0] + " " + im[1] + " " + im[2] + " " + im[3] + " -tile 2x2 -geometry 800x600+10+10 " + dir_save + "p001.pdf")
                #ant2
                im = sorted(glob.glob(dir_save + dir_ms[i].split("/")[4].replace(".ms", "") + "_" + n + "*ant2*" + m + "*.png"))
                os.system("convert -pointsize 20 label:'" + n + " vs. ant2@" + m + "\n1.avgc, 2.avgt, 3.avgct' " + dir_save + "name.png")
                im.append(dir_save + "name.png")
                os.system("montage " + im[0] + " " + im[1] + " " + im[2] + " " + im[3] + " -tile 2x2 -geometry 800x600+10+10 " + dir_save + "p002.pdf")
                #uvdist
                im = sorted(glob.glob(dir_save + dir_ms[i].split("/")[4].replace(".ms", "") + "_" + n + "*uvdist*" + m + "*.png"))
                os.system("convert -pointsize 20 label:'" + n + " vs. uvdist@" + m + "\n1.avgc, 2.avgt, 3.avgct' " + dir_save + "name.png")
                im.append(dir_save + "name.png")
                os.system("montage " + im[0] + " " + im[1] + " " + im[2] + " " + im[3] + " -tile 2x2 -geometry 800x600+10+10 " + dir_save + "p003.pdf")
                #freq/time
                im = sorted(glob.glob(dir_save + dir_ms[i].split("/")[4].replace(".ms", "") + "_" + n + "*freq*" + m + "*.png"))
                im2 = sorted(glob.glob(dir_save + dir_ms[i].split("/")[4].replace(".ms", "") + "_" + n + "*time*" + m + "*.png"))
                im.extend(im2)
                os.system("montage " + im[0] + " " + im[1] + " -tile 2x1 -geometry 800x600+10+10 " + dir_save + "p004.pdf")
                #merge
                im=sorted(glob.glob(dir_save + "p00*.pdf"))
                os.system("convert " + im[0] + " " + im[1] + " " + im[2] + " " + im[3] + " " + dir_save + dir_ms[i].split("/")[4].replace(".ms", "") + "_" + m + "_" + n + ".pdf")
                os.system("rm -rf " + dir_save + "p00*.pdf")
            pdf = glob.glob(dir_save + "*.pdf")
            shutil.copy(pdf[0], "../visual_qa/")
            shutil.copy(pdf[1], "../visual_qa/")
            shutil.copy(pdf[2], "../visual_qa/")

