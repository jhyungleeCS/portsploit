# PortSploit

**PortSploit** is a one-stop show web application reconnaissance tool that allows users to input an organization and receive information about accessible IPs and open ports, pairing that with a known vulnerabilities database.


## Description: 
Investigating different devices and vulnerabilities across the internet can result in cross-referencing multiple sites to get the information one needs. 
PortSploit aims to consolidate this information and combine the power of multiple tools to make reconnaissance and vulnerability hunting straightforward. 
PortSploit will utilize the power of Shodan to pull information on organizations such as accessible IPs, open ports, and other metadata and present it to the user. 
PortSploit will combine this data from the Shodan API with a local database containing port vulnerability information from SpeedGuide.net. 
The result is a view that provides a user with information about an organization’s open ports and potential vulnerabilities, all from one search. 
PortSploit also conveniently provides IP address information next to vulnerable ports, further simplifying the reconnaissance process. 
With the results, the user is able to sort the table and search for specific keywords. 
Additionally, if there is an IP Address that the user is interested in, they are able to click on that specific IP Address to only see that IP Address from the associated organization. 
Overall, PortSploit makes host discovery and vulnerability hunting a fast, easy, and more convenient process allowing for professionals to spend more time exploiting and less time hunting.

Ports are endpoints used for communication in a network that allows data to be sent and recieved. 

Open ports are a risk to a network because this gives a potential access point for attackers to gain unauthorized access. 
Having open ports on a network can leave attackers to deploy an array of attacks including Port/Packet sniffing, a DoS (Denial of Service) attack, 
and even exploiting known vulnerabilities that the port has. 



shodan.io </br>
speedguide.net </br>

## How to run in your local machine: 

<li>Extract the PortSploit 1.0 zip </li>
<li>Open your IDE and install the following modules: </li>
  <br>
  <ul>Flask</ul>
  <ul>Shodan</ul>
  <ul>csv</ul>
  <ul>pandas</ul>
  <ul>os</ul>
<li>Move every file to your root app directory</li>
<li>Run PortSploit1.0.py</li>
<li>Access the GUI by clicking on the local machine link:5000 </li>
