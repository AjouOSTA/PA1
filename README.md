# PA1: TAsh

코딩 덕후인 TA Mr.Choi는 Ubuntu의 bash 을 통해 채점을 진행하면서 "내가 만들어도 이것보단 낫겠다"는 생각을 하고 자신의 shell을 만들기로 했다. 채점하기 귀찮은 TA를 위해 편의 기능을 제공하는 TA shell을 만들어보자.

## 기본적인 shell 들의 기능

- Process creation

    * Scenario 1
    ```sh
    $ pwd
    $ /bin/ls
    ```
    
    * Scenario 2
    ```sh
    $ ~/workspace/PA0/course_sched
    $ cd ~/workspace/PA0
    $ make
    $ make run
    ```

- File redirection

    * Scenario 3
    ```sh
    $ echo "Good luck" > Big_Fan_Of_KO.txt
    $ echo "Good luck too" > Big_Fan_of_jafffy.txt
    $ echo "You can make it" > Manhattan.txt
    $ ls > students.txt
    $ grep Fan < students.txt
    ```
    
    * Scenario 4
    ```sh
    $ cd ~/workspace/PA0
    $ make
    $ make test
    ```

- Environmental variable

    * Scenario 5
    ```sh
    $ echo $PATH
    ```

## 채점 보조 기능

TA Mr.Choi는 채점을 위한 script를 작성했지만, 작성한 script들을 매번 찾아가 실행하기 귀찮았다. 그래서 shell이 시작하자마자 아래 python script가 마치 shell built-in command처럼 실행되도록 작성하려고 한다.

실행 예시는 아래와 같다.

    ```sh
    $ ls  # out; 2019-1-PA0/
    $ ready-to-grade 2019-1-PA0/ # python3 $(프로젝트 경로)/scripts/ready-to-grade.py 과 같은 의미
    $ auto-grade-pa0 2019-1-PA0/  # python3 $(프로젝트 경로)/scripts/auto-grade-pa0.py
    $ report-grade 2019-1-PA0/  # python3 $(프로젝트 경로)/scripts/report-grade.py
    ```

## 힌트와 팁

- `alias`
- `./scripts/generate-fake-pa0s.py` 을 통해 채점 보조 기능 검증을 위한 가짜 과제 파일 생성 가능

## 주의사항

- `system()` 등의 함수 사용 **엄격히** 금지. 해당 구현 부분 0점처리.
    - 추천: `fork()`와 `exec()` 계열 함수 사용
    - 뭘 써야 하는지 애매하면 물어보세요!

---

# Grading

- Deadline: **4월 7일 (일) 자정**
- 기본 shell 기능 70% (시나리오 하나당 1/5 * 70 = 14점)
- 보조 채점 기능 20%
- 보고서 10%
