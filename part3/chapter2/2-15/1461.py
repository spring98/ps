'''
    해설
    0보다 큰 책들과 0보다 작은 책들을 나누어서 처리한다.
        -> 이유는 어차피 0에 책이 있기 때문에 부호가 바뀌면
            따로 처리해도 같이 처리하나 같음, 계산의 편리(라고 생각)
    2개의 우선순위 큐를 사용한다.
    가장 먼 책을 마지막으로 놓는다.
    음수와 양수에 대하여 개별적으로 M 개씩 묶어서 처리한다.
    M개씩 묶음 중에서 가장 거리가 먼 책만큼 이동한다.
    묶음의 최대 값들을 모두 더한 후 가정 먼 책의 편도거리만 뺀다.
'''