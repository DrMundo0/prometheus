// 80. 删除有序数组中的重复项 II
// https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
// medium
// 给定一个按 非递减顺序 排列的整数数组 nums，请你 原地 删除部分重复元素，使得每个不同的元素 最多出现两次。元素的 相对顺序 应保持 不变。
// 
// 由于在某些语言中无法改变数组的长度，因此必须将结果放在数组 nums 的前半部分。更准确地说，如果删除重复元素后有 k 个元素，那么 nums 的前 k 个元素应该保存最终结果。前 k 个元素之后的内容无关紧要。
// 
// 将最终结果放入 nums 的前 k 个位置后，返回 k。
// 
// 不要 为另一个数组分配额外空间。你必须使用 O(1) 的额外内存，通过 原地 修改输入数组 来完成此操作。
// 
// 自定义判题：
// 
// 判题程序将使用以下代码测试你的解答：
// 
// int[] nums = [...]; // 输入数组
// int[] expectedNums = [...]; // 长度正确的预期答案
// 
// int k = removeDuplicates(nums); // 调用你的实现
// 
// assert k == expectedNums.length;
// for (int i = 0; i < k; i++) {
    // assert nums[i] == expectedNums[i];
// }
// 如果所有断言都通过，那么你的解答将被 接受。
class Solution
{
    public int removeDuplicates(int[] nums) {
        int n = nums.length;

        // 前两个数不用管，如果数组长度本来就很短（只有 0、1 或 2 个元素），那根本不需要去重，直接把长度返回就行了，因为它们最多也就出现 2 次
        if (n <= 2) {
            return n;
        }

        // 双指针登场
        // 既然前两个数绝对安全，我们干脆从第 3 个数（下标 2）开始检查
        // 这里定义了两个指针：
        // fast（快指针）：负责像探路员一样，挨个往后扫描数组里的每一个数字
        // slow（慢指针）：负责把“合法”的数字按顺序重新填回到数组的前面去
        int slow = 2, fast = 2;

        while (fast < n) {
            // 为什么跟 slow - 2 比？
            // 因为数组是从小到大排好序的，相同的数字肯定都连在一起。
            // 如果当前快指针看到的数字 (nums[fast])，和慢指针往前数两个位置的数字 (nums[slow - 2]) 不相等，这就说明：这个数字如果放进来，它连续出现的次数绝对不会超过 2 次！（因为如果超了，slow - 2 那个位置的数就会和当前数相同）
            if (nums[slow - 2] != nums[fast]) {
                // 如果安全（不相等），就把快指针指向的数复制到慢指针的位置 (nums[slow] = nums[fast])，然后慢指针往前走一步 (++slow)
                nums[slow] = nums[fast];
                ++slow;
            }

            // 不管安不安全，快指针 fast 每次都要往前走一步，继续看下一个数 (++fast)
            ++fast;
        }

        // 当快指针把整个数组扫完后，slow 停下来的那个位置，正好就是处理完之后新数组的长度。
        return slow;
    }
}
