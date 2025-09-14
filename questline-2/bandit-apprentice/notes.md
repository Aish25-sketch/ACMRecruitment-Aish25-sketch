# Bandit Apprentice Notes (Levels 0–10)

## Level 0-1
- **Username:** bandit0 
- **Password:** bandit0 
- **Command:** 
  '''bash
  cat readme
## Level 1-2
- **Command:**
  '''cat ./-
## Level 2-3
- **Command:**
  '''cat "spaces in this filename"
## Level 3-4
- **Command:**
  '''cd inhere
  '''ls -a
  '''cat .hidden
## Level 4-5
- **Command:**
  '''cd inhere
  '''file ./-file*
  '''cat ./-file07
## Level 5-6
- **Command:**
  '''find . -type f -size 1033c ! -executable
  '''cat ./maybehere07/.file2
## Level 6-7
- **Command:**
  '''find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
  '''cat /var/lib/dpkg/info/bandit7.password
## Level 7-8
- **Command:**
  '''grep "millionth" data.txt
## Level 8-9
- **Command:**
  '''sort data.txt | uniq -u
## Level 9-10
- **Command:**
  '''strings data.txt | grep ===
