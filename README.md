# README for PHANGS Visual Quality Assurance  
## Get started
run this command under 2017.1.00886.L/ directory.
```
git clone https://github.com/toshikisaito1005/phangs_visual_qa_scripts.git
```


## Directory Tree　　
```  
2017.1.00886.L                                          ! parent directory
    ├  science_goal.uid___A001_X1284_X2633  
    ├  science_goal.uid___A001_X1284_X263d  
    ├  science_goal.uid___A001_X1284_*  
    ├  phangs_visual_qa_scripts                         ! contains all scripts
    |    ├  README.md                                   ! this file
    |    ├  run_scriptForPI.py  
    |    └  visual_qaplots.py  
    ├  visual_qa                                        ! automatically created by visual_qaplots.py  
    |    ├  uid___A002_Xc53e4e_X2579  
    |    |    └  uid___A002_Xc53e4e_X2579_*.png         !  products by plotms task
    |    ├  uid___A002_Xc53e4e_X2579_bpcal_amp.pdf  
    |    ├  uid___A002_Xc53e4e_X2579_bpcal_phase.pdf  
    |    ├  uid___A002_Xc53e4e_X2579_phcal_amp.pdf  
    |    ├  uid___A002_Xc53e4e_X2579_phcal_phase.pdf  
    |    ├  uid___A002_Xc53e4e_X2579_status.pdf    
    |    └  uid___A002_X*  
    └  imaging                                          ! contains all images by imaging pipelines
```  


## execfile("run_scriptForPI.py")  
Run all scriptForPI.py under all science_goal*/member*/group*/script/ directories, if calibrated/ directory is not present under group*/ directory.  


## execfile("visual_qaplots.py")
Create visual_qa/ directory, which contains some useful diagnostic plots (png files and merged pdf files) by plotms and weblog.  It takes ~10 minutes per \*.ms.

