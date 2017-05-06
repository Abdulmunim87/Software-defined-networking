'''
Swapnasheel Sonkamble
SIMPLE TOPOLOGY CREATION USING PYTHON SCRIPT

(h1,h2) ---> (s1)
               |----->(C0)
(h3,h4) ---> (s2)

'''


# Topology

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost1 = self.addHost( 'h1' )
        leftHost2 = self.addHost( 'h2' )
	rightHost1 = self.addHost( 'h3' )
	rightHost2 = self.addHost( 'h4' )
        leftSwitch = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )

        # Add links
        self.addLink( leftHost1, leftSwitch )
	self.addLink( leftHost2, leftSwitch )
	self.addLink( rightHost1, rightSwitch )
	self.addLink( rightHost2, rightSwitch )
        
        


topos = { 'mytopo': ( lambda: MyTopo() ) }


'''
To run custom topology in mininet, use
sudo mn --controller=remote,ip=<>,port=6653 --custom ~/PATH_OF_FILE/FILE_NAME.py --topo=mytopo --mac
'''

