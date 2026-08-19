*******************************************************************************
* MACIS INPUT FILES FOR HYDROGEN CHAINS
* WM - Aug. 19, 2026
*******************************************************************************
I am including an example macis input file here for h12.
To adapt it for other molecules, use the data in the 
table below. See the readme in 
fcidumps/fcidumps/data/macis-input-examples/readme.txt
for more details. The output and wavefunction is included
as well.

The table blow provides the important input options for
each hydrogen chain including NACTIVE, NALPHA, and NBETA.
I also include the maximum number of determinants that
preserve the number of alpha and beta electrons for
each molecule. Due to the molecular point groups symmetry
and the minimal basis set used, the actual number of
non-zero amplitudes will be roughly half of max-dets.
For example, although there are 4 determinants for h2
that preserve nalpha and nbeta, there will only be 2
non-zero amplitudes in the wavefunction. For h14, that
means there will be roughly 6E6 non-zero amplitudes,
so we will probably need to go beyond this if we want
problems where we can't recover all of the determinants.

!molec.    nactive    nalpha     nbeta          max-dets
h02              2         1         1                 4
h04              4         2         2                36
h06              6         3         3               400
h08              8         4         4              4900
h10             10         5         5             63504
h12             12         6         6            853776
h14             14         7         7           1.2e+07
h16             16         8         8           1.7e+08
h18             18         9         9           2.4e+09
h20             20        10        10           3.4e+10
h22             22        11        11           5.0e+11
h24             24        12        12           7.3e+12
h26             26        13        13           1.1e+14
h28             28        14        14           1.6e+15
h30             30        15        15           2.4e+16
h32             32        16        16           3.6e+17
h34             34        17        17           5.4e+18
h36             36        18        18           8.2e+19
h38             38        19        19           1.2e+21
h40             40        20        20           1.9e+22
h42             42        21        21           2.9e+23
h44             44        22        22           4.4e+24
h46             46        23        23           6.8e+25
h48             48        24        24           1.0e+27
h50             50        25        25           1.6e+28
h52             52        26        26           2.5e+29
h54             54        27        27           3.8e+30
h56             56        28        28           5.9e+31
h58             58        29        29           9.0e+32
h60             60        30        30           1.4e+34
h62             62        31        31           2.2e+35
h64             64        32        32           3.4e+36
