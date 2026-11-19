// 122. 买卖股票的最佳时机 II
// https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150
// medium
// 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
// 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。然而，你可以在 同一天 多次买卖该股票，但要确保你持有的股票不超过一股。
// 返回 你能获得的 最大 利润 。
class Solution
{
    public int maxProfit(int[] prices) {
        // n 是价格数组的长度（总天数）
        int n = prices.length;
        int[][] dp = new int[n][2];
        // 第 0 天不持股：什么都不做，利润为 0
        dp[0][0] = 0;
        // 第 0 天持股：买入第 0 天的股票，利润记为 -prices[0]（相当于投入成本）
        dp[0][1] = -prices[0];

        // 第 1 天到第 n - 1 天
        for (int i = 1; i < n; ++i) {
            // 第 i 天不持有股票时的最大利润
            // 计算 dp[i][0]（今天不持股）有两种方式取最大值：
            // dp[i - 1][0]：昨天就不持股，今天继续观望（不操作）
            // dp[i - 1][1] + prices[i]：昨天持有股票，今天按 prices[i] 卖出，加上卖出所得
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
            // 第 i 天持有股票时的最大利润
            // 计算 dp[i][1]（今天持股）也有两种方式取最大值：
            // dp[i - 1][1]：昨天就持有股票，今天继续持有
            // dp[i - 1][0] - prices[i]：昨天不持股，今天花 prices[i] 买入一支新股票（因为允许多次交易，可以用此前积累的利润 dp[i - 1][0] 减去今天的买入价）
            dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
        }

        // 最后一天（第 n - 1 天）结束时，手里不持股的最大利润一定大于或等于持股时的利润（因为卖掉股票才能把账面价值变成实际利润），所以直接返回 dp[n - 1][0]
        return dp[n - 1][0];
    }
}
