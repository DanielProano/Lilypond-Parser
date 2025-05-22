\version "2.22.1"

voiceone =
\relative  cis'{
   r16   cis[  dis eis]    fis[  dis eis cis]   gis'8[  cis bis^\prall  cis]              | % 1
    dis16[  gis, ais bis]   cis[  ais bis gis]   dis'8[  gis fis^\prall  gis]               | % 2
    eis16[  ais gis fis]   eis[  gis fis ais]   gis[  fis eis dis]   cis[  eis dis fis]              | % 3
    eis[  dis cis bis]   ais[  cis bis dis]   cis[  bis ais gis]   g[  ais gis bis]              | % 4
    ais8[  dis,]   cis'8.[^\mordent  dis16]   bis[  ais gis g]   eis[  gis g ais]    | % 5
    gis[  bis ais cis]   bis[  dis cis eis]   dis[  bis32  cis dis16  gis]   bis,8[^\prall  ais16  gis] | % 6
    gis8 r r4 r16   gis[  ais bis]   cis[  ais bis gis]                           | % 7
    g8^\prall r r4 r16   ais[  bis cis]   dis[  bis cis ais]                  | % 8
    bis8          r r4 r16   dis[  cis bis]   ais[  cis bis dis]                  | % 9
    cis8          r r4 r16   eis[  dis cis]   bis[  dis d eis]                | % 10
    dis8[  d dis eis]   fis[  ais, bis! d]                               | % 11
    dis[  g, a ais]   bis[  cis]  dis4 ~                                | % 12
    dis16[  eis, g a]   ais[  g a eis]   eis'[  dis cis eis]   dis[  cis bis dis]    | % 13
    cis[  ais' a bis]   ais[  eis fis dis]   a,[  fis' eis dis]   cis8[  bis16  ais]        | % 14
    ais16[  ais' gis fis]   eis[  gis fis ais]  gis2 ~                              | % 15
    gis16[  eis fis gis]    ais[  fis gis eis]  fis2 ~                              | % 16
    fis16[  gis fis eis]    dis[  fis eis gis]  fis2 ~                              | % 17
    fis16[  dis eis fis]    gis[  eis fis dis]  eis2 ~                              | % 18
    eis16[  cis dis eis]   fis[  dis eis cis]   dis[  eis fis gis]   ais[  fis gis eis]              | % 19
    fis[    gis ais bis]   cis[  ais bis gis]   cis8[  gis]   eis[  dis16  cis]                 | % 20
    cis[  b ais gis]   fis[  ais gis b]   ais[  bis cis eis,]   dis[  cis' fis, bis]         | % 21
   < cis gis eis>1^\fermata\arpeggio                                | % 22
   \bar "|."
}

voicetwo =
\relative  cis{
   \clef "bass"
   r2          r16    cis[  dis eis]   fis[  dis eis cis]                      | % 1
    gis'8[  gis,] r4 r16   gis'[  ais bis]   cis[  ais bis gis]                      | % 2
    cis8[  bis cis dis]   eis[  gis, ais bis]                                    | % 3
    cis[  eis, g gis]   ais[  bis]  cis4 ~                                  | % 4
    cis16[  dis, eis g]   gis[  eis g dis]   gis8[  bis, cis dis]                  | % 5
    eis[  g gis eis]   bis8.[  cis16]   dis8[  dis,]                           | % 6
   r16   gis[  ais bis]   cis[  ais bis gis]   dis'8[  gis g gis]                    | % 7
    ais16[  dis, eis g]   gis[  eis g dis]   ais'8[  dis cis dis]                  | % 8
    gis,16[ \clef "treble"  gis' fis eis]   dis[  fis eis gis]   fis8[  eis fis dis]       | % 9
    eis16[  ais gis fis]   eis[  gis fis ais]   gis8[  fis gis eis]                        | % 10
    fis16[  b ais gis]   fis[  ais gis b]   ais[  gis fis eis]   dis[  fis eis gis]          | % 11
    fis[  eis dis cis]   bis[  dis cis eis]   dis[  cis bis ais]   a[  bis ais cis]              | % 12
   \clef "bass"
    bis8[  eis,]   dis'8.[^\mordent  eis16]   cis[  bis ais gis!]   g[  ais a bis]   | % 13
    ais[  cis bis dis]   cis[  eis dis fis]   eis8[  ais, eis' eis,]                       | % 14
    ais8[  ais,] r4 r16   eis''16[  dis cis]   bis[  dis d eis]                  | % 15
    dis2 ~   dis16[  ais bis cis]     dis[  bis cis ais]                            | % 16
    bis2 ~   bis16[  dis cis bis]     ais[  cis bis dis]                            | % 17
    cis2 ~   cis16[  gis ais b]   cis[  ais b gis]                          | % 18
    ais8[  b ais gis]   fis[  dis' cis b]                                | % 19
    ais[  fis' eis dis]     eis16[  dis, eis fis]   gis[  eis fis dis]                     | % 20
    eis8[  cis dis eis]   fis16[  dis eis fis]   gis8[  gis,]                          | % 21
   < cis cis,>1\_\fermata                                 | % 22
   \bar "|."
}

\score {
   \context PianoStaff <<
      \set PianoStaff.connectArpeggios = ##t
      \context Staff = "one" << \voiceone >>
      \context Staff = "two" << \voicetwo >>
   >>
   
   \layout { }
   
  \midi {
    \context {
      \Score
      tempoWholesPerMinute = #(ly:make-moment 80 4)
      }
    }
}
