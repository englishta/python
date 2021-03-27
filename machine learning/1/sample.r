install.packages( "quantmod" )
library( "quantmod" )
getSymbols( "DEXJPUS", src="FRED" )
DEXJPUS
plot( DEXJPUS )