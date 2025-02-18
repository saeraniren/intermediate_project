# 코드잇 스프린트 DA 5기 중급 프로젝트 Repository

<주의사항> (내용 추가시 디스코드로 공지할 예정)
1. 현재 작업하고 계시는 폴더의 상위 폴더에 clone을 진행해주세요
2. clone시 현재 저장소에 업로도 되어 있는 모든 데이터가 복제됩니다.<br/>
   이와 관련하여 clone 된 데이터는 <ins>되도록이면 삭제하지 않는 선에서 작업 부탁드립니다.</ins>
3. ``data`` 내 폴더에 현재 올라와있지 않은 데이터는 다음과 같습니다.<br/>
   이 데이터만 따로 복사/붙여넣기를 진행하시고 작업해주세요.<br/>
   또한, 이 데이터는 용량이 많이 크기 때문에 commit 시 이 데이터는 제외하고 commit/push를 진행해주세요.<br/>

   - ``enter.content_page.csv``
   - ``enter.lesson_page.csv``
4. 커밋 메세지는 ``작업 내용(홍길동)`` 와 같은 방식으로 입력해주시기 바랍니다.
5. 작업하신 ipynb 파일을 commit/push 시 이름은 ``<영문이름_이니셜_main.ipynb>``로 바꾼 후 진행해주시기 바립니다.
6. 현재 repository 내 파일은 팀 내 GitHub 관리자를 제외한 **<ins>임의의 수정 및 삭제는 자제 부탁드립니다.</ins>**
7. 이 repository는 향후 여러분들의 포트폴리오로 작성되기 위해 계속 공유된 상태로 열어둘 예정입니다!<br/>
   프로젝트가 끝날 시 ``data`` 내 모든 파일은 저작권 상의 이유로 지워지니 참고해주세요.

---

이하, GitHub사용 설명 관련입니다.<br/>
가장 크게 사용될 내용에 대해서 다루었고, 토글 방식으로 되어 있으니 클릭해서 봐주시면 감사드리겠습니다!<br/>
질문이 생기시면 저에게 말씀해주세요!

<details>
<summary>Git Clone 관련</summary>
<div markdown="1">


1. VSCode를 킨 뒤 F1 버튼을 눌러 ``Git:Clone`` 검색 후 ``Clone from GitHub`` 실행<br/>
![clone1](./img/clone1.png)<br/>
2. ``saeraniren/intermediate_project`` 검색<br/>
![clone2](./img/clone2.png)<br/>
3. 작업 영역을 만들 곳에 ``Select as Repository Destination`` 클릭<br/>
![clone3](./img/clone3.png)<br/>

</div>
</details>

<details>
<summary>Git Commit/Push 관련</summary>
<div markdown="1">

1. <ins>Clone으로 만들어진 작업 영역에서 꼭 시작하기</ins><br/>
2. 왼쪽 사이드의 아이콘 중 위에서 3번째 아이콘 클릭<br/>
![commit_push1](./img/commit_push1.png)<br/>
3. ``Changes`` 탭에 있는 파일 중 내가 업로드할 파일 선택 후 ``Staged Changes`` 탭에 잘 올라가져 있는지 확인<br/>
![commit_push2](./img/commit_push2.png)<br/>
4. VSCode 최상단 ``Terminal(터미널)`` 클릭 후 ``New Terminal(새 터미널)`` 선택<br/>
![commit_push3](./img/commit_push3.png)<br/>
5. 표시된 터미널에 ``git commit -m "상단의-예시"`` 입력 후 엔터<br/>
![commit_push4](./img/commit_push4.png)<br/>
6. ``git push origin main`` 입력 시 GitHub 저장소에 저장 완료<br/>
![commit_push15](./img/commit_push5.png)<br/>
</div>
</details>

---
