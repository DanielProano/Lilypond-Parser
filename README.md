![Kundalini_Software_Internship_Code]("https://github.com/user-attachments/assets/f495e052-d9e0-4003-a076-c21eb7c9cd30")

# Overview
This is the open source code I made for my internship with Kundalini Software. 

In this project, I made code that interacts with and interprets Lilypond.

The main application is read-in music and then apply a symmetrical inversion,

maintaining the pitch and reflecting the music into a different clef. This allows

piano players to practice ambidextrousity while playing tunes they are familiar with.


## Folder: C-Scale
In this folder, I created my first Lilypond code, experimenting with how to read and write .ly files.

In addition, I also discovered how to save the Lilypond code as a pdf. The main

funtion of this folder was to serve as a playground for experimenting with python ly

and Lilypond.


### Original

In this folder, I started to make the parsing code. I first experimented with 

reading in a Lilypond file programmatically. Before, I only transposed with

command-line. I first managed to read the file and rewrite its entirity to another file. 


### Advanced Transpose

I then began working on the code apply a transpose to all of notes within the file. 

I used python lys PitchIterator to parse and transpose the notes. I then experimented with 

the Simplifier function. I was able to create code the successfully wrote transposed notes

to an output file. 

However, there were a few bugs, including one where the pitches were printed but one octave

off its intended place. I tracked this bug to the simplify function but was unable to come up 

with a solution. So I briefly tried my hand at a custom simplify function but it quickly become

apparent that it just wasn't working.


### Symmetric Transpose

I began this code by trying to invert the D scale from the treble to bass clef.

My original code, parser.py, takes a pitch, converts it to the MIDI system,

inverts it around middle C, and writes the result to an output file. While this system

worked well, there are still problems with overly convoluted notes. For example, 

often times a note will inverted into Bisis, or Bbb, instead of A. While technically

correct, this is an overly complex system and should be simplified as much as possible

avoid confusion.


This lead me to developing "experimental.py". See python-ly natively handles a 12

equal temperament system, meaning that some notes overlap in their representation.

This means the computer often has to "guess" what the note should be and is

often wrong. In experimental.py, I convert the notes to a 31 TET system, where

every meaningful note is representated uniquely.
