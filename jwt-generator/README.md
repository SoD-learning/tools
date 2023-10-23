# JWT Generator

## Contents

- [Description for developers](#developer-description)
- [Description for non-developers](#non-developer-description)

## Developer Description 👨‍💻

### Project Overview:

The sole purpose of this script is to generate a 128-hexadecimal string. It leverages the `crypto` module from Node.js to generate the key.

### Technology Used

- Node.js

### File Structure:

- `generateKey.js`: The main and only file in this utility.

### Usage:

1. Ensure you have Node.js installed on your machine and initialise the project: `npm init`.
2. Run `node generateKey.js` in your terminal.
3. The script will output a 128-character hexadecimal string.

### Why was this created?

- It automates the process of key generation, ensuring consistency and saving developer time.
- By using a cryptographically secure method to generate the key, it helps in maintaining a high level of security within an application.

---

## Non-Developer Description 🙍‍♂️

### Project Overview:

This script is a simple tool that helps us create a special kind of password, called a 'key', in order to obfuscate sensitive information like database credentials. This key helps to keep our project's sensitive information safe. It’s a small but important part of our project’s security system.

### How it Works:

- When run, this tool gives us a new, random key each time.
- This new key is then used in a special file that helps keep our project's sensitive data protected.

### Why was this created?

- It’s a simple way to get a new key whenever needed without any hassle.
- It helps keep our project’s sensitive data safe by providing strong keys, which are hard for bad actors to guess.
