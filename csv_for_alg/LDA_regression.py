# -*-coding: utf-8 -*-

'''
学習フェーズ：
入力：アニメに関するFeature＆Preferenceデータ
出力：観るべきアニメ

予測フェーズ：
入力：アニメに関するFeatureデータ
出力：Preferenceの予測値
'''

#モジュール
import numpy as np
#np.seterr(divide='ignore', invalid='ignore') #RuntimeWarningを無視
from scipy import linalg, sparse, stats, special
from scipy.sparse import linalg as sp_linalg
from gensim.models import ldamodel
import matplotlib.pyplot as plt
import sys
import time

#ファイル群
flearn = 'feature_learn.csv'
plearn = 'preference_learn_notitle.csv'
fpred = 'feature_test.csv'
label = 'feature_2017autumn.csv'

def LDA_learning(inData):
    #変分ベイズ法によりパラメータを更新
    pass

def recommend(phi,theta,mu,sigma):
    #秋アニメのFeatureから評点を予測
    pass

def main():
    #データの読み込み
    LFeature = pd.read_csv(flearn,delimiter=',')
    LPreference = pd.read_csv(plearn,delimiter=',')
    PredData = pd.read_csv(fpred,delimiter=',')
    Labels = pd.read_csv(label,delimiter=',')

    Labels = Labels['タイトル']

    #パラメータチューニング
    phi ,theta, mu, sigma = LDA_learning(inData)

    #評点予測
    Result = recommend(phi,theta,mu,sigma)

    #結果表示
    print "***推薦結果***"
    for i in xrange(topN):
        print Labels[Result[i]]

if __name__=="__main__":
    main()