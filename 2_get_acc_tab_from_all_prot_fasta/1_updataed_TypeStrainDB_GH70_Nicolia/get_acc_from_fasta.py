# get ACC_# from all_pro.fasta
# output as a label.tab

from Bio import SeqIO
in_fasta_f_name = "all_prot.fasta"
out_tab_f_name = "label.tab"

out_tab_f = open(out_tab_f_name, 'w')

acc_list = []

for seq_record in SeqIO.parse(in_fasta_f_name, "fasta"):
    acc_full = seq_record.id
    acc = "_".join(acc_full.split("_")[:-1]) + "_"
    acc_list.append(acc)
    acc_list = list(set(acc_list)) # remove duplicates from list

out_tab_f.write('\n'.join(acc_list))

out_tab_f.close()
# print(len(acc_list))

