Hard clipping distortion
------------------------

This tutorial shows the usage of a simple function of the library, the `clip` 
function.

We will use it to constrain the signal between a low and a high threshold, with 
post-processing power restoration.

#### Step 1 ####

The very beginning of our plugin is to give it a name, import the CookDSP 
library and display the threshold slider:


    /* Hard Clipping Distortion with Power Restoration. */

    desc:Hard Clipping Distortion

    import cookdsp.jsfx-inc

    slider1:1<0.01,1>Amplitude Threshold

#### Step 2 ####

In order to do the power restoration step in our process, we need the inverse
of the threshold. We will compute it in the **@slider** code section and keep
it in a variable `ithresh`:


    @slider
    ithresh = 1 / slider1;

#### Step 3 ####

Finally, in the **@sample** code section, we will clip the signals with a
threshold given by `slider1` and restore the power with the `ithresh` variable:


    @sample
    spl0 = clip(spl0, -slider1, slider1);
    spl1 = clip(spl1, -slider1, slider1);
    spl0 *= ithresh;
    spl1 *= ithresh;

#### Complete plugin ####

    /* Hard Clipping Distortion with Power Restoration. */

    desc:Hard Clipping Distortion

    import cookdsp.jsfx-inc

    slider1:1<0.01,1>Amplitude Threshold

    @slider
    ithresh = 1 / slider1;

    @sample
    spl0 = clip(spl0, -slider1, slider1);
    spl1 = clip(spl1, -slider1, slider1);
    spl0 *= ithresh;
    spl1 *= ithresh;

