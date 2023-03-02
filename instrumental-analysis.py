# find a CSE accepted latex distribution for scientific notation
# find how to make subscripts in math/science related formulas

import os
import subprocess
data_path = 'C://Users/eannefawcett/Desktop/Data Science/Projects/data/college-notes-in-latex/'
project_path = 'C://Users/eannefawcett/Desktop/Data Science/Projects/college-notes-in-latex/'
report_path = project_path + 'reports/'

import numpy as np
from pylatex import Document, Command, Section, Subsection, Itemize, Math
from pylatex.utils import italic, bold, NoEscape
import pylatex.quantities as pq

geometry_options = {"tmargin": "2.54cm", "bmargin": "2.54cm", \
                    "lmargin": "2.54cm", "rmargin": "2.54cm"}
doc = Document(geometry_options=geometry_options)

doc.preamble.append(Command('title','Instrumental Analysis'))
doc.preamble.append(Command('author','Beth Fawcett'))
doc.preamble.append(Command('date', NoEscape('Spring 2014')))
doc.append(NoEscape(r'\maketitle'))

with doc.create(Section('Direct Current')):
     with doc.create(Subsection('Charge')):
          with doc.create(Itemize()) as charge:
               charge.add_item('Can be positive or negative')
               charge.add_item('Depicted by the symbol "\mathrm{Q}"')
               charge.add_item('Measured in Columbs where \electron{1} = 1.6e-19\mathrm{C}')
               charge.add_item('All charges are multiples of the electron charge')
               charge.add_item("\tHowever, charge is often considered a continuous value \
                         for simplicity's sake")
               charge.add_item('Conserved in a closed system')
     with doc.create(Subsection('Current')):
          with doc.create(Itemize()) as current:
               current.add_item('Flow of electrical charge')
               current.add_item('I = \dfrac{d \mathrm{Q}} {d \mathrm{t}}')
               current.add_item('\tWhere \mathrm{I} is current, \mathrm{Q} is charge, and \mathrm{t} is time')
               current.add_item('Direction is conventionally flow of POSITIVE charge')
               current.add_item('Measure in Amps where \mathrm{A} = \dfrac{\mathrm{C}}{\mathrm{s}} = \SI{6.25e18}{\frac{\electron}{\mathrm{s}}}')
               current.add_item('Lower Power = 1-10 \mathrm{m}\mathrm{A}')
               current.add_item('High Power = anything higher')
               current.add_item('2 Types')
               current.add_item('\tDirect Current')
               current.add_item('\t\tDirection of charge flow is ALWAYS the same')
               current.add_item('\t\tPulsating Direct Current has variable current magnitude')
               current.add_item('\tAlternating Current')
               current.add_item('\t\tDirection of charge flow is variable')
     with doc.create(Subsection('Voltage')):
          with doc.create(Itemize()) as voltage:
               voltage.add_item('Electric potential')
               voltage.add_item('\t\mathrm{V} = \dfrac{\mathrm{W}}{\mathrm{Q}} = \frac{Potential Energy}{Charge} = \frac{Joules}{Columbs}')
               voltage.add_item('Ground is the point at which the energy of all charges is zero')
               voltage.add_item('Flows from high to low')
     with doc.create(Subsection('Resistance')):
          with doc.create(Itemize()) as resistance:
               resistance.add_item('With flow comes resistance')
               resistance.add_item('\t\mathrm{R} = (\dfrac{\mathrm{V2} - \mathrm{V1}}{\mathrm{I}}) = \Omega = \dfrac{Volts}{Amps}')
               resistance.add_item('Current in must equal current out')
               resistance.add_item('Passive circuits: if no energy is given to the charge, then the charge loses energy')
               resistance.add_item('\t\dfrac{{(\mathrm{{V2}} - \mathrm{{V1}})}}{{\mathrm{R}}} and \mathrm{V2}\gtr\mathrm{V1}')
               resistance.add_item('\tResistance is positive')
               resistance.add_item('Dependent on length')
               resistance.add_item('\t\mathrm{R} = \rho * \dfrac{{\mathrm{l}}}{{\mathrm{A}}}')
               resistance.add_item('\t\twhere \mathrm{R} is resistance, \rho is resistivity (ohm meters), \
                         \mathrm{l} is length, and \mathrm{A} is cross-sectional area')
               resistance.add_item('Resistivity: the difficulty that an electron has in moving through \
                         a material due to the collisions it experiences with the atoms \
                         in the material')
               resistance.add_item('\tCan be temperature dependent')
               resistance.add_item('\t\tIncreases 0.5% - 1% for a rise of 10C in carbon resistors')
               resistance.add_item('\tDoes NOT depend on size or shape, but on material properties')
               resistance.add_item('\tConductors have low resistivity')
               resistance.add_item('\tInsulators have high resistivity')
               resistance.add_item('\t\tBatteries have a negative resistance due to \
                              chemical energy contribution (\mathrm{V1} \gtr \mathrm{V2})')
               resistance.add_item('\mathrm{R} = \frac{{d\mathrm{V}}}{{d\mathrm{I}}}')
               resistance.add_item('Resistors are a two terminal circuit element \
                         that has a consistent resistance')
               resistance.add_item('\tColor code where \mathrm{R} = (1st)(2nd)*10^(3rd) \
                              and the (4th) is the tolerance')


### Conductance
### Ohm's Law
### Batteries
### Kirchoff's Laws
### Power
### Series
### Parallel

#8 Touch Points to Learn, 10,000 hours to become a master at the topic
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
#subprocess.call(["latexmk, full.tex"])