/*

Click file that will perform ICMP packet drop function

*/

define($IP 192.168.56.105);                   // defined IP variable
define($MAC 00:00:00:00:01:00);				  // defined the mac address of the ovs bridge	

source :: FromDevice;                         // source name is mapped to packets coming from device
dest :: ToDevice;						      // dest is the destination

c :: Classifier(
    12/0806 20/0001,   //This is to match ARP requests
    12/0800,           //This is to match IP packets
    );               

Arp :: ARPResponse($IP $MAC);                   // made use of the ARPResponse element which check for the ARP response of the packet 
source -> c;									// source packets go to c (the classifier)

c[0] -> ARPPrint -> Arp -> dest; 				// ARP requests go to ARPPrint which again goes to the destination

c[1] -> CheckIPHeader(14) -> ICMPPingResponder() -> Print(‘Packet Discarded’) -> Discard; 
   
   // check if its an ICMP message by checking its protocol type protocol no of ICMP is 1, discard all ICMP packets and print "Packet discarded"
   

