# Algorithm Study K

## 폴더 생성 방법
주차 - 문제 폴더 (문제번호) - 코드 파일 (문제번호_이름)

ex) 1주차 - 2557 - 2557_yonghee.py

* 1주차
  * 2557
    * 2557_yonghee.py
  * 10718
    * 10718_yonghee.py

## Git Branch

### 원격저장소 로컬에 가져오기

<code> git clone https://github.com/Algoritm-Study-K/First_week.git </code>

### 로컬에서 개인 브랜치 생성하기

local repository에 name(본인의 이름) 브랜치 생성<br>
<code> git branch name </code>

### 로컬에서 브랜치 작업후 원격저장소에 반영하기

로컬 브랜치가 있는 폴더에서 개인작업을 마친 후 공동 저장소에 반영한다.

1. <code> **git checkout name** </code> - main에서 name 브랜치로 전환 (name : 본인의 이름)
2. workspace에서 작업
3. <code> **git commit -add .**</code> - 작업한 내용 스테이지에 추가
4. <code> **git commit -m "message"**</code> - 작업한 내용 커밋 (message 예시 : "1000_yonghee")
5. <code> **git push origin name** </code> - 원격저장소에 name 브랜치에 반영 
6. <code> **git checkout main** </code> - main 브랜치로 브랜치 전환
7. <code> **git pull** </code> - 원격저장소 main의 최신 정보를 로컬에 업데이트 시키기
8. <code> **git merge name** </code> - main에 name 브랜치 작업 반영
9. <code> **git push origin main** </code> - 원격저장소 main에 반영
