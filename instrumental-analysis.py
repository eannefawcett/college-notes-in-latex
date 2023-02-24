# find a CSE accepted latex distribution for scientific notation
# find how to make subscripts in math/science related formulas

import os
import subprocess
data_path = 'C://Users/eannefawcett/Desktop/Data Science/Projects/data/college-notes-in-latex/'
project_path = 'C://Users/eannefawcett/Desktop/Data Science/Projects/college-notes-in-latex/'
report_path = project_path + 'reports/'

import numpy as np
from pylatex import Document, Command, Section, Subsection
from pylatex.utils import italic, bold, NoEscape

geometry_options = {"tmargin": "2.54cm", "bmargin": "2.54cm", \
                    "lmargin": "2.54cm", "rmargin": "2.54cm"}
doc = Document(geometry_options=geometry_options)

doc.preamble.append(Command('title','Instrumental Analysis'))
doc.preamble.append(Command('author','Beth Fawcett'))
doc.preamble.append(Command('date', NoEscape('Spring 2014')))
doc.append(NoEscape(r'\maketitle'))

with doc.create(Section('Direct Current')):
     with doc.create(Subsection('Charge')):
          doc.append('Can be positive or negative')
          doc.append('Depicted by the symbol "\mathrm{Q}"')
          doc.append('\nMeasured in Columbs where \electron{1} = 1.6e-19\mathrm{C}')
          doc.append('\nAll charges are multiples of the electron charge')
          doc.append("\n\tHowever, charge is often considered a continuous value \
                      for simplicity's sake")
          doc.append('\nConserved in a closed system')
     with doc.create(Subsection('Current')):
          doc.create('Flow of electrical charge')
          doc.create('\nI = \frac{d \mathrm{Q}} {d \mathrm{t}}')
          doc.create('\n\tWhere \mathrm{I} is current, \mathrm{Q} is charge, and \mathrm{t} is time')
          doc.create('\nDirection is conventionally flow of POSITIVE charge')
          doc.create('\nMeasure in Amps where \mathrm{A} = \frac{\mathrm{C}}{\mathrm{s}} = \SI{6.25e18}{\frac{\electron}{\mathrm{s}}}')
          doc.create('\nLower Power = 1-10 \mathrm{m}\mathrm{A}')
          doc.create('\nHigh Power = anything higher')
          doc.create('\n2 Types')
          doc.create('\n\tDirect Current')
          doc.create('\n\t\tDirection of charge flow is ALWAYS the same')
          doc.create('\n\t\tPulsating Direct Current has variable current magnitude')
          doc.create('\n\tAlternating Current')
          doc.create('\n\t\tDirection of charge flow is variable')
     with doc.create(Subsection('Voltage')):
          doc.create('Electric potential')
          doc.create('\n\t\mathrm{V} = \frac{\mathrm{W}}{\mathrm{Q}} = \frac{Potential Energy}{Charge} = \frac{Joules}{Columbs}')
          doc.create('\nGround is the point at which the energy of all charges is zero')
          doc.create('\nFlows from high to low')
     with doc.create(Subsection('Resistance')):
          doc.create('With flow comes resistance')
          doc.create('\n\t\mathrm{R} = (\frac{\mathrm{V2} - \mathrm{V1}}{\mathrm{I}}) = \Omega = \frac{Volts}{Amps}')
          doc.create('\nCurrent in must equal current out')
          doc.create('\nPassive circuits: if no energy is given to the charge, then the charge loses energy')
          doc.create('\n\t\frac{{(\mathrm{{V2}} - \mathrm{{V1}})}}{{\mathrm{R}}} and \mathrm{V2}\gtr\mathrm{V1}')
          doc.create('\n\tResistance is positive')
          doc.create('\nDependent on length')
          doc.create('\n\t\mathrm{R} = \rho * \frac{{\mathrm{l}}}{{\mathrm{A}}}')
          doc.create('\n\t\twhere \mathrm{R} is resistance, \rho is resistivity (ohm meters), \
                     \mathrm{l} is length, and \mathrm{A} is cross-sectional area')
          doc.create('\nResistivity: the difficulty that an electron has in moving through \
                      a material due to the collisions it experiences with the atoms \
                      in the material')
          doc.create('\n\tCan be temperature dependent')
          doc.create('\n\t\tIncreases 0.5% - 1% for a rise of 10C in carbon resistors')
          doc.create('\n\tDoes NOT depend on size or shape, but on material properties')
          doc.create('\n\tConductors have low resistivity')
          doc.create('\n\tInsulators have high resistivity')
          doc.create('\n\t\tBatteries have a negative resistance due to \
                            chemical energy contribution (\mathrm{V1} \gtr \mathrm{V2})')
          doc.create('\n\mathrm{R} = \frac{{d\mathrm{V}}}{{d\mathrm{I}}}')
          doc.create('\nResistors are a two terminal circuit element \
                        that has a consistent resistance')
          doc.create('\n\tColor code where \mathrm{R} = (1st)(2nd)*10^(3rd) \
                          and the (4th) is the tolerance')


### Conductance
### Ohm's Law
### Batteries
### Kirchoff's Laws
### Power
### Series
### Parallel

#8 Touch Points to Learn, 10,000 to become a master at the topic
## 1) pre-reading text book
## 2) Listening in lecture
## 3) Writing your notes from lecture
## 4) Looking at the powerpoint/chalkboard/whiteboard
## 5) After class to review notes
## 6) Working a practice problem
## 7) Rewriting notes in different
## 8) Compare your notes to a friend's
## 9) Go to tutoring/recitation

doc.generate_pdf('full', clean_tex=False)
subprocess.call(["latexmk, full.tex"])