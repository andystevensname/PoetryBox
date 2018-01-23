# Poetry Box

Poetry Box prints poems on demand. Running on a Raspberry Pi, Poetry Box scrapes poems from the Poetry Foundation website with a Python script and stores them in MongoDB. When the user pushes the glowing white button, Poetry Box prints these poems with a Epson POS thermal reciept printer. To make the poems printer friendly Poem Box uses PhantomJS to produce a .png file of the poem.