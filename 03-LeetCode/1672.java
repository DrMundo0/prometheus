// 1672. 最富有客户的资产总量
// easy
// 给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i​​​​​​​​​​​​ 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的资产总量 。
// 客户的资产总量就是他们在各家银行托管的资产数量之和。最富有客户就是资产总量最大的客户。
class Solution
{
    public int maximumWealth(int[][] accounts) {
        int maxWealth = Integer.MIN_VALUE;

        for (int[] account : accounts) {
            maxWealth = Math.max(maxWealth, Arrays.stream(account).sum());
        }

        return maxWealth;
    }
}
