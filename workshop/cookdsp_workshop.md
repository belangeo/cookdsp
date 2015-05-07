%title: CookDSP - JIM2015 - Workshop
%author: Olivier Bélanger
%date: 2015-05-06

-> Création de plugiciels audio avec le langage JS de Reaper <-
===============================================================

^
* Introduction au langage JS de Reaper
^
    - Structure d'un plugiciel JSFX
^
    - Les descriptions
^
    - Les sections de code
^
    - Les éléments de langage
^
    - Variables réservées
^
    - Programmation orientée-objet
^
* Présentation de la librairie CookDSP
^
    - Objectifs
^
    - Gestion de l'espace-mémoire
^
    - Les outils de conversion
^
    - Les objets de traitement audio
^
    - Traitement dans le domaine spectral
^
    - Création d'instruments MIDI
^
* Suggestions de projet

-------------------------------------------------

-> Introduction au langage JS de Reaper <-
==========================================

Documentation du langage JS: 

    http://reaper.fm/sdk/js/js.php

Basé sur le langage EEL:

    http://eelang.org/

^
## Structure d'un plugiciel JSFX

^
- Simple fichier texte (portable)
^
- Compilé à la volée à même le séquenceur
^
- Composé de *descriptions* et de *sections de code*

-------------------------------------------------

-> Structure d'un plugiciel JSFX <-
===================================

## Les descriptions

Une description est un mot clé suivi du symbole deux-points (:)  
et d'une structure de data.

^
*desc* : Titre du plugin

    desc:Fantastic Distorsion

^
*slider1*, *slider2*, ..., *slider64* : Définition des contrôles

    slider1:5000<20,20000>Cutoff Frequency
    slider2:0<0,2,1{Hanning,Blackman,Bartlett}>Envelope

-------------------------------------------------

-> Structure d'un plugiciel JSFX <-
===================================

## Les sections de code

Les sections de code permettent de définir les opérations à  
effectuées aux diverses étapes du traitement.  
Une section est définie par la syntaxe *@nom_de_la_section*.

^
*@init* : Code exécuté à l'initialisation du plugin

^
*@slider* : Code exécuté lorsque l'interface est manipulée

^
*@block* : Code exécuté juste avant chaque bloc d'échantillons

^
*@sample* : Code exécuté à chaque instant d'échantillonnage

^
*@gfx* : Code exécuté à chaque rafraîchissement d'écran

-------------------------------------------------

-> Éléments de langage <-
=========================

Le langage JS est écrit avec le langage EEL2  
(Extensible Embeddable Language)

^
- Syntaxe comparable à celle du C.

^
- Conçu pour l'écriture temps réel de scripts multimédia.

^
- Offre une puissance de calcul comparable aux langages compilés.

^
- Peu de dépendances, facile à intégrer.

-------------------------------------------------

-> Éléments de langage - syntaxe <-
===================================

^
- Variables non-déclarées, globales par défaut, double précision

^
- Un commentaire est indiqué à l'aide des symboles *//* ou */\* \*/*

^
- Séparation des déclarations à l'aide du symbole *;*

^
- Les parenthèses servent à créer un groupe d'opérations...

^
- ... et à clarifier l'ordre des opérations mathématiques

^
- On indexe la mémoire du plugin avec les crochets: `buf[0]`

^
- Les instructions conditionnelles utilisent la syntaxe:

-> `condition ? code si vrai : code si faux` <-

-------------------------------------------------

-> Éléments de langage - variables réservées <-
===============================================

Un certain nombre de variables sont réservées à l'intérieur du plugin.

^
*slider1*, ..., *slider64* : Noms réservés aux variables des sliders.

^
*spl0*, ..., *spl63* : Noms réservés aux 64 variables audio possibles.

^
*srate* : Donne accès à la fréquence d'échantillonnage courante.

^
*play_state* : Indique l'état courant de la lecture (play, stop, etc.).

^
*play_position* : Position courante, en secondes, de la lecture.

^
*tempo* : Valeur de tempo, en _bpm_, du projet courant.

^
*$pi* : Valeur mathématique de *pi*!

-------------------------------------------------

-> Éléments de langage - code orienté-objet <-
==============================================

Le langage JS offre une implémentation simple de la programmation  
orientée-object à l'intérieur des définitions de fonctions.

^
Le préfixe *this* permet la persistance des variables. Ces variables  
conservent leur valeur entre deux appels de fonction.

    function saw(freq)
    (
        this.inc = freq * 2 / srate;
    );

