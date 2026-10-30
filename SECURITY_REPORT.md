\# SQL Injection Security Lab — Day 8



\*\*Project:\*\* Local SQL Injection Training Lab  

\*\*Researcher:\*\* Donald Victor Muchura  

\*\*Environment:\*\* Python, Flask, SQLite  

\*\*Date:\*\* 30 October 2026



\## 1. Objective



To understand SQL injection, demonstrate how unsafe SQL query construction can expose database records, and implement parameterized queries to prevent the demonstrated vulnerability.



\## 2. Lab Environment



\- Python

\- Flask

\- SQLite

\- Localhost: `127.0.0.1:5001`

\- Fictional user records

\- Local testing only



\## 3. Vulnerability Identified



The original `/search` endpoint directly inserted user input into an SQL query using string interpolation.



This allowed specially crafted input to alter the intended SQL query logic.



\*\*Impact demonstrated:\*\* A crafted username returned all three fictional user records instead of only the requested account.



\## 4. Remediation



The vulnerable query was replaced with a parameterized SQLite query:



```python

query = """

&#x20;   SELECT id, username, email

&#x20;   FROM users

&#x20;   WHERE username = ?

"""



rows = conn.execute(query, (username,)).fetchall()

```



This separates SQL instructions from user-supplied values.



\## 5. Automated Security Testing



Four automated tests were executed:



| Test | Result |

|---|---|

| Normal Alice search | PASS |

| Normal Bob search | PASS |

| Unknown username | PASS |

| SQL injection attempt | PASS |



\*\*Final result: 4/4 tests passed.\*\*



\## 6. Security Findings



The original implementation was vulnerable to the demonstrated SQL injection payload.



After remediation, the same payload was treated as ordinary input and returned no matching records.



\## 7. Conclusion



This exercise demonstrated how SQL injection occurs when user input is directly incorporated into SQL statements.



Parameterized queries successfully prevented the specific injection demonstrated in this local lab.



The tests provide evidence that the tested behavior was corrected. They do not constitute a complete security audit or prove that all possible SQL injection vulnerabilities have been eliminated.



\## 8. Scope and Ethics



All testing was performed on a locally hosted application using fictional data. No third-party systems or real user accounts were accessed.



