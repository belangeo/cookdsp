Scaling values from an input range to an output range
-----------------------------------------------------

In this tutorial, we will perform a common task in the DSP world, the 
conversion of a value lying in an input range to the corresponding value in 
an output range. We will use another basic utility of the library, the `scale` 
function. This function takes an input value and the bounding points of the 
input and output ranges and perform the translation according to a power
factor (useful to translate in a non-linear way).

The signature of the `scale` function is:
    
    ret = scale(input, xmin, xmax, ymin, ymax, ex)

We will control the gain of a stereo signal with a percentage between 0 and 
100. The left part of the signal will be affected with a simple linear scaling 
between 0 and 1. For the right part of the signal, we will add a power factor 
of 4 to give a curve more related to our perception of the amplitude.

#### Step 1 ####

The very beginning of our plugin is to give it a name, import the CookDSP 
library and display the percentage slider:

    /* Scaling values from an input range to an output range. */

    desc:Scaling values

    import cookdsp.jsfx-inc

    slider1:50<0,100>Volume

#### Step 2 ####

Now, we scale the value from the slider to get the gain values of both side
of our stereo signal. In a **@slider** code section, we will use the `scale` 
function to perform this task (pay attention to the gain curve of both 
channels):

    @slider
    ampL = scale(slider1, 0, 100, 0, 1, 1);
    ampR = scale(slider1, 0, 100, 0, 1, 4);

#### Step 3 ####

Finally, in the **@sample** code section, we just need to multiply each channel 
with the gain factors saved in the `ampL` and `ampR` variables:

    @sample
    spl0 *= ampL;
    spl1 *= ampR;

#### Complete plugin ####

    /* Scaling values from an input range to an output range. */

    desc:Scaling values

    import cookdsp.jsfx-inc

    slider1:50<0,100>Volume
     
    @slider
    ampL = scale(slider1, 0, 100, 0, 1, 1);
    ampR = scale(slider1, 0, 100, 0, 1, 4);

    @sample
    spl0 *= ampL;
    spl1 *= ampR;
