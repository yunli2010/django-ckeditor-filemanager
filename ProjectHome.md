Thanks to **CKEditor** we all now have to fork out huge piles of money for **CKFinder**... cheeky. I got incredibly fed up with this factor so I hunted around for an alternative to **CKFinder**. What I found was http://is.gd/8ViHb - **An Open File Manager for CKEditor 3.0**.

Great! One snag: there was no connector for Django, and the Python module they wrote didn't work at all.

Along with the **File-Manager** connector, what I really needed was a stupidly-simple base package - something I can quickly build onto, and doesn't throw me hassles of having to configure Django's already awesome framework to get a project actually going.

I needed something that includes a couple of standard models (Nothing fancy, and not using flatpages - I found flatpages annoying when trying to build up any of my projects) so that I could seriously hit the ground running.

I prayed for something I could quickly download and extend off of; effectively so that I could get a _brochure_ site up and running in couple of hours.

If this is what you've been looking for too, look no further. I've taken the best of the web: **Open File-Manager**, **CKEditor 3.0**, the **Flickr API** and I've created a neatly boxed base package. It includes a couple models under a 'common' app, with a nice standalone Python fixture in 'lib' too.


**1.** Download the repo or extract the **zip file** that is in the repo (I placed it in there so that you have access to the project unassociated to SVN). Access the 'newproject' folder:
```
svn checkout http://django-ckeditor-filemanager.googlecode.com/svn/trunk/newproject/ newproject
```

**2.** Synchronize the Database:
```
./manage.py syncdb 
```

**3.** optionally, change your database setup to mysql, then go into 'lib' in terminal and run:
```
$python new_fixtures.py
```

**4.** Run the Server
```
./manage.py runserver
```

Give the project a full run through. Log into the admin area and click on 'Pages'. **CKEditor** will load up; click the **image icon** then **browse the server**. You should successfully be able to use **CKEditor** with **Open File-Manager**.

The Project also comes with  **Flickr** support so that you can have a Gallery (setup you're **user-token** and **key** in settings.py).

The **Contact us** form writes emails to the /tmp/test\_emails/ folder provided EMAIL\_TEST\_MODE is set to True in settings.py too.

Please note; by downloading this, you understand that I hold no responsibility for your use of the code. I am responsible for placing each component in this project and working with it till it was properly functioning, however not all the code belongs to me.

The code in this package is open-source. The only thing I built was the **File-Manager connector**.

Let me know of your success, I'd love Feedback.

Regards,
Paul von Hoesslin.