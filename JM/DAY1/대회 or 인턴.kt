package JM.DAY1

import java.lang.Integer.min
fun main() {
    val (n, m, k) = readln().split(" ").map{ it.toInt() }
    var team = min(n/2, m)
    while(n + m - team *3 < k) {
        team--
    }
    println(team)
}