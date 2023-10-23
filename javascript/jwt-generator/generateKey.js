// This is a script written in Node.js to generate a random 128-character hexadecimal key.
// This key can be used in a .env file to keep sensitive data secure.

// Import the 'crypto' module from Node.js, which provides cryptographic functionalities.
const crypto = require("crypto");

// Define a function named 'generateKey' to encapsulate the key generation logic.
function generateKey() {
  // 'crypto.randomBytes(64)' generates 64 random bytes of data.
  // '.toString("hex")' converts these random bytes into a hexadecimal string.
  // Since each byte is represented by two hexadecimal characters,
  // the final string is 128 characters long.
  return crypto.randomBytes(64).toString("hex");
}

// Call the 'generateKey' function and print the resulting key to the console.
// This way, you can see the generated key and copy it for use in your .env file.
console.log(generateKey());
