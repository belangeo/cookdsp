Stereo amplifier controlled with decibel values
-----------------------------------------------

This tutorial shows the usage of a basic utility of the library, the `dbtoa` 
function.

The goal is to control the gain of a stereo input with a dB slider.

#### Step 1 - Setting up the plugin ####

The very beginning of our plugin is to give it a name, import the CookDSP
library and display the gain slider:


    /* Stereo amplifier controlled with decibel values. */

    desc:Stereo Amplifier

    import cookdsp.jsfx-inc

    slider1:0<-60,18>Decibel Gain

#### Step 2 - Reading slider values ####

Now, because our slider gives decibel values and sample amplitudes are linear, 
between 0 and 1, we need to convert our values before using them. In a 
**@slider** code section, we will use the `dbtoa` function to convert our 
decibels into linear amplitude values:


    @slider
    amp = dbtoa(slider1);

#### Step 3 - DSP processing ####

Finally, in the **@sample** code section, we just need to multiply each channel 
with the amplitude value saved in the `amp` variable:


    @sample
    spl0 *= amp;
    spl1 *= amp;

#### Step 4 - Smooth transition to new amplitude value ####

At this point the complete souce code for the plugin is:

    /* Stereo amplifier controlled with decibel values. */

    desc:Stereo Amplifier

    import cookdsp.jsfx-inc

    slider1:0<-60,18>Decibel Gain

    @slider
    amp = dbtoa(slider1);

If we test this plugin in Reaper, we may hear undesired clicks whenever we 
change the gain value. The reason  is that amplitude changes abruptly, 
resulting in steps and discontinuities in the resulting waveform. 
In order to avoid this, we will ensure a smooth transition of amplitude value 
over the duration of one signal vector.

We do this by introducing the variable **amp\_dsp** that will be used in the DSP processing.
First we calculate the stepwise aplitude increase **dsp\_inc** in the **@block** code section:

    @block
    amp_inc = (amp - amp_dsp) / samplesblock;

Next, in the **@sample** code block we increment **amp_dsp** gradually:

    @sample
    amp_dsp += amp_inc;
    spl0 *= amp_dsp;
    spl1 *= amp_dsp;

Finally we need to ensure that **amp\_dsp** is properly initiated in the **init** 
code section:

    @init
    amp_dsp = amp;

#### Complete plugin ####

    /* Stereo amplifier controlled with decibel values. */
    
    desc:Stereo Amplifier
    
    import cookdsp.jsfx-inc
    
    slider1:0<-60,18>Decibel Gain
    
    @init
    amp_dsp = amp;
    
    @slider
    amp = dbtoa(slider1);
    
    @block
    amp_inc = (amp - amp_dsp) / samplesblock;
    
    @sample
    amp_dsp += amp_inc;
    spl0 *= amp_dsp;
    spl1 *= amp_dsp;
