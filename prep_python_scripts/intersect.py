# Script for finding non-overlapping snips in PLEIO and MTAG results

with open("./output_pleio.txt") as pleio_file:
    with open('./output_mtag.txt') as mtag_file:
        pleio_set = ()
        mtag_set = ()
        line = pleio_file.readline()
        line = mtag_file.readline()
        for line in pleio_file:
            pleio_set.add(line.split()[0])
        for line in mtag_file:
            mtag_set.add(line.split()[0])
print(mtag_set.difference(pleio_set))