^
Pour créer un objet, on fait précéder l'appel de fonction par un nom  
de variable unique.

    osc1.saw(100);

-------------------------------------------------

    @init
    function saw(freq)
    (
        this.phs = 0; 
        this.inc = freq * 2 / srate;
    );
    function saw_do()
    (
        val = this.phs;
        this.phs += this.inc;
        this.phs >= 1 ? this.phs -= 2;
        val;
    );
    osc1.saw(100); osc2.saw(150);
    //
    @sample
    spl0 = osc1.saw_do() * 0.5; spl1 = osc2.saw_do() * 0.5;

-------------------------------------------------

-> La librairie CookDSP - objectifs <-
======================================

^
- Environnement d'exploration du DSP simple et versatile

^
- Courbe d'apprentissage très rapide

^
- Intimement lié à l'environnement de composition

^
- Nécéssite peu ou pas d'expérience en programmation

^
- Cacher les aspects techniques inutiles à l'apprentissage du DSP

^
- Qualité audio professionnelle!

^
-> `http://ajaxsoundstudio.com/software/cookdsp/` <-

-------------------------------------------------

-> La librairie CookDSP - gestion de la mémoire <-
==================================================

Un plugin JSFX offre une mémoire virtuelle indépendante d'environ  
8 millions de mots (~3 minutes de son monophonique à 44.1 kHz).

^
On indexe dans cette mémoire avec la syntaxe suivante:

    startpoint[index]

