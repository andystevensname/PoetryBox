# Poetry Box

Poetry Box prints poems on demand. Running on a Raspberry Pi, Poetry Box scrapes poems from the Poetry Foundation website with a Python script and stores them in MongoDB. When the user pushes the glowing white button, Poetry Box prints these poems with a Epson thermal receipt printer.

## Required Hardware
- Raspberry Pi 2 (or 3)
- A Button with LED
- Epson Thermal Reciept Printer (such as the TM-T88V)

## Required Software

- [png2pos](https://github.com/petrkutalek/png2pos)
- [phantomJS](https://github.com/fg2it/phantomjs-on-raspberry)

- MongoDB

- PyMongo
- PIL
- pyqrcode

## Instructions
- Run scrape.py
**NOTE:** This project is intended for educational and personal use only. All poems scraped from the Poetry Foundation website are subject to copyright law. As such, I will not be updating the scraper file, which no longer works with the Poetry Foundation website.

- Edit button.py to reflect the pins you have chosen for your button and LED.
- Add button.py to your Pi's startup processes
- Run button.py

## Further Thoughts
The main problem with the current setup is that MongoDB creates a lock file if the Raspberry Pi is not shutdown properly. In general this means if the Poetry Box loses power (via being unplugged) the device must be disassembled and the lock file manually removed. As of right now you can power down Poetry Box safely by holding down the button for a few seconds. However future iterations will most likely employ a different database.

