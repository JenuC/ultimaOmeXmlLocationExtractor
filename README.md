# ultima Microscope Ome Xml Stage Location Extractor : UW-LOCI

-python script to extract location for Ultima Microscope OME-XML / tiff or env.

## root
* Sequence >> Frame >> PVStateShard >> PVStateValue
* Root PVScan
* * ['Sequence', 'SystemIDs', 'PVStateShard']
* * * ['Frame', 'PVStateShard']
* * * *['ExtraParameters', 'File', 'PVStateShard']
* * * * * ['PVStateValue'] >> key value +descp
* * * * * *['IndexedValues'] >> key value index +descp
* * * * * *['SubindexedValues'] >> key value index subindex +descp

## location 
  [('index', 'XAxis')] [('subindex', '0'), ('value', '-41468.71')]
  [('index', 'YAxis')] [('subindex', '0'), ('value', '7607.47')]
  [('index', 'ZAxis')] [('subindex', '0'), ('value', '2444.85')]
