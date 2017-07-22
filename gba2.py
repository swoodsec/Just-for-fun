#!/usr/bin/python
# Title: GBA - Gollum's Buzzword Appraiser
#################################################################################################
# Description: This is a joke application that rates websites based upon the number and frequency
# of industry buzzwords on their homepage. No offense intended to any specific company and this
# is a personal (joke) project not tied to the opinion of any company or employer (of anyone).
#################################################################################################

# Important: ASCII art. Thanks to 'JRO' for the totally inaccurate but hilarious Gollum. 
# Seriously I think this is a Chupacabra. If it asked me what I had in my pocketses.. I'd run.
print "                             `-."
print "                -._ `. `-.`-. `-."
print "               _._ `-._`.   .--.  `."
print "            .-'   '-.  `-|\/    \|   `-.      Gollum's Buzzword Appraiser"
print "          .'         '-._\   (o)O) `-."
print "         /         /         _.--.\ '. `-. `-.   A Serious Application"
print "        /|    (    |  /  -. ( -._( -._ '. '."
print "       /  \    \-.__\ \_.-'`.`.__'.   `-, '. .'   For The Enterprise "
print "       |  /\    |  / \ \     `--')/  .-'.'.'"
print "   .._/  /  /  /  / / \ \          .' . .' .'"
print "  /  ___/  |  /   \ \  \ \__       '.'. . .    'What Next-Gen IOT Device"
print "  \  \___  \ (     \ \  `._ `.     .' . ' .' does it have in its pocketses???'"
print "   \ `-._\ (  `-.__ | \    )//   .'  .' .-'"
print "    \_-._\  \  `-._\)//    ""_.-' .-' .' .'"
print " jro  `-'    \ -._\ ""_..--''  .-' .'"
print "              \/    .' .-'.-'  .-' .-'"
print "                  .-'.' .'  .' .-'"

import requests 

# Proprietary algorithms based upon next-generation research mostly originating from deep, dark, and on occasion stank-web
buzzExploitive = ['threat feed', 'cybercrime', 'darknet', 'hacktivism', 'surface web', 'tradecraft', 'threat actor', 'adversary', 'kill chain', 'advanced persistent threat', 'APT', 'dark web', 'deep web', 'expert system']
buzzDescription = ['bleeding edge', 'bleeding-edge', 'cutting edge', 'cutting-edge', 'synergy', 'disruptive', 'data driven', 'data-driven', 'next-gen', 'next gen', 'next generation', 'next-generation', 'lightweight', 'real-time', 'realtime', 'advanced', 'cloud-based', 'cloud based', 'preemptive', 'proactive', 'security stack', 'SME', 'single pane of glass', 'drill down', 'pivot', 'cyber fusion center', 'cyber fusion centre', 'trampolining']
buzzTrend = ['data science', 'data-science', 'machine learning', 'machine-learning', 'IOT', 'Internet of Things', 'internet-of-things', 'neural network', 'neural-network', 'agile', 'big data', 'BYOD', 'Bring Your Own Device', 'data mining', 'data-mining', 'devops', 'microservices', 'containerized', 'artificial intelligence', 'artificial-intelligence', 'threat intelligence', 'data lake']
buzzBorderline = ['analytics', 'algorithm', 'cloud', 'cyber', 'visualization', 'contextual', 'clustering', 'rest api', 'SDN', 'webinar', 'heap']

# User inputs website
site = raw_input("Please enter the vendor's URL (format:http://www.coolvender.com):")

# Main function that downloads and evaluates site
def siteDownload(site):
    try:
        response = requests.get(site)
        content = response.text
    except:
    	print "ERROR: Please try again. "
    
    # Total counter for all buzzwords
    nextGenTotal = 0
    # Trendy buzzwords can indicate how much thought leadership your vendor shows
    trendTotal = 0
    # Exploitive buzzwords essentially mean your vendor is high speed low drag fragging space hackers in cyberspace
    exploitTotal = 0
    # Buzzy descriptions indicate how much money the vendor spent on bleeding-edge expert marketing masterminds. 
    descTotal = 0 
    
    for i in range(len(buzzExploitive)):
    	total = content.count(buzzExploitive[i])
    	if total > 0:
            print buzzExploitive[i] + " appears " + str(total) + " times."
            nextGenTotal = total + nextGenTotal
            exploitTotal = total + exploitTotal

    for i in range(len(buzzDescription)):
    	total = content.count(buzzDescription[i])
    	if total > 0:
            print buzzDescription[i] + " appears " + str(total) + " times."
            nextGenTotal = total + nextGenTotal
            descTotal = total + descTotal

    for i in range(len(buzzTrend)):
    	total = content.count(buzzTrend[i])
    	if total > 0:
            print buzzTrend[i] + " appears " + str(total) + " times."
            nextGenTotal = total + nextGenTotal
            trendTotal = total + trendTotal

    for i in range(len(buzzBorderline)):
    	total = content.count(buzzBorderline[i])
    	if total > 0:
            print buzzBorderline[i] + " appears " + str(total) + " times."
            nextGenTotal = total + nextGenTotal

    print "======================================================="
    print "Exploitive Buzzwords: " + str(exploitTotal)
    if exploitTotal > 5:
        print "  _   ______             ____            "
        print " /_| /__)/    /|/| /  //  /  //__///  /  "
        print "(  |/   (    /   |(__/(__(  (/  )((__(__ "
    print "Trendy Buzzwords: " + str(trendTotal)
    if trendTotal > 5:
        print "  __  __   _   ___ ___ ___    ___  _   _  _   ___  "
        print " |  \/  | /_\ / __|_ _/ __|  / _ \| | | |/_\ |   \ "
        print " | |\/| |/ _ \ (_ || | (__  | (_) | |_| / _ \| |) |"
        print " |_|  |_/_/ \_\___|___\___|  \__\_\____/_/ \_\___/ "                                              
    print "Descriptive Buzzwords: " + str(descTotal)
                                  
    if nextGenTotal > 15:
        print "======================================================="
        print "Your vendor had a total of " + str(nextGenTotal) + " buzzwords!"
        print "======================================================="
        print "           )          (              )    *            )  " 
        print "   (    ( /(   (      )\ )     (  ( /(  (  `     (  ( /(  " 
        print "   )\   )\())( )\ (  (()/(     )\ )\()) )\))(  ( )\ )\()) "
        print " (((_) ((_)\ )((_))\  /(_))  (((_|(_)\ ((_)()\ )((_|(_)\  " 
        print " )\_____ ((_|(_)_((_)(_))    )\___ ((_)(_()((_|(_)_  ((_) "
        print "((/ __\ \ / /| _ ) __| _ \  ((/ __/ _ \|  \/  || _ )/ _ \ "
        print " | (__ \ V / | _ \ _||   /   | (_| (_) | |\/| || _ \ (_) |" 
        print "  \___| |_|  |___/___|_|_\    \___\___/|_|  |_||___/\___/ " 
    else:
        print "======================================================="
        print "Your vendor only had " + str(nextGenTotal) + " buzzwords"
        print "======================================================="
        print "              Do you even buzzword bro?                "
           



siteDownload(site)


