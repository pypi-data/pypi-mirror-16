/** \file oagraph.cpp

 C++ program: oagraph

 oagraph: tool for testing new algorithms

 Author: Pieter Eendebak <pieter.eendebak@gmail.com>, (C) 2015

 Copyright: See LICENSE.txt file that comes with this distribution
*/

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>

#include "arraytools.h"
#include "arrayproperties.h"
#include "anyoption.h"
#include "tools.h"
#include "extend.h"

#include "oadevelop.h"
#include "lmc.h"

#include <numeric>

namespace nauty
{
extern "C" {
//#include "nygraph.hpp"

//#include "nauty.h"


}

#include "nauty.h"

/* DYNALLSTAT declares a pointer variable (to hold an array when it
is allocated) and a size variable to remember how big the array is.
Nothing is allocated yet. */
DYNALLSTAT ( graph,g,g_sz );
DYNALLSTAT ( int,lab,lab_sz );
DYNALLSTAT ( int,ptn,ptn_sz );
DYNALLSTAT ( int,orbits,orbits_sz );
static DEFAULTOPTIONS_GRAPH ( options );
statsblk stats;
int n,m,v;
set *gv;

/* Default options are set by the DEFAULTOPTIONS_GRAPH macro above.
Here we change those options that we want to be different from the
defaults. writeautoms=TRUE causes automorphisms to be written. */
options.writeautoms = TRUE;
while ( 1 )
{
	printf ( "\nenter n : " );
	if ( scanf ( "%d",&n ) == 1 && n > 0 ) {
		/* The nauty parameter m is a value such that an array of
		m setwords is sufficient to hold n bits. The type setword
		is defined in nauty.h. The number of bits in a setword is
		WORDSIZE, which is 16, 32 or 64. Here we calculate
		m = ceiling(n/WORDSIZE). */
		m = SETWORDSNEEDED ( n );
		44/* The following optional call verifies that we are linking
to compatible versions of the nauty routines. */
		nauty_check ( WORDSIZE,m,n,NAUTYVERSIONID );
		/* Now that we know how big the graph will be, we allocate
		* space for the graph and the other arrays we need. */
		DYNALLOC2 ( graph,g,g_sz,m,n,"malloc" );
		DYNALLOC1 ( int,lab,lab_sz,n,"malloc" );
		DYNALLOC1 ( int,ptn,ptn_sz,n,"malloc" );
		DYNALLOC1 ( int,orbits,orbits_sz,n,"malloc" );
		EMPTYGRAPH ( g,m,n );
		for ( v = 0; v < n; ++v )
			ADDONEEDGE ( g,v, ( v+1 ) %n,m );
		printf ( "Generators for Aut(C[%d]):\n",n );
		densenauty ( g,lab,ptn,orbits,&options,&stats,m,n,NULL );
		printf ( "order = " );
		writegroupsize ( stdout,stats.grpsize1,stats.grpsize2 );
		printf ( "\n" );
	} else
		break;
}
exit ( 0 );

}

extern "C" {
//#include "nygraph.hpp"
//#include "nauty.h"
}
template<class NumType>
std::vector<NumType> cumsum ( const std::vector<NumType> x )
{
	// initialize the result vector
	std::vector<NumType> res ( x.size() );
	std::partial_sum ( x.begin(), x.end(), res.begin() );
	return res;
}

template<class NumType>
std::vector<NumType> cumsum0 ( const std::vector<NumType> x )
{
	// initialize the result vector
	std::vector<NumType> res ( x.size() +1 );
	res[0]=0;
	std::partial_sum ( x.begin(), x.end(), res.begin() +1 );
	return res;
}

