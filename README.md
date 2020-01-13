# The-generating-tool-of-non-recursive-zipboom
## Introduction
This tool is a non-recursive zip bomb batch generator based on "zipbomb-20190822.zip" provided by David Fifield and is a python3 script. （I have provided this zip file. If you need the latest version or need to learn more about non-recursive zipbomb, please enter https://www.bamsoftware.com/hacks/zipbomb/）

This script was written by the way because of my experimental needs, so it doesn't look so formal (of course, my own code level is also limited)

## How to run it
Please run this script in the same directory as the file "zipbomb". This script provides all the zipbomb batch generation commands mentioned in the "MakeFile" file except zbxxl.zip and zbxxl.extra.zip, because these two commands will consume a lot of RAM and take a lot of time.

## How to use it
### Format
The code format is as follows:

'
These are for xx


(code)
'
### Usage

Find the corresponding code according to the size of the zip bomb you need to generate in batches.


'for i in range(100)' --> 100 is the number of bombs you want to generate  

'
    mode = "quoted_overlap"
    
    num_file = random.randint(100000, 190023)
    
    compressed_size = random.randint(10000000, 22982788)
'  
--> Modify these parameters according to your needs（Specific can go to "MakeFile"）

