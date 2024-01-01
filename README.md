# 양승원T Discord ChatBot

[초대 링크](https://discord.com/api/oauth2/authorize?client_id=1191302757504786462&permissions=2048&scope=bot)

## 개요
양승원 선생님께서는 매우 특이한 카카오톡 말투를 가지신 선생님이시다. 그래서 나는 이것을 꼭 양승원 선생님과 카카오톡 채팅을 하지 않아도 느껴볼 수 있도록 이 ChatBot을 개발하게 되었다.

## 명령어
- `!yang` 양승원 선생님과 대화를 진행할 수 있다.

## 구현 방법
- OpenAI의 `gpt-4-1106-preview` 모델을 사용하였다.
- `!yang` 명령어를 입력하면 기존의 `prompt.txt` 파일 안에 있는 프롬프트 뒤에 사용자가 입력한 문장을 붙여서 OpenAI에 요청을 보낸다.
- 응답을 사용자에게 보여준다.