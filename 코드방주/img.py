def download(url,target):
    session.headers.update({
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    })

    try:
        r=session.get(url,stream=True)
        r.encoding='utf-8'

        with open(target,'wb') as f:
            f.write(r.raw.read())
            print(target,'가 저장되었습니다.')
    except Exception as e:
        print(target,'저장실패',e)