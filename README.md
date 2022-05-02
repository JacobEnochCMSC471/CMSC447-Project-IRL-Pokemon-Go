# CMSC447-Project-IRL-Pokemon-Go
A project that consists of 5 iterations of an agile development cycle. 

### Current Release: v0.3.0-prealpha 

### FOR TESTING:
* Change directory to outer PGIRL directory ...\PGIRL -> `python manage.py test` in terminal to run the tests
* ~~One test in \PGIRL\Photo_Uploader\tests.py fails because I'm still unsure about how to make the client POST correctly for the image upload form.
* The issue above with the failing test has been fixed. 
* As far as we know no special configurations must be made to have the software run
* Run instructions: Simply change directory via terminal to the top-level PGIRL directory and type `python manage.py runserver` to run the server. Click IP address in console to connect.
* There are now links to the WIP upload, inventory and verification pages. No URL editing in the address bar required! 
* All tests found throughout all of the applications can be ran via `python manage.py test`
* The verification test requires the installation of selenium and webdriver. The lines to do so are: 
    pip install selenium &
    pip install webdriver-manager
* Tests for individual applications can be ran via `python manage.py test <Applicaton Directoy Name>`, eg `python manage.py test Photo_Uploader` for upload tests only

