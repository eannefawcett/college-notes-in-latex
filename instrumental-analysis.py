import numpy as np
from pylatex import Document, Section, Subsection, Tabular, \
    Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
from pylatex.utils import italic, bold

geometry_options = {"tmargin": "2.54cm", "bmargin": "2.54cm", \
                    "lmargin": "2.54cm", "rmargin": "2.54cm"}
doc = Document(geometry_options=geometry_options)

# Instrumental Analysis
## From Spring 2014

with doc.create(Section('Direct Current')):
     with doc.create(Subsection('Charge')):
          doc.append('Can be positive or negative')
          doc.append('\nMeasured in Columbs where \electron{1} = \SI{1.6e-19}{C}')
          doc.append('\nAll charges are multiples of the electron charge')
          doc.append("\n\tHowever, charge is often considered a continuous value \
                      for simplicity's sake")
          doc.append('\nConserved in a closed system')
     with doc.create(Subsection('Current')):
          doc.create('Flow of electrical charge')
          doc.create('\nI = \frac{dQ}{dt}')
          doc.create('\n\tWhere I is current, Q is charge, and t is time')
          doc.create('\nDirection is conventionally flow of POSITIVE charge')
          doc.create('\nMeasure in Amps where A = \frac{C}{s} = \SI{6.25e18}{\frac{\electron}{s}}')
          doc.create('\nLower Power = 1-10 mA')
          doc.create('\nHigh Power = anything higher')
          doc.create('\n2 Types')
          doc.create('\n\tDirect Current')
          doc.create('\n\t\tDirection of charge flow is ALWAYS the same')
          doc.create('\n\t\tPulsating Direct Current has variable current magnitude')
          doc.create('\n\tAlternating Current')
          doc.create('\n\t\tDirection of charge flow is variable')

### Charge
#- Can be positive or negative
#- Measured in Columbs
#- ``` ```
### Current
### Voltage
### Resistance
### Resistivity
### Conductance
### Ohm's Law
### Batteries
### Kirchoff's Laws
### Power
### Series
### Parallel

#doc.generate_pdf('full', clean_tex=False)