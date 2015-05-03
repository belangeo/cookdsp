Stereo amplifier controlled with decibel values
-----------------------------------------------

This tutorial shows the usage of a basic utility of the library, the `dbtoa` 
function.

The goal is to control the gain of a stereo input with a dB slider.

#### Step 1 ####

The very beginning of our plugin is to give it a name, import the CookDSP
library and display the gain slider:


    /* Stereo amplifier controlled with decibel values. */

    desc:Stereo Amplifier

    import cookdsp.jsfx-inc

    slider1:0<-60,18>Decibel Gain

#### Step 2 ####

Now, because our slider gives decibel values and sample amplitudes are linear, 
between 0 and 1, we need to convert our values before using them. In a 
**@slider** code section, we will use the `dbtoa` function to convert our 
decibels into linear amplitude values:


    @slider
    amp = dbtoa(slider1);

#### Step 3 ####

Finally, in the **@sample** code section, we just need to multiply each channel 
with the amplitude value saved in the `amp` variable:


    @sample
    spl0 *= amp;
    spl1 *= amp;

#### Complete plugin ####

    /* Stereo amplifier controlled with decibel values. */

    desc:Stereo Amplifier

    import cookdsp.jsfx-inc

    slider1:0<-60,18>Decibel Gain

    @slider
    amp = dbtoa(slider1);

    @sample
    spl0 *= amp;
    spl1 *= amp;

