# Lexicon
Beginnings of the language learner


### Parking Lot Notes

**Modules os, shutil, send2trash**
* Copy Files and Folders
 * copytree for subdirectories
 * renaming possible in destination
* Moving and Renaming Files and Folders
 * overwrite files in destination
 * if destination is a folder, add within, otherwise assume it is destination
 * destination path folders must exist
* permanently deleting files and folders
 * os module for single file or empty folder, shutil module for entire folder and contents
 * send2trash is a third party module to move things to trash/recycle bin
  * only sends to trash, cannot pull things out of it!
  * generally safer than a permamnent delete

**Walking a directory tree**
* os.walk("folder-name") - returns foldername, subfolders, and filenames
* does not change heirarchy of files
* python zipfile can read, extract from, and create zip files
 * This happens in the working directory by default
 * Can be done in a new folder that is created in the process as well
 * Creating zip files like writing to normal files
  * open file for writing
  * write mode will overwrite current contents of zip file
  * append mode to add zip files to main file in succession
  * close when done selecting files for zip

What files will your apps use?
	renaming and moving them all is pretty easy
	zip up and send away progress for recording
	stats on language learned
	daily activity files
	alphabet files
	take notes as you learn

