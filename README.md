# Basic_Scripts
Basic Python Scripts 

## Windows UAC
User Account Control (UAC) is a security component in Windows operating systems that enables users to perform common tasks as non-administrators and as administrators without having to switch users, log off, or use the option “Run As.”

Every time that a user attempts to perform a task that requires a user administrative access, the consent prompt is presented:

The binary contains “auto-elevation” settings in its manifest file, it’s created and digitally signed by Microsoft, and is housed in a trusted file location(C:\Windows\System32). This means that a UAC prompt won’t show when running this binary.

In short, what was found was that during the execution of the fodhelper.exe binary, the OS looks for additional commands to be executed based on two registry keys:

```
Software\Classes\ms-settings\shell\open\command\(default)
Software\Classes\ms-settings\shell\open\command\DelegateExecute
```

With that in mind, an attacker could change those registry keys and delegate any kind of code to be executed on the users’ behalf without any consent.
