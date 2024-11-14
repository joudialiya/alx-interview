#!/usr/bin/node

const request = require('request');

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err;
    } else {
      const characters = JSON.parse(body).characters;
      let i = 0;
      while (i < characters.length) {
        request(characters[i], (err, response, body) => {
          if (err) {
            throw err;
          } else {
            console.log(JSON.parse(body).name);
            i = i + 1;
          }
        });
      }
    }
  }
);
