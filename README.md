# Clock
This was made for the Computer Science Final Summative assignment. The project is to create a functioning gui for a clock I tried to build last year. The clock is comprised of a 2.1 inch round lcd display, 2 keyboard switches, a rotary encoder, a realtime clock module and a speaker. 

The Success criterion for the project are as follows
1. The ability to display the time given by the real time clock module
2. The ability to set multiple alarms which do not overlap each other
3. The ability to change settings in a screen
4. Functioning inputs
5. Working speaker

## Instalation Guide
- Assemble the clock hardware
- Connect the qualia board to your computer
- Install the uf2 bootloader using the [adafruit guide](https://learn.adafruit.com/adafruit-qualia-esp32-s3-for-rgb666-displays/install-uf2-bootloader)
- Clone the repository with ```git clone https://github.com/owenashbury/Clock```
- Move the contents of the repository onto the Qualia
- Optionally install contents of the onboard lib on the board under lib to use only the required library

## User Manual 

### Clock View/Setting the Time
By default the clock will begin imediately displaying the clock view to set the time use the encoder to pick the correct time 

### Alarm View
To enter the alarm view press the encoder down to activate the button. You will see a view were you can set an alarm by rotating the encoder. Once you have selected the time you want press the button to set the alarm. This can be repeated if you set an alarm that is in the range of another alarm the alarm will not be set. You can set as many alarms as you want

### Trouble Shooting
- It is possible that the hardware could fail in this case you could try to reconnect it or reach out to adafruits support team
- If the program is crashing because of over use you could introduce a delay in the main loop using sleep(**your delay**)
- If the program contains a bug feel free to submit a github issue or contact me by email and I will try to resolve it

### Remaining Fixes
- [ ] Set time with encoder
- [ ] Alarm
  - [ ] Icon
  - [ ] Sound
  - [ ] Set hour than minutes 
- [ ] Final Enclosure
