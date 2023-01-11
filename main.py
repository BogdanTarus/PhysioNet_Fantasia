
## import the WFDB package
import wfdb

records_list = wfdb.get_record_list('fantasia/1.0.0')

record_header = wfdb.rdheader(record_name='f1o01', pn_dir='fantasia/1.0.0')
signal_numbers = record_header.n_sig
signal_names = record_header.sig_name

print(type(record_header))
print("signal_numbers: ", signal_numbers)
print("signal_names: ", signal_names)

# wfdb.io.rdann(record_name, extension, sampfrom=0, sampto=None, shift_samps=False, pn_dir=None, return_label_elements=['symbol'], summarize_labels=False)

rr_annotation = wfdb.rdann(record_name='f1o01', extension='ecg', pn_dir='fantasia/1.0.0')

