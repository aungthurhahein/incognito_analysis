## Introduction

### Motivation

1. Browswer contains valuable information in terms of forensic analysis such as 
2. Apple introdcues private browsing at 2005 and forensic analysts are analysing whether it is becoming anti-forensic technique or not
3. Criminals and non-technical users can get access this mode to commit electronic crimes and hides traces 
4. For this reason, It is important to recover digital artifacts left from private browsing mode

5. Chrome is leading brwoser in terms of tech & market share
6. Statistic shows that 45.6 market shares on both mobile and PC usage
7. it says it doesn't leave browsing artifacts on the system but past researchs show possibility to recover from it.

### Problem statement

1. possibility of recovering data from it
2. implementatio variations of browser makes research works difficult
3. no common standards  in digital forensic research work beacause of it's immature research area and few research works 

### Objectives

1. propose a method to recover browsing artifacts and resources from Chrome's incognito mode
2. analyze possiblity of recovering data from different data sources
3. analyze Google Chrome's data structures

## Background

### Methodology

1. A generic forensic process contains 4 process
2. In this section, i will emphasize on 2 important stages which are Acqusition & Analysis

### Data Acqusition
1. Acqusition types by system stages
2. If the system is power off, only can clone the HDD using hardware or software tools
3. If the system is alive, depends on other criteria, two ways to acquies the digital evidence; live acqusition of physical memory and HDDs

4. Another way to categorize acqustion is by the acqustion methods: hardware based acqusition or software based acqusition methods
5. hardware base acqusition methods have high atomicity but the hardware devices are expensive
6. software based methods are cost effective but doubutful in fedility of captured digital images

### Data Analysis
1. For physcial storage devices, Forensic Data analysis can be divided into 2 main categories: persistent storage analysis and physical memory analysis 
2. for persistent storage analysis, it can be classified into several categories based on types of evidence we are looking for and data resources
3. in this section, i will explan briefly about 3 analysis categories, which are memory analysis, swap space analysis and persistent storage analysis

#### Memory Analysis 
4. Physical memory contains unique data that can't be found in HDD. It's a buffer between CPU and HDD/Network.
5. It is important analysis source for forensic analysis related with network, current state of a system and traces can't find on disk.

6. At this time, there are several existing tools and frameworks to analyze physical memory dumps.
7. The following listing is some of the common memory forensic analysis tools.
8. Volatility is a well known memory forensic framework 
9. KnTools is the winner of DFRWS 2005 contenst for Windows OS 
10. Free GUI memory analysis tool by Mandriant cybersecurity firm
10. FATKit & Rekall are also frameworks like volatility 

Volatility is better!

#### Swap Space Analysis
1. For Windows system, there are 3 memory contents that can be found on disk: pagefile.sys, hiber.sys & crash dump file
2. changes of discovering pagefile is the highest followed by hiber.sys and crash dump file
3. only way to analyze is by string searching

#### Application Analysis
1. called next-generation analysis. focus on discovering past activities and data of a particular applications
2. Communicational Applications such as browser, email client, chat client are mostly focus on appliaction analysis.
3. The following figure is the view of histroy.sqlite from Google Chrome browser on disk.

4. As for memory analysis, memory context can be seen as several layer. 
5. Application analysis of memory focus on application address spaces 
6. physical address space to refer to the addresses that the processor requests for accessing physical memory
7. virtual address space s is single continous address space which program deal with 
8. virtual memory can be seen by operating system as user address space and kernel address space
9. for application analysis, focus of memory artifacts of applications in user address space

## Proposed Method

### Overview

1. The following figure describes the overview of research process of the proposed method.
User browses incognito mode and forensic analysts will preseve digital images of memory and hard disk. 
Forensic Analysis will perform to analyze existence of browsing artifacts.
As a presentation, these information will be presented as digital evidence.

2. As by comparing with theoritical framework, the proposed method can be seen as the following.

### Environment Setup 

### Tools

1. Focus on Volatility, Autopsy,Scalpel, Yara 

### Data Acqusition

1. Data Acqusition for persistent strorage uses FTKImager and 3 images captures
 
2. As for volatile acqusition,physical memory dumps are captured directly from VM emulator. 6 mem dumps are captured at 6 stages of exp.

### Data Analysis

1. There are 6 analysis steps for persistent storage analysis to analyze browsing artifacts. The details of each process will be explained with the output at preliminary experiment. 

2. For Volatile data analysis, there are 4 main analysis process and the detail proceure of each process can be seen at next 4 slides.


## Preliminary Experiment
1. talk about experiment result for both data sources
2. From this experiment, It is able to achive 2 objectives of the research which are 

3. 

## Related Works
1. Methodology comparison of 4 private browsing research works 
2. All of them focus on data recovery and past activity of browsers
3. 

## Research plan
1. 4 tasks to continue

## Thanks for your time and questions!














