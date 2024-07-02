# AI8CB (AI팔코봇)

[팔만코딩경(80000Coding)](https://80000coding.oopy.io/)에 있는 게시글들에 대해서 '이날의 게시글' 이라는 소개글을 작성해서 게시해주는 AI봇

![](/images/ai8cb-introducing-operation.png)
- [원본 게시글](https://80000coding.oopy.io/d9470feb-e824-4077-bf17-02dd64d72b1c#d9470feb-e824-4077-bf17-02dd64d72b1c)
- [결과물](https://github.com/refigo/ai8cb/issues/7)


## 작동 원리 구조

![](/images/ai8cb-operation-structure.png)

1. 게시글을 균일 토큰 단위로 분할
2. 분할된 토큰 단위로 개별 요약
3. 개별 요약본들을 합쳐서 최종 요약본 생성
4. 최종 요약본으로 소개글 생성
5. 생성된 소개글을 전달 매체에 게시 (ex. Github, Slack, Discord, ...)


## 사용 방법

- Cloning Repository
```bash
git clone https://github.com/refigo/ai8cb.git
```

- Setting venv
```bash
(venv-ai8cb) $ pip install -r requirements.txt
```

- Setting environment variable
```.env
OPENAI_API_KEY=

GITHUB_TOKEN=
DISCORD_WEBHOOK_URL=
```

- Executing with a link as argument
```bash
(venv-ai8cb) $ python3 copywriter.py <url-of-article>
```
여기서 `<url-of-article>` 부분은 해당 게시글 URL로 대체하세요.


## 주요 라이브러리

- OpenAI
- transformers
	- GPT2TokenizerFast
- requests
- bs4


## 주요 기능 소개

- Getting text of an article
- Summarizing
- Copywriting
- Posting


## 로드맵

- [x] Getting Text ✅ 2024-04-01
- [x] Summarize ✅ 2024-04-01
	- [x] Tokenizing with GPT2TokenizerFast
	- [x] Chunkify - Splitting token into evenly sized chunks
	- [x] Setting to use OpenAI
- [x] Copywrite ✅ 2024-04-01
	- [x] Prompt Engineering
- [x] Post to Slack with Github issue ✅ 2024-04-01
- [x] Post to Discord using webhook ✅ 2024-04-04
- [ ] Auto Link Selector
- [ ] Automation Daily Execution
- [ ] Fine Tuning


## Author

Mijong Go (mgo in 42Seoul) - mgo@student.42seoul.kr


## License

MIT 라이센스에 따라 배포됩니다. 자세한 내용은 LICENSE 내용을 참조하십시오.