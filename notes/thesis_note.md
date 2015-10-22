### Data Extraction & Expected Deliverables
There are two types of evidence data it is expected to extract from digial images, which are "Known" and "Unknown" data. "Known" data structure is the type of data which forensic analysts know beforehand. In the research experiment, the following data structures are "known" data which are browsing URLs, evidence keywords, username and keywords that used during the experiment. By extracting and presenting these information, it can be proven that user access to a particualr web services with extract activities. However, "known" data can be varied for real world invistigation depends on the stages of suspet's system and also the traces and intel on the suspect. Extracting "known" data is a straightforward process with tools like "strings.exe", grep or advanced searching tool like Yara. For data on harddisk, forensic viewer provides searching allocated and unallocated disk space within the application. For untruncated files, it can be extracted and analyzed with third-party application like SQLite Database Browser for SQLITE database. 

https://books.google.co.th/books?id=1X33BQAAQBAJ&pg=PA68&lpg=PA68&dq=%22unknown+data%22+digital+forensic&source=bl&ots=GU2E_yckWg&sig=21vkHx9imHr-m_ldd5FMKTms_bM&hl=en&sa=X&ved=0CCoQ6AEwAmoVChMIqdqcnO76xwIVg1eOCh1scg_J#v=onepage&q&f=false 
"Unknown" data is the rest of the data that can extract though out the forensic analysis process. Basic method of analysing "unknown" data is using hex editor to scan thorough memory contents. Another common and practical approach is scanning and searching using signatures. Tools like foremost, scalpel and yara carve for files and extracts data fragments by matching file header and footers. For Yara pattern matching tool, it extracts data segments by feeding conditions, regular expressions as rules. Forensic analysts and researchers need to study metadata of files and constructs signatures or "needles" and look for the "unknown" data from digital images. Another way to gather information is by viewing code base of a open-source program to identify important and useful data structures such as variables, class and method names which can contains application level information about running process and program. Other approaches to extract "unknown information" is by using statistical model and an artifical intellengence deep machine learning algorithm.

### Data Analysis

#### Presistent Storage Analysis

From captured disk image, evidence images files are preserved as E01 raw format and for each evidence images, a new case file is created at Autopsy forensic viewer.For normal browsing mode, browsing activities are located at default data location of Google Chrome. Browsing URLs, Downloaded URLs, Caches and website resources can be extracted at default location. The default location of Chrome browsing artifacts are located and forensic analysis process are proceeded afterwards. 

Chrome relys on SQLite3 file-based database technology to store browsing artifacts as primary source. As for fallback mode in case the browser or the system crashes, it uses SQLite fallback journal mode to recover data. Most of the existing tools to recover Chrome browsing artifacts decode and presents data from SQLite browsers. These database files are examined and invistigated to see whether data are populated from Chrome's incognito mode or not. Moreover, other folders and file formats are analyzed to see type of data stored and traces of private browsing data in it. 

**Need to make sure**
For forensic analysis, Autopsy provides 2 basic searching functionalities to search evidence words from the disk image, which are strings and grep. strings can search though allocated,unallocated and slackspce, which means it can identify data allocated in different clusters. The drawbacks of strings is that it can lead to false positives. For grep search, it looks for 

User inputs and browsing URLs are seraching through the disk images to identiy files and location of user input to analyze how user inputs are dispersed in the disk image.  Windows swapfiles content are also extracted and analyzed to see browsing traces are in located in memory contents in hard disk or not. In a scneario of power down system, swap files, hibernation files and crashdump files are the only soureces to analyze memory contents.

#### Volatile memeory analysis

From physical memory image, it is possible to analyze and invistigate system and application running process, process handles, memory allocation of process and so on. Volatility framework is a solid platform to analyze memory images but however, it needs a background knowledge of memory contents and data structures of process. At literature review, it is mentioned about overview of Windows proces strucutre and methods to enumerate lists of process. Volaility framework handles structure differences due to implementation variation among different operating systems. The process of the analysis of application-level data, “next generation analysis”  of physical memory is focused on application address space. Size of application address space, user mode space of 32 bit process is 2GB for x86 architecture for windows operating system and it can be 3GB if the windows 3GB swtich is on. For x64 architecutre, the maximum size of user mode space can be between 7TB to 128 TB, that depends on Windows version. However, it is not likely to see the size of a process larger than the memory limits. By using volatility framework, it is possbile to enumerate running and recently exited process and also, all pagesof the process images of a specifc Process ID can be extracted for further forensic analysis. Figure 15 is the layout of process image.

For application-level analysis, the main objective is to find location of data structure of desired application and it requires knowledge about data structures of the application. For open source applications, it can be achieved by code reviewing of the application and for closed source application, this apporach can not be applied. For Google Chrome, Google offers open source version of Chrome browser called Chromium and it have most of the same features as Google Chrome with slightly differences such as automatic update patch installation, default media codec installation and default flash player. From the review of chromium source code, several class names related to incognito mode and class names that can flag the usage of incognito mode. From the analysis of unknown data, it can give the examiner supporting information about evidence.

