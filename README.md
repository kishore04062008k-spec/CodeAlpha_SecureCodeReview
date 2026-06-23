# Secure Code Review

## Overview

I built a small Flask web application called "Notes Portal" 
and intentionally introduced common security vulnerabilities 
into it — then performed a full manual code review to find, 
document and fix each one. The idea was to learn security 
auditing on code I actually understood line by line, rather 
than diving into a large unfamiliar codebase.

## Technologies & Libraries

- Python 3
- Flask
- SQLite
- Manual Code Review (OWASP Top 10 Methodology)

## What the App Does

A basic notes web app with user registration, login and 
personal note storage — simple enough to read in one 
sitting but complex enough to contain real, exploitable 
vulnerabilities across multiple layers.

## Vulnerabilities Found
