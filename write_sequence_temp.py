import manage as man

#write masterlist produced by SequenceTimestamp to the appropriate sequence 
#files
def CreateSequenceFile(min_node,tot,masterlist,stamp_ID):
    """ Write a list of sequenced timestamps to appropriately named files.
        Create a master sequence file.
            min_node -- the smallest node number, an integer
            tot -- the total number of nodes, an integer
            masterlist -- a list whose elements look like 
                [modified timestamp, disk number, node number, timestamp, 
                sequence number, duplicate string]
                Output of SequenceTimestamp
            stamp_ID -- a string used to uniquely identify a file
                    eg if the file name is timestamp.2013-07-25T01:30:00.1.dat,
                    the stamp_ID is '.2013-07-25T01:30:00'
    """
    n=min_node
    max_node = min_node + tot
    while n < max_node:
        name='node{0}/sequence{1}.mod.dat'.format(n,stamp_ID)
        master=[]
        for i in range(len(masterlist)):
            if masterlist[i][2] == n:
                point=[masterlist[i][4], masterlist[i][1]]
                master.append(point)
        man.WriteFileCols(master,name)
        n+=1