/**  Convert orthogonal array to graph representation
 *
 *   The conversion method is as in Ryan and Bulutoglu.
 *   The resulting graph is bi-partite.
 *   The graph representation can be used for isomorphism testing.
*/
array_link array2graph ( const array_link &al, int verbose=1 )
{
	arraydata_t arrayclass = arraylink2arraydata ( al );
	int nrows = al.n_rows;
	int ncols = al.n_columns;
	const std::vector<int> s = arrayclass.getS();

	int nRowVertices = nrows;
	int nColumnLevelVertices = std::accumulate ( s.begin(), s.end(), 0 );
	int nColVertices = ncols;

	int nVertices = nrows + ncols + nColumnLevelVertices; // number of vertices in the graph
	int colOffset = nrows;

	std::vector<int> vertexOffsets ( s.size() +1 );

	std::vector<int> cs = cumsum0 ( s );

	for ( size_t j=0; j<s.size(); j++ )
		vertexOffsets[j] = colOffset + ncols + cs[j];

	std::vector<int> colors ( nVertices );

	// row vertices: color 0
	for ( int i=0; i<nrows; i++ )
		colors[i]=0;
	// column vertices: color 1
	for ( int i=0; i<ncols; i++ )
		colors[i+nrows]=1;
	// other vertices: color 2
	for ( int i=0; i<nColumnLevelVertices; i++ )
		colors[i+nrows+ncols]=2;


	nauty::NyGraph G ( nVertices ); // graph

//    im = np.zeros((nVertices, nVertices))  # incidence matrix


	for ( int r=0; r<nrows; r++ ) {
		for ( int c=0; c<ncols; c++ ) {
			int idx = al.at ( r, c ) + vertexOffsets[c];
			G.add_edge ( r, idx ); // should be color 1
		}
	}


	if ( nColVertices > 0 ) {
		int colidx = 2;
		for ( int col =0; col<ncols; col++ ) {
			for ( int sx=0; sx<s[col]; sx++ ) {
				int sel = vertexOffsets[col] + sx;
				G.add_edge ( colOffset+col, sel ) ; // = colidx;
			}
		}
	}

	/*
	# The non-row vertices do not have any connections to other non-row
	# vertices.

	xy = np.zeros((2, nrows + s.sum()))

	# calculate positions
	for row in range(0, nrows):
	    xy[:, row] = np.array([0, row])

	pos = nrows
	for col in range(0, ncols):
	    for ss in range(0, s[col]):
	        xy[:, pos] = np.array([2 + ss / s[col], col])
	        pos = pos + 1

	return im, colors, dict({'adata': adata, 'im': im, 'colors': colors, 'nVertices': nVertices})
	*/

	G.do_nauty ( true );
	std::string cstr  = G.canon_string();
	std::vector<int> p = G.canon_labeling;

	if ( verbose ) {
		printf ( "perm: " );
		display_vector ( p );
//	for(size_t i=0; i<p.size(); i++)
//		printf("%d: %d\n", i, p[i] );
		printf ( "\n" );
		display_vector ( G.ptn );
		//for(int i=0; i<p.size(); i++)
		printf ( "\n" );
	}
	//printf("canon string: %s\n", cstr.c_str() );


	return G;
}

int main ( int argc, char* argv[] )
{
	AnyOption opt;
	/* parse command line options */
	opt.setFlag ( "help", 'h' );   /* a flag (takes no argument), supporting long and short form */
	opt.setOption ( "output", 'o' );
	opt.setOption ( "rand", 'r' );
	opt.setOption ( "verbose", 'v' );
	opt.setOption ( "ii", 'i' );
	opt.setOption ( "dverbose", 'd' );
	opt.setOption ( "rows" );
	opt.setOption ( "cols" );
	opt.setOption ( "oaconfig", 'c' ); /* file that specifies the design */

	opt.addUsage ( "Orthonal Array: oatest: testing platform" );
	opt.addUsage ( "Usage: oatest [OPTIONS] [FILE]" );
	opt.addUsage ( "" );
	opt.addUsage ( " -h --help  			Prints this help " );
	opt.processCommandArgs ( argc, argv );


	int randvalseed = opt.getIntValue ( 'r', 1 );

	srand ( randvalseed );

	int verbose = opt.getIntValue ( 'v', 1 );

	print_copyright();
	setloglevel ( NORMAL );

	/* parse options */
	if ( opt.getFlag ( "help" ) || opt.getFlag ( 'h' ) || opt.getArgc() <0 ) {
		opt.printUsage();
		exit ( 0 );
	}

	setloglevel ( SYSTEM );

	// select a design
	array_link al = exampleArray ( 5 );

	nauty::testx();



	exit ( 0 );

	/*
	// convert design (with isomorphism type) to a colored graph
	nauty::NyGraph G = array2graph(al, 1);

	if (verbose)
	printf("creatd graph with %d vertices and ? edges\n", G.num_nodes );

	*/
	if ( verbose )
		printf ( "done\n" );
	return 0;

}

// kate: indent-mode cstyle; indent-width 4; replace-tabs off; tab-width 4; 
