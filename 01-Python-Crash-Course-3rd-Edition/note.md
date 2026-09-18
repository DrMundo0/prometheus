坚持使用虚拟机提交代码，所以怎么让 VirtualBox 中的 Ubuntu 虚拟机使用宿主机上的显卡？

说实话，我有点不想弄乱物理机，就在虚拟机里折腾

所以我们百度下 How to access GPU from Ubuntu 22 VM running in Virtual Box on Windows 10? https://superuser.com/a/1767617

回答中给出了两篇文章：
1. [Running GPU passthrough for a virtual desktop with Hyper-V](https://www.techtarget.com/searchvirtualdesktop/tip/Running-GPU-passthrough-for-a-virtual-desktop-with-Hyper-V)
2. [Tutorial: Passing through GPU to Hyper-V guest VM](https://www.tenforums.com/virtualization/195745-tutorial-passing-through-gpu-hyper-v-guest-vm.html)

## Hyper-V

第一篇文章中提到了 Hyper-V，什么是 Hyper-V？
https://learn.microsoft.com/zh-cn/windows-server/virtualization/hyper-v/get-started/Install-Hyper-V?tabs=powershell&pivots=windows
