package JM.DAY1

/*
<문제>
[동전 0](https://www.acmicpc.net/problem/11047)

<구현 방법>
큰 동전을 먼저 확인하고 나눌 수 있으면 최대한 나누며 k를 갱신한다.

<트러블 슈팅>
 */
fun main() {
    var (n, k) = readln().split(" ").map{ it.toInt() }
    val coinTypes = mutableListOf<Int>()
    repeat(n) {
        coinTypes.add(readln().toInt())
    }
    coinTypes.reverse()
    var idx = 0
    var result = 0
    while (k > 0) {
        if (coinTypes[idx] <= k) {
            result +=  k / coinTypes[idx]
            k %= coinTypes[idx]
        }
        idx += 1
    }
    println(result)
}