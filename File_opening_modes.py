# -*- coding: utf-8 -*-
from pprint import pprint
file_name = 'File_opening_modes.txt'
file = open(file_name, mode='w')  # mode (режим): запись
file_content = chr(35) + '''-*- coding: utf-8 -*-
My soul is dark - Oh! quickly string
The harp I yet can brook to hear;
And let thy gentle fingers fling
Its melting murmurs o'er mine ear.
If in this heart a hope be dear,
That sound shall charm it forth again:
If in these eyes there lurk a tear,
'Twill flow, and cease to burn my brain.

But bid the strain be wild and deep,
Nor let thy notes of joy be first:
I tell thee, minstrel, I must weep,
Or else this heavy heart will burst;
For it hath been by sorrow nursed,
And ached in sleepless silence, long;
And now 'tis doomed to know the worst,
And break at once - or yield to song.'''
# ---------------------------------------
file.write(file_content)
file.close()
print(f'------- {file_name} content -------')
print(file_content)