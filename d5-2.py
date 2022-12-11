

with open('inputs/d5-1.txt') as file:
    # Get the information from the first line
    first_line = file.readline()
    num_stacks = len(first_line) // 4

    # list of lists for the stacks
    stacks = [ 
        [] for _ in range(num_stacks)
    ]
    # First line processing
    for i in range(num_stacks):
        crate = first_line[4*i:4*i+4].strip()
        if crate:
            stacks[i].insert(0,crate)
        
    # Read the rest
    for line in file:
        if line.startswith('move'):
            parsed_line = line.split(' ')
            num_blocks = int(parsed_line[1])
            source_stack = int(parsed_line[3])-1
            dest_stack = int(parsed_line[5])-1

            # get num blocks from end of stack


            stacks[dest_stack].extend(stacks[source_stack][-1*num_blocks:])

            # remove from source stack
            del stacks[source_stack][-1*num_blocks:]

        else:
            # ignore the blank line before moves
            if line.strip() is False:
                continue
            # ignore the stack label line
            if line.replace(" ","").strip().isalnum():
                continue
        #elif line.endswith(']\n'): # very hacky, what if no crates in the last stack?
            for i in range(num_stacks):
                crate = line[4*i:4*i+4].strip()
                if crate:
                    stacks[i].insert(0,crate)

# get result string
result = ''
for stack in stacks:
    result += stack[-1][1]
print(result)