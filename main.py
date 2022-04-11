
# import the WFDB package
import wfdb

record_header = wfdb.rdheader(record_name='f1o01', pn_dir='fantasia/1.0.0')
signal_numbers = record_header.n_sig
signal_names = record_header.sig_name

print(type(record_header))
print("signal_numbers: ", signal_numbers)
print("signal_names: ", signal_names)

