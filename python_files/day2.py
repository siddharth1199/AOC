import pandas as pd
df = pd.read_csv('../inputs/day2.txt', sep='x', names=['len', 'wid', 'hei'])

# Part 1
print('Wrapping paper len = ', sum((2*df['len']*df['wid']) + (2*df['len']*df['hei']) + (2*df['hei']*df['wid']) +
   pd.concat([(df['len']*df['wid']), (df['len']*df['hei']), (df['hei']*df['wid'])], axis=1).min(axis=1)))

# Part 2
print('Ribbon length = ', sum((df['len']*df['wid']*df['hei'])+    
    (pd.concat([(df['len']+df['len']+df['hei']+df['hei']),
                (df['hei']+df['hei']+df['wid']+df['wid']),
                (df['wid']+df['wid']+df['len']+df['len'])], axis=1).min(axis=1))))
