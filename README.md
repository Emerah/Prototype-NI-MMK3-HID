# Prototype-NI-MMK3-HID

the problem we are trying to solve is the problem of gaining access to the gorgeous screens found on newer generation ni products, namely komplete kontrol smk2 series and maschine mk3.

this can be very useful if we for example want to use one of those ni products with ableton live and be able to see meaningful feedback on the screens instead of using the old and ugly mackie control protocol for text display. to make things worse, mackie is only available on the maschine mk3 hardware and not the komplete series.

for this prototype engine we will try to accomplish 1 thing:

 - send valid data messages to Maschine MK3 to **fill the screens with colors**.
  
we will assume since we know the product ids of all NI products with similar screens, that what works here will also work with komplete keyboards from the S mk2 family. in order to be able to access Maschine MK3 screens and therefore be able to accomplish the goal of this prototype that is, filling the screens with colors, we must suspend ni drivers.

---

**Suspending ni backend support services**

ni products are back-powered by ni drivers that handle all communications between the hardware device and ni applications running on your computer like komplete kontrol and maschine 2 software or other midi-capable software. as soon as your computer starts, these drivers claims control of the hardware and therefore before we are able to send date to the screens, we must suspend these background processes/drivers to be able to claim control of the hardware to ourselves. 

this operation is complletely safe. as soon you start maschine 2 software or at worst restart your computer, the drivers start up and immidiately claim control of the Maschine MK3 hardware device again.

**Platform**
the code in this prototype was developed on **macOS** 10.14.6 and 10.15.x. since we must accesses the system to suspend ni drivers the code will only work on **mac**.
developed with **python 3.7.7**

**Required**

this prototype uses **pyusb**, which uses **libusb** as its backend. both must be installed before this prototype will work on your computer

    brew install libusb
    pip install pyusb

**How to run**

in terminal, cd to this package folder and type:

    python3 main.py

script will ask you to agree to suspending ni drivers. if you choose yes, the script will run and you should see you Maschine MK2 screens blinking in random colors.
