### Experiment Result
This chapter detailed about forensic analysis results of Google Chrome's Incognito browing artifacts from 3 different data sources for 4 scnearios. Experiment result are explained as detailed analysis for each data sources for 4 scnearios. Therefore, there are 3 sections for each data sources repsectively.Common ananlysis and observation points are presented for each datasoutces, followed by discussion about significant anlysis and observation points for each scneario. At the end of the chapter, a result summary matrix of scneario with disk image is provided at the end of this chapter to recap the summary result. 

#### Acqusition Result 

Table xx is list of evidence images captured with FTKImager and memory dump with QEMU emulator for 4 scnearios. As for disk images, FTKImager validate suspect and evidence disk images with cryptographic checksums. For physical memory dumps, cryprographic checksums are generated after the acqusition. The correctness of file size, missing pages and the case of first 256 MB zero out are cheked for all memory dumps. Volatility Imageinfo shows correct system information and 

#### Persistent Storage Analysis 

Location of Data artifacts
From preliminary experiement, default location of Google Chrome data artifcats for Windows operating system is discovered. Google Chrome relies SQLite database technology to store browsing artifacts and also uses JSON and proprietary formats to store data artifacts. These files are extracted and analyzed to see ttypes of data stored in them. Table xx is a list of Chrome artifcats that stored information about browsing records and user activities.

Keyword searching
List of evidence keywords from known and unknown data are created as a keyword list and scan with autopsy keyword searching function. Autopsy keyword search is powered by Apache SOLR text search and indexing engine to search keywords instead of searching raw data.

Timestamp changes
Changes in the accessed, modified and created timestamp of files are analyzed. 

##### Scneario 1

siginificant findings at this stage

##### Scneario 2

##### Scneario 3

##### Scneario 4

Memory Contents on Persistent Storage Analysis

At Windows 8 system, it is likely to find hiberfil.sys no matter hibernation mode is turned on or not. The reason behind this behaviour is due to fast boot mode, which is explained in Methodology section xxx. New page file,swapfile.sys is to store volatile data from Windows Metro/Modern apps. For normal desktop mode Windows application, traditional Windows swap file, pagefile.sys is used to store volatile data. Analysis of swapfile.sy

Files Extraction

Files Size

Swapfile

Hibernation file

Scneario 1

Scneario 2

Scneario 3

Scneario 4

Volatile Data Analysis

Known data analysis

Unknown data

File carving

Scneario 1

Scneario 2

Scneario 3

Scneario 4

Result Summary





