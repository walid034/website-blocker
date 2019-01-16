# website-blocker
A python script that runs on the background and blocks websites for a certain time. Blocks by modifying the windows hosts file

<h3> Instructions (windows only) - </h3>

1. Open task scheduler
2. Action -> Create task
3. Give it a name and check "Run with highest privileges"
4. Go to 'Triggers' tab, click 'New...' and select 'begin the task'-> At Startup.
5. Go to 'Actions' tab, click 'New...'. Under settings browse the file 'blocker.pyw'. Click 'Open'
6. Uncheck the boxes under Power in 'Conditions' tab if you are on a laptop.
7. Click ok. The task should be listed in task scheduler library.

The original hosts file is in the repository for convenience.
