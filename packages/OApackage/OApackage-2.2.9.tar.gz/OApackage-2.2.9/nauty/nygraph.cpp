// nygraph.cpp
// a C++ wrapper for nauty graphs


#include <nygraph.hpp>
//#include <naugroup.h>
//#include <gtools.h>
#include <vector>
#include <string>
#include <cstdio>



extern "C" {
  
 void testx() {
// allocate
DYNALLSTAT(graph,g,g_sz);
DYNALLSTAT(int,lab,lab_sz);
DYNALLSTAT(int,ptn,ptn_sz);
DYNALLSTAT(int,orbits,orbits_sz);
static DEFAULTOPTIONS_GRAPH(options);
statsblk stats;
int n,m,v;
set *gv;
/* Default options are set by the DEFAULTOPTIONS_GRAPH macro above.
Here we change those options that we want to be different from the
defaults. writeautoms=TRUE causes automorphisms to be written. */
options.writeautoms = TRUE;


/* The following optional call verifies that we are linking
to compatible versions of the nauty routines. */
nauty_check(WORDSIZE,m,n,NAUTYVERSIONID);
/* Now that we know how big the graph will be, we allocate
* space for the graph and the other arrays we need. */
DYNALLOC2(graph,g,g_sz,m,n,"malloc");
DYNALLOC1(int,lab,lab_sz,n,"malloc");
DYNALLOC1(int,ptn,ptn_sz,n,"malloc");
DYNALLOC1(int,orbits,orbits_sz,n,"malloc");
EMPTYGRAPH(g,m,n);
for (v = 0; v < n; ++v) ADDONEEDGE(g,v,(v+1)%n,m);
printf("Generators for Aut(C[%d]):\n",n);
densenauty(g,lab,ptn,orbits,&options,&stats,m,n,NULL);
printf("order = ");
writegroupsize(stdout,stats.grpsize1,stats.grpsize2);
printf("\n");
}

}

