# Webscraping a list of all reptile species native to Australia

### TLDR 
csv file of all reptiles species native to Australia can be found at [aus_native_reptiles.csv](aus_native_reptiles.csv)


### Goal: 
Compile a list of reptiles species native to Australia using the help of webscraping. 

### Process:
I used the Reptile-database advanced search (http://reptile-database.reptarium.cz/advanced_search) to perform two searches (in [Python](webscrape_aussie_natives_from_reptile-database.py)):
1. The first search specifies the distribution category as "Australia". This yields a list of all species who inhabit Australia (native and non-native).
2. The second search specifies the distribution category as "Australia -introduced". This yields a list of all species who inhabit Australia but have not been introduced to Austrlia nor introduced elsewhere in the world.

The species found in search 1 but not in search 2 can be either non-native to Australia OR native to Austrlia but non-native elsewhere.
Therefore the next step was to manually search through each of species found in search 1 but not in search to categorize them as native or non-native to Australia (n = 9).
After removing the non-native species from list 1, the resulting list is all reptile species native to Australia. 


### Thoughts
I suspect this method can be used to compile a list of species native to other locations. It may also be possible for other taxa depending on how their databse is set up. 
