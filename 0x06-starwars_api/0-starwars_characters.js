#!/usr/bin/node

const request = require('request');
const fetchChars = (characters, index) => {
  if (index === characters.length) return;
  request(characters[index], (err, response, body) => {
    if (err) {
      throw err;
    } else {
      console.log(JSON.parse(body).name);
      fetchChars(characters, index + 1);
    }
  });
};

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err;
    } else {
      const characters = JSON.parse(body).characters;
      fetchChars(characters, 0);
    }
  }
);
