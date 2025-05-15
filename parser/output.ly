\version "2.11.46"

voiceone =
\relative d'{
   r16  d[ ef]   g[ efd]  a'8[ dc'^\prall d]              | % 1
   e16[ a,bc']  d[ bc'a]  e'8[ ag^\prall a]               | % 2
   f16[ bag]  f[ agb]  a[ gfe]  d[ feg]              | % 3
   f[ edc']  b[ dc'e]  d[ c'ba]  gis[ bac']              | % 4
   b8[ e,]  d'8.[^\mordent e16]  c'[ bagis]  f[ agisb]    | % 5
   a[ c'bd]  c'[ edf]  e[ c'32 de16 a]  c8[^\prall b16 a] | % 6
   a8 r r4 r16  a[ bc']  d[ bc'a]                           | % 7
   gis8^\prall r r4 r16  b[ c'd]  e[ c'db]                  | % 8
   c'8          r r4 r16  e[ dc']  b[ dc'e]                  | % 9
   d8          r r4 r16  f[ ed]  c'[ edisf]                | % 10
   e8[ disef]  g[ b,c'!dis]                               | % 11
   e[ gis,aisb]  c'[ d] e4 ~                                | % 12
   e16[ f,gisais]  b[ gisaisf]  f'[ edf]  e[ dc'e]    | % 13
   d[ b'aisc']  b[ fge]  ais,[ g'fe]  d8[ c'16 b]        | % 14
   b16[ b'ag]  f[ agb] a2 ~                              | % 15
   a16[ fga]   b[ gaf] g2 ~                              | % 16
   g16[ agf]   e[ gfa] g2 ~                              | % 17
   g16[ efg]   a[ fge] f2 ~                              | % 18
   f16[ def]  g[ efd]  e[ fga]  b[ gaf]              | % 19
   g[   abc']  d[ bc'a]  d8[ a]  f[ e16 d]                 | % 20
   d[ ces'ba]  g[ baces']  b[ c'df,]  e[ d'g,c']         | % 21
   <daf>1^\fermata\arpeggio                                | % 22
   \bar "|."
}

voicetwo =
\relative d{
   \clef "bass"
   r2          r16   d[ ef]  g[ efd]                      | % 1
   a'8[ a,] r4 r16  a'[ bc']  d[ bc'a]                      | % 2
   d8[ c'de]  f[ a,bc']                                    | % 3
   d[ f,gisa]  b[ c'] d4 ~                                  | % 4
   d16[ e,fgis]  a[ fgise]  a8[ cde]                  | % 5
   f[ gisaf]  c'8.[ d16]  e8[ e,]                           | % 6
   r16  a[ bc']  d[ bc'a]  e'8[ agisa]                    | % 7
   b16[ e,fgis]  a[ fgise]  b'8[ ede]                  | % 8
   a,16[ \clef "treble" a'gf]  e[ gfa]  g8[ fge]       | % 9
   f16[ bag]  f[ agb]  a8[ gaf]                        | % 10
   g16[ ces'ba]  g[ baces']  b[ agf]  e[ gfa]          | % 11
   g[ fed]  c'[ edf]  e[ dc'b]  ais[ c'bd]              | % 12
   \clef "bass"
   c'8[ f,]  e'8.[^\mordent f16]  d[ c'ba!]  gis[ baisc']   | % 13
   b[ dc'e]  d[ feg]  f8[ b,f'f,]                       | % 14
   b8[ b,] r4 r16  f''16[ ed]  c'[ edisf]                  | % 15
   e2 ~  e16[ bc'd]    e[ c'db]                            | % 16
   c'2 ~  c'16[ edc']    b[ dc'e]                            | % 17
   d2 ~  d16[ abces']  d[ bces'a]                          | % 18
   b8[ ces'ba]  g[ e'dces']                                | % 19
   b[ g'fe]    f16[ e,fg]  a[ fge]                     | % 20
   f8[ def]  g16[ efg]  a8[ a,]                          | % 21
   <dd,>1\_\fermata                                 | % 22
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
