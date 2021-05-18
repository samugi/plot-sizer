# Plot Size - best configuration calculator
Simple tool to calculate the best configurations of Chia plot sizes based on the total space available on the disk and the temporary size to plot

## Example
```
python sizer.py --disksize 8000000000000 --tempsize 600000000000

Calculating plots combinations for a disk of size: 8000000000000 bytes
Valid combinations:

 K32  k33  k34  k35     Wasted (MB)
  57    8    0    0     408.74
  24   24    0    0     6206.96
  59    7    0    0     6851.19
  26   23    0    0     12649.41
  ...
```
Or simply edit the `config.py` file and run:
```
python sizer.py
```