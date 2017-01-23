/******************************************************* 
POBJECTS
========

Polyphonic objects.

A `Pobject` is the polyphonic variation of a current object in
the library. It works exactly as the original object but every
arguments for its methods must be a CookDSP list instead of a 
single value. The _do() method also returns a list holding all 
internal objects output values.  

In addition to importing **cookdsp.jsfx-inc**, to use the polyphonic
objects you also have to import **cookdsp/pobjects.jsfx-inc**. It is
a separated import in order to accelerate the loading of the standard
library. pobjects.jsfx-inc is a fairly big file.

Available `Pobjects` are:
    
%s

They must be used with a variable name as prefix (object oriented).

Here is an example, using the `follow` object, of the method 
signatures:

Initializer
-----------

#### Pfollow(lst1) ####

Initializes as many envelope follower as the length of the list
`lst1`, corresponding to the `freq` argument of `follow`.

Methods
-------

#### Pfollow_set_freq(lst1) ####

Sets a new cutoff frequency, in Hz, to each of the internal
`follow` object. The list `lst1` must be of the same length
as the list given to the initializer.

#### Pfollow_do(signal) ####

Processes one samples of a multi-channel input signal `signal` 
and outputs a list of amplitudes, between 0 and 1. The argument
`signal` must be a `tmp` list of any length, the method will 
wrap around the inputs to fill every internal object. This
method returns a CookDSP list (ie starting at index 1, index 0
hold the list length).

Example
-------

    desc:Stereo Amplitude Follower

    import cookdsp.jsfx-inc
    import cookdsp/pobjects.jsfx-inc

    slider1:10<1,100>Follower Responsiveness In Hz

    @init
    // Initializes cutoff frequencies
    freq = set(2, slider1);
    // Initializes the followers
    fol.Pfollow(freq);

    @slider
    // Sets follower's responsiveness
    freq[1] = freq[2] = slider1;
    fol.Pfollow_set_freq(freq);

    @sample
    // Follow a stereo input signal
    amps = fol.Pfollow_do(tmp(spl0, spl1));
    // Add modulated noise to the input signal
    spl0 += (rand(2) - 1) * 0.5 * amps[1];
    spl1 += (rand(2) - 1) * 0.5 * amps[2];

********************************************************/