For both known and unknown data artifacts, yara pattern matching tool is selected to use a effecient scan of patterns of data from memory images. Carving of memory mapped files from process images is carried out with scalpel program. The details of the process can be seen at the following sections.

##### Pattern Searching of Known Data

As it mentioned at Data Extraction and Expected Deliverables section, Known data is type of data, that forensic analyzts gather from case briefings. In this research, it implies the input user makes during the experiment. Yara rules are generated by using the evidence keywords, browsing URLs and also created rules for finding usernames, email addresses and passwords. One point to identify is that character encoding format of Chrome, that can affect allocation of characters on memory content. There are 2 encoing formats which are Unicode and ASCII. Chrome default encoding format is UTF-8 but user can change the encoding format such as UTf-18, ASCII and so on. UTF-8 takes 1 byte per characters and UTF-16 takes 2 bytes per characters. For text representation of Chrome, it is likely to see UTF-8 because modern websites uses UTF-8 charcter sets. For source code of Chrome, it it necessary to define input as ASCII. Yara can handle both Unicode and ASCII character encoding by setting as a flag.

##### Pattern Searching of UnKnown Data

Memory process images contain executable of a process which contains the compiled source code of the process and by extracting variables and class names. Yara is advanced searching tool and it is effecient to scan fragemented data like memory because of its support of regex, binary and texual data, programming conditions. As for malware researchers, it is convient to create rules for a particular badware for a quick scan of the memory images and running process. However, it is not only limited for malware reserachworks, it can also apply for digital forensic analysis that requires searching subsequence characters and strings. As for unknown data, forensic analysts can construct yara rules to find traces of data artifiacts in physical memory. 

From code review of Google Chromium project, there are several classnames that is used through the execution path of Incgontio private browsing mode.


##### File Carving

##### 4.4.2 Analysis of Memory contents on persistent Storage

All modern operating systems have memory paging and virtual memory are allocated at persistent storage to offer the program a big continuous linear memory address space. There are 3 type of files Windows operating system stores virtual memory contents  on the persistent storage, which are 
Swap file 
Hibernation file
crash dump file. 

Windows swap file, pagefile.sys is a read-only binary file that can find in the root directory of system partition. It’s a defragmented page file with pages from physical  memory are dispersed throughout the file. It is not likely to see multiple contiguous pages, and for this reason, analysis of swap file is limited with strings searching for data size less than 4 kb such as passwords, usernames and email address. For windows 8 and 8.1, there is another swap file called swapfile.sys for modern apps. Yara Patterns constructed for volatile memory are scanned through swap file to see traces of browsing artifacts.

Hibernation file is a compressed memory content of system stage in a Microsoft proprietary format. The contents of the file are loaded into physical memory when the system is activated. In the case of system in hibernation mode, it is an important data source to analyze stages of the system and memory. It is located at the same location as swapfiles in Windows Operating system. If the forensic analyst can log in to the system, it is able to turn on hibernation services and extract the file from system disk partition. Volatility supports analysis of hibernation file format, and forensic analysis procedure and pattern searching analysis are carried out using Volatility framework and Yara tool.

The last file that can find memory content is crash dump file. At normal usage, Windows operatng system creates crash dump file if the system occurs fatal error. According to Microsoft support, user can create a crash dump file by using a specific key board input,CLTR+(ScrollLock)x2, and another method is to set up at startup/shutdown tab of System propoerties. Even though Volatility support of crash dump file analysis. it needs to be a full memory dump. In other words, solely kernel memory dump or crashing application dump is not possible to analyze with Volatility. Another useful plugin from Volatility is called raw2dump which can convert raw physical memory dump to crash dump format, which is useful if the forensic analyzt wants to use WinDbg kernel debugger with memory dump. One significant drawback of crashdump acqusition is that it leaves the fiel system in a unclean stage and the page file needs to be larger than size of physical memory at least 1 MB. 

In this research work, swap file and hibernation dump files are analyzed from experiment scnearios. However, crash dump file are not considered to analyze at the experiment but it is possible to analyze crash dump file with similar procedure as physical memory raw dump analysis. 

#### Experiment Details

4.4 Experiment Details

In order to make sure that Chrome doesn’t store unrelated data from previous use, the experiment is carried out at a clean environment with only default Windows application. Google Chrome is installed with standalone installer and it runs as a desktop Windows mode. Due to limitation of resources, only 1GB memory is shared from host system to virtual machine. Windows 8 recommend minimum 512 MB memory to run system processes and also Chrome is consuming is relatively higher than other browsers. For this reason, it is likely to see memory contents on swap file and hibernation file. 

4.4.1 Scenarios

