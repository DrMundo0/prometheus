// 189. 轮转数组
// https://leetcode.cn/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
// medium
// 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
class Solution
{
    public void rotate(int[] nums, int k) {
        // 记录原数组长度 n，并初始化一个等长的新数组 newArr，用来暂存轮转后的元素，避免在遍历时直接覆盖原数组导致数据丢失
        int n = nums.length;
        int[] newArr = new int[n];

        for (int i = 0; i < n; ++i) {
            // 原数组中下标为 i 的元素，向右移动 k 步后，理论新下标是 i + k
            // 当 i + k 超过或等于数组长度 n 时，需要绕回数组开头，因此使用取模运算 (i + k) % n 实现循环下标
            // 即使 k 大于 n（例如数组长为 5，要右移 7 步），取模也能正确映射到对应的位置
            newArr[(i + k) % n] = nums[i];
        }

        // System.arraycopy 是 JVM 提供的原生底层拷贝方法，参数含义依次为：
        // newArr：源数组
        // 0：源数组的起始复制位置
        // nums：目标数组
        // 0：目标数组的起始存放位置
        // n：要复制的元素个数
        System.arraycopy(newArr, 0, nums, 0, n);
    }
}
