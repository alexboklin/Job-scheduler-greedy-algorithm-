This is the implementation of the greedy algorithm that optimally schedules jobs in decreasing order of the ratio (weight/length) in order to minimize the weighted sum of completion times. The program reports the sum of weighted completion times and optionally prints the sequence of jobs with corresponding completion times to the standard output. (If two jobs have equal ratio (weight/length), the job with higher weight is scheduled first.)
The input file should describe a set of jobs with positive and integral weights and lengths and have the following format:
[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...
For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59. 
