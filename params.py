xg_params = {'max_depth': 14, 'learning_rate': 0.034583691423507874, 'min_child_weight': 56,
             'gamma': 0.03134932674402008, 'subsample': 0.841092374719567, 'colsample_bynode': 0.4544908220235693,
             'colsample_bytree': 0.47560907676414077, 'reg_alpha': 2.544481586005913e-07,
             'reg_lambda': 1.598331373566232e-05, 'scale_pos_weight': 5}
xg_params_without_oh = {'max_depth': 6, 'learning_rate': 0.02087182491726285, 'min_child_weight': 4,
                        'gamma': 0.03055868851171002, 'subsample': 0.24298396203608008,
                        'colsample_bynode': 0.2496988845198069, 'colsample_bytree': 0.33054290421393945,
                        'reg_alpha': 0.016852987952045692, 'reg_lambda': 0.3254904131239201, 'scale_pos_weight': 2}

cb_cat_features_params = {'learning_rate': 0.012492905385099772, 'objective': 'CrossEntropy',
                          'colsample_bylevel': 0.3946170174514822, 'min_data_in_leaf': 43, 'depth': 7,
                          'boosting_type': 'Plain', 'bootstrap_type': 'MVS'}

cb_params = {'learning_rate': 0.023034450123221473, 'objective': 'CrossEntropy',
             'colsample_bylevel': 0.38751922976147585,
             'min_data_in_leaf': 41, 'depth': 8, 'boosting_type': 'Ordered', 'bootstrap_type': 'Bayesian',
             'bagging_temperature': 5.562886679659466}
li_cat_features_params = {'subsample': 0.7115185946603728, 'learning_rate': 0.024023736944555056,
                          'colsample_bytree': 0.14329151151137828, 'reg_alpha': 0.30974329894538843,
                          'reg_lambda': 0.6316534790805843, 'scale_pos_weight': 1, 'num_leaves': 128, 'max_depth': 4,
                          'min_child_samples': 162}

li_params = {'subsample': 0.1556374166425304, 'learning_rate': 0.014450008402834034,
             'colsample_bytree': 0.13263115321921576, 'reg_alpha': 0.9499820492262308, 'reg_lambda': 0.45452325900163,
             'scale_pos_weight': 2, 'num_leaves': 53, 'max_depth': 5, 'min_child_samples': 184}
