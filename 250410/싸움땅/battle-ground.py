n, m, k = map(int, input().split())

# 총 초기화 (총이 있다면 리스트로, 없으면 빈 리스트)
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append([[x] if x != 0 else [] for x in row])

# 플레이어 초기화: x, y, 방향, 초기 능력치, 총 능력치(0)
player = []
for _ in range(m):
    x, y, d, s = map(int, input().split())
    player.append([x - 1, y - 1, d, s, 0])

# 플레이어 위치 저장 배열
parr = [[0] * n for _ in range(n)]
for i in range(m):
    x, y = player[i][0], player[i][1]
    parr[x][y] = i + 1  # 1-based 인덱스로 저장

# 점수 배열
point = [0] * m

# 방향: 상 우 하 좌
def dir(x, y, d):
    if d == 0:
        return x - 1, y
    elif d == 1:
        return x, y + 1
    elif d == 2:
        return x + 1, y
    else:
        return x, y - 1

# 반대 방향
opp = {0: 2, 1: 3, 2: 0, 3: 1}

# 진 사람 이동 함수
def go(i, j, idx):
    d = player[idx][2]
    for _ in range(4):
        ni, nj = dir(i, j, d)
        if 0 <= ni < n and 0 <= nj < n and parr[ni][nj] == 0:
            player[idx][0], player[idx][1], player[idx][2] = ni, nj, d
            parr[i][j] = 0
            parr[ni][nj] = idx + 1
            # 총 줍기
            if arr[ni][nj]:
                best = max(arr[ni][nj])
                player[idx][4] = best
                arr[ni][nj].remove(best)
            return
        d = (d + 1) % 4  # 시계 방향 회전

# k턴 반복
for _ in range(k):
    for idx in range(m):
        pi, pj, d, ph, gun = player[idx]

        # 이동
        ni, nj = dir(pi, pj, d)
        if not (0 <= ni < n and 0 <= nj < n):
            d = opp[d]
            ni, nj = dir(pi, pj, d)

        # 방향 갱신
        player[idx][2] = d

        # 위치 이동
        parr[pi][pj] = 0

        # 이동 위치에 다른 사람이 있는 경우
        if parr[ni][nj] != 0:
            opp_idx = parr[ni][nj] - 1
            opp_ph, opp_gun = player[opp_idx][3], player[opp_idx][4]
            me_power = ph + gun
            opp_power = opp_ph + opp_gun

            # 승자 결정
            if me_power > opp_power or (me_power == opp_power and ph > opp_ph):
                winner, loser = idx, opp_idx
            else:
                winner, loser = opp_idx, idx

            # 점수 추가
            point[winner] += abs(player[idx][3] + player[idx][4] - player[opp_idx][3] - player[opp_idx][4])

            # 패배자 총 내려놓기
            arr[ni][nj].append(player[loser][4])
            player[loser][4] = 0

            # 패배자 이동
            go(ni, nj, loser)

            # 승자 총 줍기
            if arr[ni][nj]:
                best = max(arr[ni][nj])
                if player[winner][4] < best:
                    arr[ni][nj].append(player[winner][4])
                    arr[ni][nj].remove(best)
                    player[winner][4] = best

            # 승자 위치 갱신
            player[winner][0], player[winner][1] = ni, nj
            parr[ni][nj] = winner + 1

        else:
            # 사람이 없다면 총 줍기
            if arr[ni][nj]:
                best = max(arr[ni][nj])
                if gun < best:
                    arr[ni][nj].append(gun)
                    arr[ni][nj].remove(best)
                    gun = best

            # 위치 갱신
            player[idx] = [ni, nj, d, ph, gun]
            parr[ni][nj] = idx + 1

# 최종 점수 출력
print(*point)
