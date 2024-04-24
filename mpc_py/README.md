## structure of MPC folder

We will have a seperate file to deal with the communication between merge, server func and share\
These three class only need to work on **number**, not files\
Currently, we need sum(value[]), mult(A,y,B,a,c) for Server_func\
We need share(value,party_size) beaver_triple(party_size)for share\
We need merge(value[]) for merge\


# add

Use ADD as example, if user input age:20 and we have party size of three, then call share function: share(value,party_size) to get a list of three shares of 20\
Then after each party send their share, the server_func will compute the sum of all shares from other parties, parameter(value[]), and return the result\
Then the merge will calculate the final result from each users' result from their server_func, with paramter(value[])\

# multiply
For MULT, we use Beaver Triple, for example input P1_age:20 and P2_age:21 and we have party size of three\
The user will be ranked by their hostname and port, assume P1, P2, P3 in this case,P1 would be x and P2 would be y\
First P1 and P2 will send their share to the party, use share(20,3) and share(21,3) to get three share of 20 and 21\
//we know that the more efficient way is to use trusted third party to generate the Beaver Triple, we will use the communication server as the third party, which will be in the TCP communication(since server does not participate in the computation in the computation, can be view as trusted third party)\
first the server will call the share function to get the beaver triple(party_size), which returns a 2d array:[[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]], where a,b,c are the triples and a*b=c\
Then the server program will send each share to each client in the party, and call the server_func's function sum(value[x,-a]) to compute the [x-a] and [y-b]\
Then the result will be share to merge to compute A=x-a B=y-b\
Then we call the mult(A,y,B,a,c), to compute share of z for each party, formula:[z] =A[y]+(-B)[a]+[c]\ 
Then just merge everyone's [z] would get the z we want