First scenario is to imitate the case of encountering suspect's live system with running applications and the user is recently interacting with the application. In this situation, it is possible to capture state of the running system and data from both physical memory and disk image. This is the stage with the highest possibility to find evidence because the application is still running and it is likely to capture stages of application. However, correctness and fidelity of captured images depends on acquisition methods. For e.g, if the forensic analyst can not promote to administrator privilege, it is still have a challenge in capturing forensically sound images. Acqusition occurs after each website is spawned and time period of browsing each website is approximately 5 minutes. 

Second scenario is the state of live running system without running application. In other words, the system is live but the user exited the application at a certain period. However, the system is in idle stage, third party foreground application are not running and the system has not been using for any other purposes. In this case, physical memory and disk image can be captured but memory allocation of closed applications might not be allocated anymore. It depends on the size of RAM, number of running process and period of acquisition time and time of existed application. Acqusition occurs after 15 minutes the browser closes with no interaction to the system.

Third scneario is that the system is in hibernation state after the applicaiton is recently closed. Hibernation file contains content of physical memory and the file size is the same with physical memory. As for Windows 8 and 10 Operating systems,it is likely to find hiberfile.sys even though the hibneration feature is turn off. The reaons is due to new boot startup scheme, that is a hybrid mode between cold boot and hibernation mode. This "hybrid shutdown" mode saves kernel address spaces into hiberfile.sys. Forensic analyzts can extract swap file, hibernation file to see states of the system. Volatility memory analysis support analysis of hibernation dump. At the experiment, system is hibernated after 20 minutes the browser closes.

Fourth scneario is the sytem is rebooted and the program is started for the next use. Changes in timestamp of the Chrome's data artifacts can be analyzed and memory content is wiped out when the system does clean reboot. In the case of cold boot acqusition, it is possible to prolong memory contents which are degrading slowly by cooling down RAM and to extract integral part of RAM at a particular time period. 

The following scenarios are not carried out to limit the scope of the research work and also its low possibility to extract browsing artifacts from the analysis of preliminary experiments;

Live running system with closed application and ther user has been interacting with other applications afterwards. The traces in memory contents are likely to replace by other processes. It depends on several factors which are size of RAM,number of running process and size of allowed swap space.

For power-down system, the resources that can rely to extract traces of browsing data is from swap files and disk image. In this case, it is possbile to apply the analysis procedure to examine and invistigate browsing artifacts.

Total of 7 memory dumps and 3 disk images are captured for these 4 scnearios. Figure 16 describes the timeline presentation of the experiment and the action with orange colored box is the period while acqusition occurs for physical memory and disk images.


4.5 Evaluation

Even though there are public forensic corpora, there is no test data and disk images for application specific research study. For this reason and also the variations of research approach and environment setup, it is not possible to evaluate the findings and result with other research works. All memory dumps and disk images will be validated with cryptographic checksum to verify the integrity of the acquired disk images. During acqusition, resuources of the websites are downloaded to file system after the acqusition. The purpose if to perform a quantitative assement of files and data recovered from captured memory. Percentage of user input found in data sources is also calculated. Also, Mean number of times repeated user input found in caputred images is also formuliazed. For unknown data, Chrome's Incognito mode identifier is analyzed and invistigate the usage of Chrome Incognito mode and reconstrcut user activities event timeline. 

##### Percentage of user input found in captured images

For Known data such as evidence keywords and urls, the propotion of user data found in the disk images is calculated. For e.g, 8 out of 10 evidence keywords are found in the memory, it can be said as 80% of the evidence keywords are dispersed through the memory images. For carved files from memory, it is validated with cryptographic checksum to see whethere actual files downloaded from the website and files recovered from data sources are the same content or not. From that point, percentage of files recovered are calculate by file types.

##### Mean number of user input repeated in captured images

It is likely to see repetate user input throughout disk and memory images. Mean number of evidence keywords and URLs are calculated. For e.g., a website URL,'www.xyz.com' is found in 3 different locations at memory as "xyz..","www.xyz..." and "xyz.com", mean number of user input,"xyz", is 3.

##### Reconstruction of user activities

From extraced information from application level data, user input can be reconstructed by sifing these pieces of information to determine user activities. Evidence that can extracted from each scneario is different, and reconstruction of user activities is be treated as different case. For each scneario,a series of analysis are performed to gather the following informaiton;
1. Is there any traces of incognito browsing mode?
2. Is there any traces of Browsing Data artifacts? 
3. By using information from step 1 and 2, analyze patterns of data and possible user activities event are reconstructed. 

The summary findings of the research are compared with previous research works and make a comparison of methodology and its effects to the result. Last but not least, the list of the research limitation is described at chapter xx, Conclusion and discussion.

### Summary
In this chapter, it is detailed the methodology of extracing applicaiton level information from Google Chrome's Incognito mode. Four scnearios are carried out during the experiment and investigate using anaysis procedure for persistent storage, memory content on persistent storage and, volatile memory analysis is presented. Evalution of the methodology is measured using quantative assessments and also by reconstructing user activites from extracted information. 
