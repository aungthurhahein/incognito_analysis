# Planning Draft
    Aung
    Saturday, 12 September 2015
    updated: 07 October 2015

## To research
        1. swapfile.sys in Windows 8-10 (Done)
        2. Acquisition & Analysis of Hibernation (Done)
        3. Code Review of Chrome tracing Incognito execution path (Done)

## Experiment

### Input data (Done)
        1. To Create (Done)
            -  Fake Twitter Account 
            -  Fake SoundCloud Account
        2. Same input dataset with slight variations (Done)
        3. Get standalone version of latest Chrome version(46) (Ignore)

#i## Acquisition

        1. 4 images for hard-disk images at 4 stages (Done)
        2. 6 memory images after each websites loaded, one after the session expired, last one after the system reboots (Done)
        3. Website data are saved at each memory acquisition (Done; need to download them to local host)

        Time-line needs to note down for all events (browser open, acquisition time...) Done

### Analysis
        Analysis will need to do for 4 system stages(While session alive, after session expires, during system hibernates and after the system reboots)

#### Forensic Analysis (Autopsy & Volatility)
To plan:
	1. 2 set of rules for yara (known,unknown) (Done)
	2. keywords for Autopsy (Done)
	3. file headers and footers for scalpel 
	4. Carving should be done at work PC due to space issue

##### PSE
        - Default Chrome Artifacts analysis
        - File system analysis( allocated and Unallocated)
        - Investigate Time-stamp changes of digital artifacts 
        - Investigate data updates on chrome artifacts

##### Memory Contents on PS 
        - Memory Content on HD (swap space analysis, hibernation.sys)
	- Analyze hibneration file with volatility (Not possible. need to think to a new method)
	- Analyze swapfile with yara (page_brute) (Done)

##### VDE
        - Get Imageinfo
        - Extract Process IDs
        - Timeline analysis of process IDs
        - Dump Process images

#### Signature Analysis (Yara)
##### PSE
         - Swapspace analysis by pattern searching 'Known' data and 'unknown' data

##### VDE
         - Known Data (Experiment Website URLs, keywords, user-name, passwords...)
         - Unknown Data (ClassName,Variables, Methods from codereview)

#### File Carving (Scalpel)

        - Memory mapped files 
        - Data recovery from persistent storage (based on result of unallocated space and slack space of HD images)

#### Incognito identifier?

        - Look for identifier of opening/closing incognito mode
        - Hard disk and memory

### Result Summary
        - By Data Sources (Chrome artifacts,Persistent Storage,Volatiled ata)
        - By 3 system stages (while browser running, after the session closes, after system reboots)

## Evaluation
	1. Comparison with previous research works by experiment and result
        2. Actual Website Resources/carved files 
        3. proportion of discovered evidence keywords

## Document Update

    - methodology(Done), evaluation(Done) & experiment result
    - Conclusion and Discussion
    - Arrange sources(experiment files and so on)
    - Presentation 

