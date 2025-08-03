"""
data = 'flag_0_fflag_1_lflag_2_aflag_3_gflag_4_{flag_5_fflag_6_3flag_7_dflag_8_3flag_9_rflag_10_4flag_11_tflag_12_1flag_13_0flag_14_nflag_15_-flag_16_0flag_17_fflag_18_-flag_19_tflag_20_hflag_21_3flag_22_-flag_23_pflag_24_lflag_25_4flag_26_nflag_27_3flag_28_tflag_29_sflag_30_-flag_31_8flag_32_8flag_33_4flag_34_1flag_35_bflag_36_eflag_37_9flag_38_2flag_39_}'

x = 0
flag = data.replace('flag', '')
print(flag)


import re

data = "_0_f_1_l_2_a_3_g_4_{_5_f_6_3_7_d_8_3_9_r_10_4_11_t_12_1_13_0_14_n_15_-_16_0_17_f_18_-_19_t_20_h_21_3_22_-_23_p_24_l_25_4_26_n_27_3_28_t_29_s_30_-_31_8_32_8_33_4_34_1_35_b_36_e_37_9_38_2_39_}"

# Rimuovi i numeri e gli underscore fuori dalle parentesi graffe
cleaned_data = re.sub(r'(_[0-9]+_|\-)(?![^{}]*\})', '', data)

# Mantieni solo lettere, numeri e parentesi graffe
cleaned_data = ''.join(c for c in cleaned_data if c.isalpha() or c.isdigit() or c in "{}")

print(cleaned_data)
"""

#flag{f3d3r4t10n-0f-th3-pl4n3ts-8841be92}




