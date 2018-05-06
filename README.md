# Springer-dl
Python script that download all Articles in "https://link.springer.com/" Journal's Search 
|| This is just a beta version that ONLY Works within Journal's Search ||

## Installation
```
git clone https://github.com/MoatazFarid/springer-dl.git
```
The script use the following packages , so make sure u install them first
* requests
* BeautifulSoup
* DataFrame
* tqdm

## Usage
Open the springer-dl.py and edit the "LINK" var with your search link
```
##########ONLY CHANGE THE LINK ######
LINK="https://link.springer.com/search?query=malware&search-within=Journal&facet-journal-id=11416"
#################
```
save and close ,Run it
```
python springer-dl.py
```

