// Node.js script to generate a random key for use in the .env file
const crypto = require("crypto");

function generateKey() {
  return crypto.randomBytes(64).toString("hex");
}

console.log(generateKey());
