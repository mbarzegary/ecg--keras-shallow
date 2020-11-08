from train_keras import main, main_DP, main_federated

# Call different configurations for train_SVM.py 

####################################################################################
winL = 90
winR = 90
do_preprocess = True
maxRR = True
compute_morph = {''} # 'wvlt', 'HOS', 'myMorph', 'u-lbp'

reduced_DS = False # To select only patients in common with MLII and V1
leads_flag = [1,0] # MLII, V1

use_RR = True
norm_RR = False
compute_morph = {'myMorph'} 

# main(winL, winR, do_preprocess, maxRR, use_RR, norm_RR, compute_morph, reduced_DS, leads_flag)

# noise_list = [0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
# for noise in noise_list:
#     main_DP(winL, winR, do_preprocess, maxRR, use_RR, norm_RR, compute_morph, reduced_DS, leads_flag, noise)

main_federated(winL, winR, do_preprocess, maxRR, use_RR, norm_RR, compute_morph, reduced_DS, leads_flag)
