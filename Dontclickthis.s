.section  .data
msg:
    .asciz "Hello, World!\n"   # Define a null-terminated string with a newline
msg_len = . - msg              # Length from current location to msg

.section .text
.globl _start              # Declare _start as a global symbol (entry point)
_start:
    # --- sys_write(int fd, const void *buf, size_t count) ---
    movl $4, %eax              # sys_write into %eax
    movl $1, %ebx              # fd stdout into %ebx
    movl $msg, %ecx            # msg address
    movl $msg_len, %edx        # msg length
    int $0x80                  # Trigger the kernel system call

    # --- sys_exit(int status) ---
    movl $1, %eax              # sys_exit into %eax
    xorl %ebx, %ebx            # Zero out %ebx (exit code 0)
    int $0x80                  # Kernel call
