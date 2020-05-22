import tweepy

def main():
    #認証キーを入力する。TwitterAPIの認証してtweepyをインストールする
    CONSUMER_KEY = 'fS3iY1VNmgIyYeZB0MlxqdXgC'
    CONSUMER_SECRET = '6RPvbFXBDuEEe7Oc5cJd4sr1fuJQ5uJvpzCRq6cCFvxMKKoivY'
    ACCESS_TOKEN = '1218165498791129088-b26TOpezVbyXWew0VA2Dh5TjQwQR8p'
    ACCESS_TOKEN_SECRET = 'BClfbCB8dC8AtMKtZnOpQH7XsRIB7WYSQlpg4XgenZTI1'
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    api=tweepy.API(auth)
    
    #リストに検索クエリーを記述。
    query_list=["マレーシア","Malaysia"]
    #取得件数を記述。カウントに数値を設定しないと無限ループになる
    count=50
    for query in query_list:
        #検索中のクエリーを出力
        print('Searching:QUERY-->>{}'.format(query))
        #ツイートのデータであるstatusオブジェクトを取得
        search_results=api.search(q=query,count=count)
        for status in search_results:
            tweet_id=status.id
            #ツイートidにアクセス
            try:
                #いいねする
                api.create_favorite(tweet_id)
            except:
                #例外はパスする
                pass
            
if __name__ == '__main__':
    main()