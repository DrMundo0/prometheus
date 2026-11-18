// 412. Fizz Buzz
// easy
// 给你一个整数 n ，返回一个字符串数组 answer（下标从 1 开始），其中：
// answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
// answer[i] == "Fizz" 如果 i 是 3 的倍数。
// answer[i] == "Buzz" 如果 i 是 5 的倍数。
// answer[i] == i （以字符串形式）如果上述条件全不满足。
class Solution
{
    public List<String> fizzBuzz(int n) {
        List<String> answer = new ArrayList<String>();

        for (int i = 1; i <= n; i++) {
            StringBuffer sb = new StringBuffer();

            if (i % 3 == 0) {
                sb.append("Fizz");
            }

            if (i % 5 == 0) {
                sb.append("Buzz");
            }

            if (sb.length() == 0) {
                sb.append(i);
            }

            answer.add(sb.toString());
        }
        
        return answer;
    }
}
