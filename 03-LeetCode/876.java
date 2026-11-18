// 876. 链表的中间结点
// https://leetcode.cn/problems/middle-of-the-linked-list/description/
// easy
// 给你单链表的头结点 head ，请你找出并返回链表的中间结点。
// 如果有两个中间结点，则返回第二个中间结点。
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution
{
    public ListNode middleNode(ListNode head) {
        ListNode[] x = new ListNode[100];
        int i = 0;

        while (head != null) {
            x[i++] = head;
            head = head.next;
        }

        return x[i >> 1];
    }
}
