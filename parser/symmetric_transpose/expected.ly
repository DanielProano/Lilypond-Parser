\version "2.22.1"

\relative c {
  \clef bass
  \key c \major
  \time 4/4

  % Inversion of: c4  c4  g4  g4  a4  a4  g2
  c4   c4   f4   f4   es4  es4  f2

  % Inversion of: f4  f4  e4  e4  d4  d4  c2
  g4   g4   gis4 gis4 ais4 ais4 c2

  % Inversion of: g4  g4  f4  f4  e4  e4  d2
  f4   f4   g4   g4   gis4 gis4 ais2

  % Repeat that line
  f4   f4   g4   g4   gis4 gis4 ais2

  % Inversion of first line again
  c4   c4   f4   f4   es4  es4  f2

  % Final cadence
  g4   g4   gis4 gis4 ais4 ais4 c2
}