L'addition du point de départ et de l'index donne la position de  
lecture (ou d'écriture) dans la mémoire.

^
______________________________________________________________________

Cette technique oblige une gestion manuelle et fastidieuse des  
blocs de mémoire (enveloppes, formes d'onde, mémoires audio, etc.)
 
-------------------------------------------------

-> La librairie CookDSP - gestion de la mémoire <-
==================================================

L'exemple suivant illustre la création de trois blocs de mémoire.  
Le premier contient une enveloppe hanning de 1024 points et les  
deux suivants réservent un espace-mémoire stéréo de 1 seconde.

    @init
    env = 0;
    bufL = 1024;
    bufR = bufL + srate;
    k = 0;
    loop(1024,
        env[k] = −0.5 ∗ cos(2 ∗ $pi ∗ k / 1024) + 0.5;
        k += 1;
    );

^
Qu'arrivera-t-il si on augmente le nombre de points de l'enveloppe?

-------------------------------------------------

-> La librairie CookDSP - gestion de la mémoire <-
==================================================

La fonction *memalloc* et les objets *buffer*, *delay* et *sdelay*  
utilisent tous un index commun dans la mémoire globale du plugin.

^
L'exemple précédent, avec la librairie CookDSP devient:

    import cookdsp.jsfx-inc
    //
    @init
    env.buffer(1024);
    env.buffer_window(1); // hanning
    bufL = memalloc(srate);
    bufR = memalloc(srate);

-------------------------------------------------

-> La librairie CookDSP - outils de conversion <-
=====================================================

CookDSP offre des fonctions servant à la conversion de valeur.  
Ce ne sont pas des objets, donc pas de variables en préfixe.

^
    import cookdsp.jsfx-inc
    //
    hz  = mtof(60);     // midi to hertz
    tr  = mtot(48, 60); // midi to transpo
    mid = ftom(261);    // hertz to midi
    amp = dbtoa(-6);    // decibels to amplitude
    db  = atodb(0.707); // amplitude to decibels
    // any conversion with power factor
    y   = scale(x, 0, 127, 0, 1, 3);

-------------------------------------------------

-> Exemple - contrôle du gain en dB <-
======================================

    /* Stereo dB amplifier */
    desc:Stereo Amplifier
    //
    import cookdsp.jsfx-inc
    //
    slider1:0<-60,18>Decibel Gain
    //
    @slider
    amp = dbtoa(slider1);
    //
    @sample
    spl0 *= amp;
    spl1 *= amp;

-------------------------------------------------

-> La librairie CookDSP - objets audio <-
=============================================

On intialise un objet à l'aide de la fonction qui porte son nom  
(précédée d'un non de variable unique):

    import cookdsp.jsfx-inc
    @init
    dL.disto(0.9, 3500); // drive, lowpass cutoff
    dR.disto(0.9, 3500);

^
On calcule un échantillon du processus à l'aide de la fonction  
*objectname_do()* (toujours précédée de son nom de variable):

    @sample
    spl0 = dL.disto_do(spl0) * 0.5;
    spl1 = dR.disto_do(spl1) * 0.5;

-------------------------------------------------

-> La librairie CookDSP - contrôle des paramètres <-
====================================================

On contrôle les paramètres d'un objet à l'aide des méthodes  
*objectname_set_xxx* (où *xxx* est le nom du paramètre à modifier).

^
Assignation de potentiomètres aux paramètres de la distorsion:

    slider1:0.9<0.5,1>Drive
    slider2:0.7<0,1>Slope
    //
    @slider
    dL.disto_set_drive(slider1);
    dR.disto_set_drive(slider1);
    hz = scale(slider2, 0, 1, 500, 10000, 4);
    dL.disto_set_cutoff(hz);
    dR.disto_set_cutoff(hz);

-------------------------------------------------

    desc:Distortion with Controls
    import cookdsp.jsfx-inc
    slider1:0.9<0.5,1>Drive
    slider2:0.7<0,1>Slope
    @init
    dL.disto(0.9, 3500); 
    dR.disto(0.9, 3500);
    @slider
    dL.disto_set_drive(slider1); 
    dR.disto_set_drive(slider1);
    hz = scale(slider2, 0, 1, 500, 10000, 4);
    dL.disto_set_cutoff(hz); 
    dR.disto_set_cutoff(hz);
    @sample
    spl0 = dL.disto_do(spl0) * 0.5;
    spl1 = dR.disto_do(spl1) * 0.5;

-------------------------------------------------

-> La librairie CookDSP - contrôle des paramètres <-
====================================================

Certains objets présentent des méthodes de contrôle supplémentaires:
 
    import cookdsp.jsfx-inc
    //
    @init
    d.delay(srate);
    //
    @slider
    x = slider1 * .001 * srate; // ms to samples conversion
    //
    @sample
    v = d.delay_read3(x);   // read with cubic interp 
    in = spl0 + v * 0.5;    // with a bit of feedback...
    d.delay_write(in);      // ... write value in delay line
    spl0 = (spl0 + v) * .5; // sum and output

-------------------------------------------------

-> La librairie CookDSP - attributs des objets <-
=================================================

Si un objet génère plusieurs valeurs en cours de processus, ces  
dernières seront accessibles via des attributs d'objet. On récupère  
les attributs via la syntaxe *objectvar.attribut*:

    @init
    hlb.hilbert(); // Hilbert transform
    ph.phasor(200, 0);
    //
    @sample
    ph1 = ph.phasor_do();
    ph2 = wrap(ph1 + 0.25, 0, 1);
    hlb.hilbert_do(spl0);
    // process "real" and "imag" attributes from hlb object
    mod1 = hlb.real * sin(2 * $pi * ph1);
    mod2 = hlb.imag * sin(2 * $pi * ph2); 

-------------------------------------------------

-> La librairie CookDSP - traitement dans le domaine spectral <-
================================================================

Deux environnements de traitement dans le domaine spectral sont  
disponibles dans la librairie.

^
*FFT* : Pour manipuler l'énergie par tranche de fréquence

^
*Phase Vocoder* : Pour les manipulations où la cohérence de phase
est importante.

^
Structure d'un processus d'analyse-resynthèse:

-> analyse ==> manipulation du data ==> resynthèse <-

-> *fftin* ==> *fftin.real*, *fftin.imag* ==> *fftout* <-

-------------------------------------------------

-> La librairie CookDSP - traitement dans le domaine spectral <-
================================================================

Aspects importants du traitement dans le domaine spectral:

^
\- Synchroniser l'analyse et la resynthèse ( attribut *fftin.count* )

    @sample
    fin.fftin_do(spl0);
    spl0 = fout.fftout_get_output(fin.count);

^
\- Manipuler le data uniquement lorsqu'un bloc d'analyse est prêt 
( attribut *fftin.ready* )

    @sample
    fin.ready ? (
        // process fin.real and fin.imag
        fout.fftout_do(newreal, newimag);
    );

-------------------------------------------------

-> La librairie CookDSP - pv-transpose - préparation du processus <-
====================================================================

    desc: Phase Vocoder Mono Transposer
    //
    import cookdsp.jsfx-inc
    //
    slider1:2<0,5,1{256,512,1024,2048,4096,8192}>PV Size
    slider2:1<0,2,1{2,4,8}>Overlaps
    slider3:1<0.5,2>Transposition Factor
    //
    @init
    pin.pvin(1024, 4);      // analysis
    pout.pvout(1024, 4);    // synthesis
    magn = memalloc(512);   // process magnitude buffer
    freq = memalloc(512);   // process true freq buffer

-------------------------------------------------

-> La librairie CookDSP - pv-transpose - gestion des paramètres <-
==================================================================

    @slider
    size = pow(2, slider1 + 8);
    olaps = pow(2, slider2 + 1);
    //
    // If size or overlaps changed
    size != pin.size || olaps != pin.olaps ? (
        // re-initialize PVs
        pin.pvin_resize(size, olaps);
        pout.pvout_resize(size, olaps);
        // re-initialize process memories
        magn = memalloc(size/2);
        freq = memalloc(size/2);
    );

-------------------------------------------------

-> La librairie CookDSP - pv-transpose - manipulation du data <-
================================================================

    @sample
    pin.pvin_do((spl0 + spl1) * 0.707);
    spl0 = spl1 = pout.pvout_get_output(pin.count);
    pin.ready ? (
        memset(magn, 0, size/2); memset(freq, 0, size/2);
        k = 0;
        while (k < size/2) (
            index = floor(k * slider3);
            index < size/2 ? (
                magn[index] += pin.magn[k];
                freq[index] = pin.freq[k] * slider3;
            ); 
            k += 1;
        ); 
        pout.pvout_do(magn, freq);
    );

-------------------------------------------------

-> La librairie CookDSP - création d'instruments MIDI <-
========================================================

La librairie, au moment d'écrire ces lignes, offre trois objets  
pour la gestion du MIDI (plus à venir!).

^
*notein* : Gère la réception des _noteon_ et des _noteoff_.

^
*masr* : Enveloppe _attack_ - _sustain_ - _release_ activée par la vélocité.

^
*poly* : Outil de gestion de la polyphonie MIDI.

^
_______________________________________________________________________ 

Afin de ne pas surcharger le CPU, il est fortement recommandé  
d'effectuer la gestion des notes MIDI dans la section de code *@block*.

-------------------------------------------------

-> La librairie CookDSP - création d'instruments MIDI <-
========================================================

L'objet *notein* retourne "true" s'il reste encore des évènements à  
traiter dans la pile d'événements MIDI. Il est d'usage de placer  
cet objet dans une boucle *while* afin de ne pas manquer de notes. 

    @block
    // Until all midi events have been processed
    while (n.notein()) (
        // "n" holds a MIDI event
    );

^
Si une note a été détectée, l'attribut *ok* vaut "true". Les attributs  
*channel*, *pitch* et *velocity* contiennent alors le data de la note midi.

        n.ok ? ( // If midi event is a midi note
            // process n.channel, n.pitch and n.velocity
        );

-------------------------------------------------

-> La librairie CookDSP - mono-synth - préparation du processus <-
==================================================================

    desc:Simple Midi Synth
    //
    import cookdsp.jsfx-inc
    //
    @init
    // Initialize variables
    amp = midinote = 0;
    // Initialize the envelope
    env.masr(0.01, 1);
    // Initialize a square wave
    buf.buffer(1024);
    buf.buffer_square(20);
    // Initialize readers
    ph1.phasor(0, 0);
    ph2.phasor(0, 0);

-------------------------------------------------

-> La librairie CookDSP - mono-synth - réception des notes midi <-
==================================================================

    @block
    // Until all midi events have been processed
    while (n.notein()) (
        // If midi event is a midi note
        n.ok ? (
            n.velocity > 0 ? ( /* noteon */ 
                midinote = n.pitch;
                ph1.phasor_set_freq(mtof(midinote));
                ph2.phasor_set_freq(mtof(midinote) * 1.01);
                amp = n.velocity / 127;
            ) : ( /* noteoff */
                n.pitch == midinote ? amp = 0;
            );
        );
    );

-------------------------------------------------

-> La librairie CookDSP - mono-synth - génération de la synthèse <-
===================================================================

    @sample
    //
    // Compute the envelope
    gain = env.masr_do(amp);
    //
    // Read the square wave
    spl0 = buf.buffer_fnread3(ph1.phasor_do());
    spl1 = buf.buffer_fnread3(ph2.phasor_do());
    //
    // Apply gain envelope
    spl0 *= gain;
    spl1 *= gain;

-------------------------------------------------

-> Suggestions de projets <-
============================

^
- Délai stéréo avec récursion croisée

^
- Processus contrôlée par un suivi de hauteur

^
- Développer un son de synthétiseur MIDI original

^
- Explorer les fonctions de transfert avec l'objet *buffer*

^
- Traitement dans le domaine spectral

^
- Explorer les effets multiples (en série et/ou en parallèle)

