# MPC Folder Structure

## General Information

1. Three key MPC classes: merge, server_func, and share.
2. file_solve.py is responsible for bridging these three classes.
3. Our MPC classes only work with **numbers**, not files.

## connect_to_peer.py

**This class is in charge of:**
1. Connecting and listening to peers.
2. Sending shares to peers.
3. Receiving shares from peers.

**Example, for a case where there are 3 people in a party:**
1. The server will open 4 threads.
2. 2 threads are for listening to the other two.
3. 2 threads are for sending to the other 2.

**Function Specifications:**
1. Init: Retrieve client information (address, IP), keeps track of connected clients, starts the send and receive methods.
2. Receive: Allows acception of incoming connections, keeps track of current clients, and starts new communication threads.
3. Handle: Receives client data, and writes data. 
4. Send: Send file(s) and it's content to selected peer.
5. Send Merge: Send merged files to all peers for final result.
6. Receive Merge: Receive merged files from all peers for other class to read and compute final result

## file_solve.py

**This module contains functions that are in charge of:**
1. Integrating the three MPC programs: merge, serve_func, and share.
2. Handling and bridging files from three different folders.
3. Initiliazing computations needed for our statistical results. 

**Streamline:**
1. Function calls 'share' to retrieve the share of a value.
2. Call a function from 'server_func' to compute the specified statistic.
3. Call the function from 'merge' to merge the results of all three servers.

## merge.py

**This module contains functions that are in charge of:**
1. Retrieving the relevant computed results of all parties.
2. Merging the computed results to produce a statistical output that includes the values of all parties.

## server_func.py

**This module contains functions that are in charge of:**
1. Calculating statistical data (add, average, max, and min).
2. Sending a party member's result to the 'share_to_send' folder.

Note: Can be used for individual party member calculations, but also reused for parties calculations.

## share.py

TODO

server_func TODO:
- sum(value[])
- mult(A,y,B,a,c)

share TODO:
- share(value,party_size)

- beaver_triple(party_size)

merge TODO:
- merge(value[])

# Additional Information

## ADD example

1. User input: 'age:20', Party size: 3
2. Share function **'share(value,party_size)'** will retrieve three shares of 20.
3. After each party sends their share 'server_func' will compute the sum of all shares from other parties, **'parameter(value[])'**, and return the result.
4. 'merge' will then calculate the final result from each user's result from their server_func, **'parameter(value[])'**.

## MULT example

Note: We use Beaver Triples for MULT.

1. User inputs: 'P1_age:20' and 'P2_age:21', Party size: 3
2. Users will be ranked by their hostname and port. Assuming the party consists of P1, P2, and P3, P1 would be x and P2 would be y.
3. P1 and P2 send their shares to the party, **share(20,3)** and **share(21,3)** to get three shares of 20 and 21.
4. The server calls the share function to get the beaver triple(party_size), which returns a **2d array:[[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]], where a,b,c are the triples and a*b=c**
5. The server then sends each share to each client in the party and calls server_func's function **sum(value[x,-a]) to compute the [x-a] and [y-b]**
6. The result is sent to 'merge' to compute A=x-a, B=y-b
7. mult(A,y,B,a,c) is called to compute the share of z for each party **(formula:[z] =A[y]+(-B)[a]+[c])**
8. Everyone's [z] is then merged to output the final result.

Disclaimer: A more efficient way to execute this is to use a trusted third party to generate the Beaver Triple. For our program, we are using a communication server as the third party. This server utilizes TCP communication and is considered a trusted third party as it does not participate in the actual data computations.

## DC-net: A possible solution for MAX 

We know that DC-net would work if anyone paid (values equal to 1) but it wouldn't be able to handle collisions easily. 

First, we turn each desired value to compute into binary. Then, we could try to have a third party server decide a partition of range of bits for each party member. Ideally, each party member would only know their own range and not the others.

For example, each party member could get three lines and they can put their result in one of these lines. Then, we'll run DC-net between each party member, which returns a list of Party_size*3. The largest binary number would be the MAX. 

If we want further privacy, we could run DC-net on each bit, and if a client finds that the current largest number prefix is already larger than its number, it can stop sending.